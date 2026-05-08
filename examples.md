# SendFlow SendAPI — Example Workflows

Copy-paste workflows for the most common tasks. All examples assume:

```bash
# Credential file
~/Documents/credentials/sendflow/main.json
{
  "apiKey": "your_key",
  "userId": "your_user_id",
  "baseUrl": "https://sendflow.pro/sendapi"
}
```

Examples below use `requests` (Python) and `fetch` (Node 18+ — no extra deps). For batteries-included clients with retry + rate-limit handling, see `clients/python.py` and `clients/node.js`.

---

## 1. List all your campaigns (releases)

```python
import requests, json, os

cred = json.load(open(os.path.expanduser("~/Documents/credentials/sendflow/main.json")))
r = requests.get(
    f"{cred['baseUrl']}/releases",
    headers={"Authorization": f"Bearer {cred['apiKey']}"},
)
r.raise_for_status()
for release in r.json():
    print(release["id"], release["name"], release["type"])
```

> ⚠️ **Rate limit:** 5 minutes minimum between calls to `GET /releases`. Cache the result.

---

## 2. Create a new campaign

```python
r = requests.post(
    f"{cred['baseUrl']}/releases",
    headers={"Authorization": f"Bearer {cred['apiKey']}"},
    json={
        "name": "Lançamento Q3 2026",
        "type": "WhatsRelease",  # or WhatsList, WhatsViralCampaign
        "projectId": "1234567890",  # optional
    },
)
r.raise_for_status()
release_id = r.json()["id"]
```

---

## 3. Send a text message to a campaign (broadcast to all groups)

The most common operation. The `actions/send-text-message` endpoint queues the message for delivery across all groups in a release.

```python
r = requests.post(
    f"{cred['baseUrl']}/actions/send-text-message",
    headers={"Authorization": f"Bearer {cred['apiKey']}"},
    json={
        "accountId": "pwYE3dPNWV5XtrrPbba0",   # OR accountIds: [...] for multi-account
        "releaseId": release_id,
        "messageText": "Olá! Estamos começando o lançamento.",
        "linkPreview": False,
        "options": {"shippingSpeed": "normal"},  # 40-60s between deliveries
    },
)
r.raise_for_status()
```

> ⚠️ **Rate limit:** 10 req/s per `releaseId` — shared across all `send-*-message` and `send-message` endpoints. Hit `403 "Limite de operações atingido!"` if exceeded.

### Variations

**Image:**
```python
{
    "accountId": "...",
    "releaseId": release_id,
    "url": "https://example.com/image.png",
    "caption": "Confira!",
    "options": {"shippingSpeed": "normal"},
}
# POST to /actions/send-image-message
```

**Video / Audio:** same shape as image, change endpoint to `/actions/send-video-message` or `/actions/send-audio-message`.

**Generic (any type):** use `POST /actions/send-message` with a `type` field (`extendedTextMessage`, `imageMessage`, `videoMessage`, `audioMessage`).

---

## 4. Schedule a message for the future

Add `scheduled: true` and `scheduledTo` (ISO 8601 UTC) to any send-message body:

```python
{
    "accountId": "...",
    "releaseId": release_id,
    "messageText": "Bom dia! Tem live hoje às 20h.",
    "scheduled": True,
    "scheduledTo": "2026-04-21T13:00:00.000Z",  # 10am BRT = 13:00 UTC
    "options": {"shippingSpeed": "normal"},
}
```

---

## 5. Send only to specific groups (not the whole campaign)

```python
{
    "accountId": "...",
    "releaseId": release_id,
    "messageText": "Mensagem só pros admins.",
    "chooseSpecificGroups": True,
    "groupIds": ["120363292004848696", "120363292004848697"],  # GIDs without @g.us
    "options": {"shippingSpeed": "normal"},
}
```

---

## 6. Create a group inside a campaign

Two-step: register the group in the campaign (`/release-groups`) **or** trigger a real WhatsApp group creation via Actions (`/actions/group-create`).

### a) Register an existing WhatsApp group in the campaign

```python
r = requests.post(
    f"{cred['baseUrl']}/release-groups",
    headers={"Authorization": f"Bearer {cred['apiKey']}"},
    json={
        "gid": "120363292004848696@g.us",
        "releaseId": release_id,
        "name": "Grupo VIP - Onda 1",
        "count": 0,
        "full": False,
        "type": "group",  # or community, community_default, community_group
    },
)
```

### b) Create a new WhatsApp group via Actions

```python
r = requests.post(
    f"{cred['baseUrl']}/actions/group-create",
    headers={"Authorization": f"Bearer {cred['apiKey']}"},
    json={
        "accountId": "...",
        "releaseId": release_id,
        "payload": {
            "name": "Grupo VIP - Onda 2",
            "participants": ["557581133148@s.whatsapp.net"],
            "standardization": False,
        },
    },
)
```

> ⚠️ **Rate limit:** 1s between calls + 60s per `releaseId`.

---

## 7. Get campaign analytics + lead scoring

```python
release_id = "De3MLuRlkjk8kGLp2cCnN"

# Analytics
analytics = requests.get(
    f"{cred['baseUrl']}/releases/{release_id}/analytics",
    headers={"Authorization": f"Bearer {cred['apiKey']}"},
).json()

# Lead scoring (top leads by engagement)
leadscoring = requests.get(
    f"{cred['baseUrl']}/releases/{release_id}/leadscoring",
    headers={"Authorization": f"Bearer {cred['apiKey']}"},
).json()

# Or download as a file
file_resp = requests.get(
    f"{cred['baseUrl']}/releases/{release_id}/leadscoring/download",
    headers={"Authorization": f"Bearer {cred['apiKey']}"},
)
open("leadscoring.csv", "wb").write(file_resp.content)
```

---

## 8. Verify a number before sending

Quick sanity check before adding a number to a sequence — avoids burning quota on already-blocked / opted-out numbers.

```python
r = requests.post(
    f"{cred['baseUrl']}/verify-number",
    headers={"Authorization": f"Bearer {cred['apiKey']}"},
    json={
        "releaseId": release_id,
        "phoneNumber": "11987654321",  # no country code, no symbols
    },
)
# Returns { "response": true } if blocked / unable to receive
```

---

## 9. Block a number (anti-spam)

```python
requests.post(
    f"{cred['baseUrl']}/block-numbers",
    headers={"Authorization": f"Bearer {cred['apiKey']}"},
    json={
        "number": "5511987654321",
        "name": "Spam — não enviar",
    },
)
```

List blocked numbers:
```python
blocked = requests.get(
    f"{cred['baseUrl']}/block-numbers",
    headers={"Authorization": f"Bearer {cred['apiKey']}"},
).json()
# Returns: ["5511987654321", ...]
```

---

## 10. Manage WhatsApp accounts (connect / disconnect / QR)

```python
# Create account
r = requests.post(
    f"{cred['baseUrl']}/accounts/create",
    headers={"Authorization": f"Bearer {cred['apiKey']}"},
    json={"data": {"name": "Conta Vendas", "type": "whatsapp"}, "projectId": "..."},
)
account_id = r.json()["id"]

# Trigger connect (asynchronously starts the WhatsApp link flow)
requests.post(
    f"{cred['baseUrl']}/accounts/connect-account/{account_id}",
    headers={"Authorization": f"Bearer {cred['apiKey']}"},
)

# Get QR code as JSON or PNG
qr_json = requests.get(
    f"{cred['baseUrl']}/accounts/{account_id}/qrcode",
    headers={"Authorization": f"Bearer {cred['apiKey']}"},
).json()

qr_image = requests.get(
    f"{cred['baseUrl']}/accounts/{account_id}/qrcode-image",
    headers={"Authorization": f"Bearer {cred['apiKey']}"},
)
open(f"qr-{account_id}.png", "wb").write(qr_image.content)
```

---

## 11. Find which group a number is in

Useful for support tickets — which campaign group does this number belong to?

```python
r = requests.post(
    f"{cred['baseUrl']}/actions/find-participant",
    headers={"Authorization": f"Bearer {cred['apiKey']}"},
    json={
        "accountId": "...",
        "phoneNumber": "5511987654321",
    },
)
# Returns matched groups across all releases of the account
```

---

## 12. Bulk send (10k+ numbers) — pattern with rate limit handling

```python
import time
from itertools import islice

NUMBERS = open("leads.csv").read().splitlines()
BATCH_SIZE = 5  # well under 10 req/s

def chunks(it, n):
    it = iter(it)
    while True:
        batch = list(islice(it, n))
        if not batch: return
        yield batch

for batch in chunks(NUMBERS, BATCH_SIZE):
    for number in batch:
        requests.post(
            f"{cred['baseUrl']}/send-text-message/{account_id}",
            headers={"Authorization": f"Bearer {cred['apiKey']}"},
            json={
                "text": f"Olá! Mensagem para {number}",
                "phoneNumber": number,
                "timeout": 60000,
            },
        )
    time.sleep(1.0)  # polite — keep well under 10 req/s
```

> For real production blasts, use `POST /actions/send-text-message` with `chooseSpecificGroups: true` and `groupIds` rather than 1-to-1 sends. Per-number sends are for support / surgical replies, not blasts.

---

## Error handling

The SendAPI returns `403 "Limite de operações atingido!"` when you hit any rate limit. Respect the documented intervals (see `SKILL.md` for the table) and implement exponential backoff:

```python
import time, random

def call_with_retry(method, url, **kwargs):
    for attempt in range(5):
        r = requests.request(method, url, **kwargs)
        if r.status_code == 403 and "Limite" in r.text:
            sleep_s = (2 ** attempt) + random.random()
            time.sleep(sleep_s)
            continue
        r.raise_for_status()
        return r
    raise Exception("Rate limit exceeded after 5 retries")
```

The `clients/python.py` and `clients/node.js` files in this skill ship with this pattern built in.

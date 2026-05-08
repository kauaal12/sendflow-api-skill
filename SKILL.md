---
name: sendflow-sendapi
description: SendFlow SendAPI integration for WhatsApp automation - send messages (text/image/video/audio), manage campaigns (releases), groups, accounts, message templates, and number blocks via REST API. Use when the user mentions sendflow, sendapi, sendi, "API do SendFlow", "disparar WhatsApp via API", "criar campanha sendi", "release groups", "lead scoring sendflow", or working with SendFlow's WhatsApp automation API for the Brazilian market.
version: 1.0.0
author: kauaalmeida
license: MIT
metadata:
  hermes:
    tags: [WhatsApp, API, Marketing, Automation, Brazil, SendFlow, REST]
    related_skills: [whatsapp-cloud-api, evolution-api]
    homepage: https://github.com/kauaalmeida/sendflow-api-skill
---

# SendFlow SendAPI

SendFlow ("Sendi") is a Brazilian WhatsApp automation platform used by major Hotmart/V4 operators for launches, lead scoring, group management, and bulk messaging. The **SendAPI** is its REST API, exposing 44 endpoints across 9 resource groups for fully programmatic access.

## When to use this skill

Activate when the user mentions any of:

- `sendflow`, `sendapi`, `sendi` (the brand or product name)
- "API do SendFlow", "disparar WhatsApp via API"
- "criar campanha SendFlow", "release groups", "lead scoring sendflow"
- "automação de grupos WhatsApp via API"
- working with `sendflow.pro/sendapi` URLs

**Don't use this skill when:**
- The user wants to integrate via SendFlow's **Webhooks** (different surface, uses the "Integrações" tab on `/whats/sendapi`).
- The user is using **Evolution API**, **WhatsApp Cloud API (Meta)**, or another WhatsApp provider — those have separate skills.

## Base URL and authentication

**Base URL:** `https://sendflow.pro/sendapi`
(Internally proxies to `https://southamerica-east1-whatsapp-ultimate.cloudfunctions.net/sendapi` — both work, prefer the canonical `sendflow.pro` URL.)

**Auth:** every endpoint requires `Authorization: Bearer <API_KEY>` header.

### Getting an API key

The user must generate the API key themselves in the SendFlow web UI:
1. Log into https://sendflow.pro/whats/sendapi
2. **Keys** tab → **Cadastrar**
3. Copy the generated key + their `userId` (also shown on the page)

**Saving the credential** (this user's convention — see `~/Documents/credentials/`):
```bash
mkdir -p ~/Documents/credentials/sendflow
cat > ~/Documents/credentials/sendflow/{account-name}.json <<EOF
{
  "apiKey": "...",
  "userId": "...",
  "baseUrl": "https://sendflow.pro/sendapi"
}
EOF
```

## Quick reference (44 endpoints, 9 groups)

| Resource | Count | Purpose |
|---|---|---|
| **Releases** (campanhas) | 9 | CRUD campaigns + analytics + leadscoring + redirect-link |
| **Release Groups** | 4 | CRUD groups inside a campaign |
| **Actions** | 9 | Bulk operations: create group, make-admin, send messages (text/image/video/audio), analyze-groups, find-participant |
| **Messages** | 4 | Direct 1-to-1 sends by accountId (text/image/video/audio) |
| **Accounts** | 8 | CRUD WhatsApp/Email accounts + connect/disconnect + QR code |
| **Message Templates** | 4 | CRUD message templates with intervals |
| **Block Numbers** | 2 | Anti-spam list (list + add) |
| **Verification** | 1 | Check if a number is blocked for a campaign |
| **Media** | 1 | Get Instagram post media-id (for repost flows) |

For the full endpoint list with request/response shapes, see **`reference.md`**. For the official Portuguese docs with real example responses, see **`docs-pt-br.md`**. For the OpenAPI 3.0 spec, see **`swagger.json`**.

## Common workflows

### 1. Send a text message to all groups of a campaign

```python
import requests, os, json

cred = json.load(open(os.path.expanduser("~/Documents/credentials/sendflow/main.json")))
headers = {"Authorization": f"Bearer {cred['apiKey']}"}

requests.post(
    "https://sendflow.pro/sendapi/actions/send-text-message",
    headers=headers,
    json={
        "accountId": "pwYE3dPNWV5XtrrPbba0",
        "releaseId": "De3MLuRlkjk8kGLp2cCnN",
        "messageText": "Olá, tudo bem?",
        "linkPreview": False,
        "options": {"shippingSpeed": "normal"},
    },
).raise_for_status()
```

### 2. Create a campaign + create a group + add participants

See **`examples.md`** for the full multi-step flow with error handling.

### 3. Schedule a message

Add `scheduled: true` and `scheduledTo: "2026-04-21T10:00:00.000Z"` (ISO 8601 UTC) to any send-message body.

## Rate limits (critical to respect — `403 "Limite de operações atingido!"` if exceeded)

| Operation | Limit |
|---|---|
| `POST /actions/send-{text,image,video,audio,}-message` | **10 req/s per `releaseId`** (shared across all four types + `send-message`) |
| `POST /accounts/create` | 1 req/s minimum |
| `POST /actions/group-create` | 1 req/s + 60s per `releaseId` |
| `GET /releases` | 5 minutes between calls |
| Most `PUT`/`DELETE` per-resource | 1 req/s + 60s per resource id |

When implementing clients, default to a polite **1s delay between requests** and exponential backoff on 403.

## Sending modes — `accountId` vs `accountIds`

Most send/action endpoints accept **either**:
- `accountId: "..."` (string) → use a single connected account
- `accountIds: ["...", "..."]` (array) → distribute the operation across multiple accounts (load balancing)

Pass one or the other, not both. The array form is preferred for high-volume releases.

## Shipping speeds (delay between sends)

For send-message endpoints, the `options.shippingSpeed` field controls delay between deliveries:

| Value | Delay between messages |
|---|---|
| `none` | no delay (immediate) |
| `fast` | 10–20s |
| `normal` | 40–60s |
| `slow` | 60–120s |
| `custom` | custom range via `options.customShippingSpeed: { min, max }` (in seconds) |

**Recommended:** `normal` for warmup / new accounts, `fast` only after accounts are warm.

## Files in this skill

- **`SKILL.md`** — this file (loaded into Claude's context when triggered)
- **`reference.md`** — full structured reference of all 44 endpoints with parameters, request/response schemas, and per-endpoint rate limits
- **`examples.md`** — copy-paste workflows: launch flow, message blast, leadscoring fetch, etc.
- **`docs-pt-br.md`** — verbatim Portuguese documentation extracted from `sendflow.pro/whats/sendapi` (includes real example responses)
- **`swagger.json`** — OpenAPI 3.0.0 spec (importable into Postman, Insomnia, OpenAPI Generator)
- **`clients/node.js`** — minimal Node.js client with auth + rate-limit helper
- **`clients/python.py`** — equivalent Python client

## Reading order when picking up a new task

1. Check **this file** for the resource group involved.
2. Read **`reference.md`** section for the specific endpoint (parameters + responses).
3. If you need a real response shape (the OpenAPI spec doesn't have schemas), check **`docs-pt-br.md`** — it has the actual JSON responses shown in the SendFlow UI.
4. Use **`clients/`** as a starting boilerplate.

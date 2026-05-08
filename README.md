<p align="center">
  <img src="assets/og-image.png" alt="SendFlow" width="500" />
</p>

# SendFlow API Skill

A [Claude Code](https://claude.com/claude-code) skill for the **SendFlow SendAPI** — the REST API for [SendFlow](https://sendflow.com.br) ("Sendi"), a Brazilian WhatsApp automation platform used by major Hotmart / V4 / Empiricus operators for launches, lead scoring, group management, and bulk messaging.

This skill bundles 44 endpoints across 9 resource groups (campaigns, groups, messages, accounts, templates, block lists, verification, media), in both English summary and verbatim Portuguese documentation extracted from `sendflow.pro/whats/sendapi`.

## What this skill gives Claude

When you mention `sendflow`, `sendapi`, `sendi`, or related terms in a Claude Code session, this skill auto-activates with:

- **44 endpoints documented** with parameters, request/response shapes, and per-endpoint rate limits
- **Real response examples** scraped from the official docs UI (the OpenAPI spec is missing response schemas — the official docs page has them)
- **OpenAPI 3.0 spec** (`swagger.json`) — importable into Postman/Insomnia
- **Helper clients** (Node.js, Python) with auth + rate-limit handling

## Install

### Option 1 — Plug-and-play `.zip`

1. Download the latest [release zip](https://github.com/kauaal12/sendflow-api-skill/releases/latest/download/sendflow-api-skill.zip)
2. Unzip into your Claude Code skills folder:

   ```bash
   mkdir -p ~/.claude/skills
   unzip ~/Downloads/sendflow-api-skill.zip -d ~/.claude/skills/
   # creates ~/.claude/skills/sendflow-sendapi/
   ```

3. Restart Claude Code (or run `/skills reload` if available).

### Option 2 — git clone

```bash
git clone https://github.com/kauaal12/sendflow-api-skill ~/.claude/skills/sendflow-sendapi
```

### Option 3 — npx skills

```bash
npx skills add kauaal12/sendflow-api-skill
```

## API key setup

You need a SendFlow API key to use the API. **Generate one in the SendFlow web UI** (Claude cannot generate it for you):

1. Log into https://sendflow.pro/whats/sendapi
2. Click the **Keys** tab → **Cadastrar**
3. Copy the generated key and your `userId` (also displayed on that page)
4. Save it where this skill (and other Claude skills on this user's machine) look:

   ```bash
   mkdir -p ~/Documents/credentials/sendflow
   cat > ~/Documents/credentials/sendflow/main.json <<EOF
   {
     "apiKey": "your_key_here",
     "userId": "your_user_id_here",
     "baseUrl": "https://sendflow.pro/sendapi"
   }
   EOF
   ```

## What's included

| File | Purpose |
|------|---------|
| `SKILL.md` | Main skill manifest + frontmatter + quick reference |
| `reference.md` | Full structured reference: 44 endpoints, parameters, request/response schemas |
| `examples.md` | Copy-paste workflows for common tasks |
| `docs-pt-br.md` | Verbatim Portuguese docs with real example responses |
| `swagger.json` | OpenAPI 3.0.0 spec |
| `clients/node.js` | Node.js client with auth + rate-limit helper |
| `clients/python.py` | Python equivalent |

## Endpoint coverage

| Resource group | Endpoints |
|---|---|
| Releases (campaigns) | 9 |
| Release Groups | 4 |
| Actions | 9 |
| Messages | 4 |
| Accounts | 8 |
| Message Templates | 4 |
| Block Numbers | 2 |
| Verification | 1 |
| Media | 1 |
| **Total** | **44** |

## Rate limits

The SendAPI is aggressively rate-limited. Key limits:

- **Send messages:** 10 req/s per `releaseId` (shared across text/image/video/audio)
- **Account create:** 1s minimum between calls
- **Group create:** 1s minimum + 60s per `releaseId`
- **List releases:** 5 minutes minimum between calls
- Most write operations: 1s minimum + 60s per resource id

Exceeding any of these returns `403 "Limite de operações atingido!"`. The provided clients implement polite defaults; build your own wrappers around them.

## Disclaimer

This is an **unofficial** community skill, not affiliated with or endorsed by SendFlow. The documentation here was extracted from the public `/sendapi/swagger.json` endpoint and the publicly accessible API documentation at `sendflow.pro/whats/sendapi` (login-gated UI but the underlying spec is open).

For official support, contact SendFlow at `equipe@sendflow.pro` or via the WhatsApp channels listed at https://sendflow.com.br.

## License

[MIT](LICENSE) — fork it, adapt it, ship it.

## Contributing

Issues and PRs welcome. If you find a divergence between this doc and the live API behavior (rate limit numbers off, undocumented field, broken example), open an issue with a request/response sample.

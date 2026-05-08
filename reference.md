# SendFlow SendAPI — Endpoint Reference

**Spec version:** 1.0.0 (OpenAPI 3.0.0)
**Base URL:** `https://sendflow.pro/sendapi`
**Auth:** `Authorization: Bearer <API_KEY>` (required globally)

## Table of contents

- [SendAPI - Accounts](#sendapi---accounts) — 8 endpoints
- [SendAPI - Actions](#sendapi---actions) — 9 endpoints
- [SendAPI - Block Numbers](#sendapi---block-numbers) — 2 endpoints
- [SendAPI - Media](#sendapi---media) — 1 endpoints
- [SendAPI - Message Templates](#sendapi---message-templates) — 4 endpoints
- [SendAPI - Messages](#sendapi---messages) — 4 endpoints
- [SendAPI - Release Groups](#sendapi---release-groups) — 4 endpoints
- [SendAPI - Releases](#sendapi---releases) — 10 endpoints
- [SendAPI - Releases (em desenvolvimento)](#sendapi---releases-em-desenvolvimento) — 1 endpoints
- [SendAPI - Verification](#sendapi---verification) — 1 endpoints


## SendAPI - Accounts


### `POST` `/sendapi/accounts/create`

*Criar uma nova conta*

> **Rate limit:** intervalo mínimo de **1 segundo** entre criações.
> Ao exceder, a API responde `403` com `Limite de operações atingido!`.

**Request body** (`application/json`):
- `data` (object) — Dados da conta
  - `name` (string) — Nome da conta *(ex: `"testessss"`)*
  - `type` (string) — Tipo da conta *(ex: `"whatsapp"`)*
- `projectId` (string) — ID do projeto *(ex: `"1234567890"`)*

**Responses:**
- `200` — Conta criada com sucesso
- `400` — Erro ao criar a conta
- `401` — Erro de autenticação
- `403` — Limite de operações atingido (rate limit) ou acesso negado

---

### `GET` `/sendapi/accounts`

*Obter contas de um usuário*

> **Rate limit:** intervalo mínimo de **60 segundos** entre listagens.
> Ao exceder, a API responde `403` com `Limite de operações atingido!`.

**Responses:**
- `200` — Contas obtidas com sucesso
- `400` — Erro ao obter contas
- `401` — Erro de autenticação
- `403` — Limite de operações atingido (rate limit) ou acesso negado

---

### `PUT` `/sendapi/accounts/{accountId}`

*Atualizar conta*

> **Rate limit (dois controles):** intervalo mínimo de **1 segundo** entre atualizações e de **60 segundos**
> por `accountId`. Ao exceder, a API responde `403` com `Limite de operações atingido!`.

**Parameters:**
- `accountId` (path) **required** — ID da conta

**Request body** (`application/json`):
- `data` (object) — Dados da conta
  - `name` (string) — Nome da conta *(ex: `"testessss"`)*
  - `type` (string) — Tipo da conta *(ex: `"whatsapp"`)*
- `projectId` (string) — ID do projeto *(ex: `"1234567890"`)*

**Responses:**
- `200` — Conta atualizada com sucesso
- `400` — Erro ao atualizar a conta
- `401` — Erro de autenticação
- `403` — Limite de operações atingido (rate limit) ou acesso negado

---

### `DELETE` `/sendapi/accounts/{accountId}`

*Remover conta*

> **Rate limit (dois controles):** intervalo mínimo de **1 segundo** entre exclusões e de **60 segundos**
> por `accountId`. Ao exceder, a API responde `403` com `Limite de operações atingido!`.

**Parameters:**
- `accountId` (path) **required** — ID da conta

**Responses:**
- `204` — Conta removida com sucesso
- `400` — Erro ao obter contas
- `401` — Erro de autenticação
- `403` — Limite de operações atingido (rate limit) ou acesso negado

---

### `POST` `/sendapi/accounts/connect-account/{accountId}`

*Conectar conta*

> **Rate limit (dois controles):** intervalo mínimo de **1 segundo** entre chamadas e de **60 segundos**
> por `accountId`. Ao exceder, a API responde `403` com `Limite de operações atingido!`.

**Parameters:**
- `accountId` (path) **required** — ID da conta

**Responses:**
- `200` — Conta conectada com sucesso
- `400` — Erro ao conectar conta
- `401` — Não autenticado ou não autorizado
- `403` — Limite de operações atingido (rate limit) ou acesso negado

---

### `POST` `/sendapi/accounts/disconnect-account/{accountId}`

*Desconectar conta*

> **Rate limit (dois controles):** intervalo mínimo de **1 segundo** entre chamadas e de **60 segundos**
> por `accountId`. Ao exceder, a API responde `403` com `Limite de operações atingido!`.

**Parameters:**
- `accountId` (path) **required** — ID da conta

**Responses:**
- `204` — Conta desconectada com sucesso
- `400` — Erro ao desconectar conta
- `401` — Não autenticado ou não autorizado
- `403` — Limite de operações atingido (rate limit) ou acesso negado

---

### `GET` `/sendapi/accounts/{accountId}/qrcode`

*Obter QR code da conta*

> **Rate limit (dois controles):** intervalo mínimo de **1 segundo** entre consultas e de **60 segundos**
> por `accountId` (compartilhado com `/qrcode-image`). Ao exceder, `403` com `Limite de operações atingido!`.

**Parameters:**
- `accountId` (path) **required** — ID da conta

**Responses:**
- `200` — QR code obtido com sucesso
- `400` — Erro ao obter QR code
- `401` — Não autenticado ou não autorizado
- `403` — Limite de operações atingido (rate limit) ou acesso negado

---

### `GET` `/sendapi/accounts/{accountId}/qrcode-image`

*Obter imagem do QR code da conta*

> **Rate limit:** mesmo limite de `/qrcode` (**1s** entre consultas + **60s** por `accountId`).
> Ao exceder, `403` com `Limite de operações atingido!`.

**Parameters:**
- `accountId` (path) **required** — ID da conta

**Responses:**
- `200` — Imagem do QR code obtida com sucesso
- `400` — Erro ao obter imagem do QR code
- `401` — Não autenticado ou não autorizado
- `403` — Limite de operações atingido (rate limit) ou acesso negado

---

## SendAPI - Actions


### `POST` `/sendapi/actions/group-create`

*Criar um grupo*

> **Rate limit (dois controles):** intervalo mínimo de **1 segundo** entre chamadas e de **60 segundos**
> por `releaseId`. Ao exceder, `403` com `Limite de operações atingido!`.

**Request body** (`application/json`):
- `accountId` (string) — ID da conta *(ex: `"7LLztsEGLPNAAAAAAAAXfc52"`)*
- `releaseId` (string) — ID da campanha *(ex: `"7LLztsEGLPNBBBBBBdtItXfc52"`)*
- `payload` (object) — 
  - `name` (string) — Nome do grupo *(ex: `"grupo teste 123"`)*
  - `participants` (array<string>) — Lista de participantes
  - `standardization` (boolean) — Se deve ser padronizado *(ex: `false`)*

**Responses:**
- `201` — Ação criada com sucesso
- `400` — Erro ao criar a ação
- `401` — Erro de autenticação
- `403` — Limite de operações atingido (rate limit), acesso negado ou recurso indisponível
- `404` — Ação não encontrada
- `500` — Erro interno do servidor

---

### `POST` `/sendapi/actions/make-group-admin`

*Tornar um usuário admin de um grupo ou de todos os grupos da campanha*

> **Rate limit (dois controles):** intervalo mínimo de **1 segundo** entre chamadas e de **60 segundos**
> por `releaseId`. Ao exceder, `403` com `Limite de operações atingido!`.

**Request body** (`application/json`):
- `accountId` (string) — ID da conta *(ex: `"7LLztsEGLPNAAAAAAAAXfc52"`)*
- `releaseId` (string) — ID da campanha *(ex: `"7LLztsEGLPNBBBBBBdtItXfc52"`)*
- `participants` (array<object>) — Lista de participantes
  - `number` (string) — Número do participante *(ex: `"557581133148"`)*
  - `name` (string) — Nome do participante *(ex: `"João"`)*
- `chooseSpecificGroups` (boolean) — Se deve escolher grupos específicos *(ex: `true`)*
- `groupIds` (array<string>) — Lista de GIDs de grupos, sem o @g.us

**Responses:**
- `201` — Ação criada com sucesso
- `400` — Erro ao criar a ação
- `401` — Erro de autenticação
- `403` — Limite de operações atingido (rate limit), acesso negado ou recurso indisponível
- `404` — Ação não encontrada
- `500` — Erro interno do servidor

---

### `POST` `/sendapi/actions/send-text-message`

*Enviar mensagem de texto*

> **Rate limit:** até **10** requisições por segundo por `releaseId` (janela móvel de 1 segundo), compartilhado entre
> `send-text-message`, `send-image-message`, `send-video-message`, `send-audio-message` e `send-message`.
> Ao exceder, `403` com `Limite de operações atingido!`.

**Request body** (`application/json`):
- `accountId` (string) — ID da conta (opcional se accountIds for fornecido) *(ex: `"pwYE3dPNWV5XtrrPbba0"`)*
- `accountIds` (array<string>) — IDs das contas (opcional se accountId for fornecido). Permite enviar para múltiplas contas
- `releaseId` (string) — ID da campanha *(ex: `"De3MLuRlkjk8kGLp2cCnN"`)*
- `messageText` (string) — Texto a ser enviado *(ex: `"Olá, tudo bem?"`)*
- `linkPreview` (boolean) — Se deve gerar preview do link contido no texto da mensagem *(ex: `true`)*
- `scheduled` (boolean) — Se a mensagem deve ser agendada *(ex: `true`)*
- `scheduledTo` (string) — Data de agendamento (formato ISO 8601) *(ex: `"2025-04-21T10:00:00.000Z"`)*
- `chooseSpecificGroups` (boolean) — Se deve escolher grupos específicos *(ex: `true`)*
- `groupIds` (array<string>) — Lista de GIDs de grupos, sem o @g.us
- `options` (object) — 
  - `shippingSpeed` (string) — Velocidade de entrega da mensagem (none, custom, fast, normal, slow). Opções:
  - none: sem atraso (envio imediato)
  - custom: tempo personalizado definido pelo usuário
  - fast: rápido (Entre 10 e 20 segundos)
  - normal: normal (Entre 40 e 60 segundos)
  - slow: lento (Entre 60 e 120 segundos)
 *(ex: `"fast"`)*
  - `customShippingSpeed` (object) — Tempo personalizado para entrega da mensagem (intervalo mínimo e máximo em segundos)
    - `min` (integer) — Valor mínimo do tempo personalizado para entrega da mensagem *(ex: `10`)*
    - `max` (integer) — Valor máximo do tempo personalizado para entrega da mensagem *(ex: `20`)*

**Responses:**
- `201` — Ação criada com sucesso
- `400` — Erro ao criar a ação
- `401` — Erro de autenticação
- `403` — Limite de operações atingido (rate limit) ou acesso negado

---

### `POST` `/sendapi/actions/send-image-message`

*Enviar mensagem com imagem*

> **Rate limit:** até **10** requisições por segundo por `releaseId` (janela móvel de 1 segundo), compartilhado entre
> `send-text-message`, `send-image-message`, `send-video-message`, `send-audio-message` e `send-message`.
> Ao exceder, `403` com `Limite de operações atingido!`.

**Request body** (`application/json`):
- `accountId` (string) — ID da conta (opcional se accountIds for fornecido) *(ex: `"pwYE3dPNWV5XtrrPbba0"`)*
- `accountIds` (array<string>) — IDs das contas (opcional se accountId for fornecido). Permite enviar para múltiplas contas
- `releaseId` (string) — ID da campanha *(ex: `"De3MLuRlkjk8kGLp2cCnN"`)*
- `caption` (string) — Legenda da imagem *(ex: `"Imagem de teste"`)*
- `url` (string) — URL da Imagem a ser Enviada *(ex: `"https://www.google.com.br/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png"`)*
- `scheduledTo` (string) — Data de agendamento (formato ISO 8601)
- `chooseSpecificGroups` (boolean) — Se deve escolher grupos específicos *(ex: `true`)*
- `groupIds` (array<string>) — Lista de GIDs de grupos, sem o @g.us
- `options` (object) — 
  - `shippingSpeed` (string) — Velocidade de entrega da mensagem (none, custom, fast, normal, slow). Opções:
  - none: sem atraso (envio imediato)
  - custom: tempo personalizado definido pelo usuário
  - fast: rápido (Entre 10 e 20 segundos)
  - normal: normal (Entre 40 e 60 segundos)
  - slow: lento (Entre 60 e 120 segundos)
 *(ex: `"fast"`)*
  - `customShippingSpeed` (object) — Tempo personalizado para entrega da mensagem (intervalo mínimo e máximo em segundos)
    - `min` (integer) — Valor mínimo do tempo personalizado para entrega da mensagem *(ex: `10`)*
    - `max` (integer) — Valor máximo do tempo personalizado para entrega da mensagem *(ex: `20`)*

**Responses:**
- `201` — Ação criada com sucesso
- `400` — Erro ao criar a ação
- `401` — Erro de autenticação
- `403` — Limite de operações atingido (rate limit) ou acesso negado

---

### `POST` `/sendapi/actions/send-video-message`

*Enviar mensagem com vídeo*

> **Rate limit:** até **10** requisições por segundo por `releaseId` (janela móvel de 1 segundo), compartilhado entre
> `send-text-message`, `send-image-message`, `send-video-message`, `send-audio-message` e `send-message`.
> Ao exceder, `403` com `Limite de operações atingido!`.

**Request body** (`application/json`):
- `accountId` (string) — ID da conta (opcional se accountIds for fornecido) *(ex: `"pwYE3dPNWV5XtrrPbba0"`)*
- `accountIds` (array<string>) — IDs das contas (opcional se accountId for fornecido). Permite enviar para múltiplas contas
- `releaseId` (string) — ID da campanha *(ex: `"De3MLuRlkjk8kGLp2cCnN"`)*
- `caption` (string) — Legenda do vídeo *(ex: `"Video de teste"`)*
- `url` (string) — URL do vídeo a ser enviado *(ex: `"https://video.com/video.mp4"`)*
- `scheduledTo` (string) — Data de agendamento (formato ISO 8601)
- `chooseSpecificGroups` (boolean) — Se deve escolher grupos específicos *(ex: `true`)*
- `groupIds` (array<string>) — Lista de GIDs de grupos, sem o @g.us
- `options` (object) — 
  - `shippingSpeed` (string) — Velocidade de entrega da mensagem (none, custom, fast, normal, slow). Opções:
  - none: sem atraso (envio imediato)
  - custom: tempo personalizado definido pelo usuário
  - fast: rápido (Entre 10 e 20 segundos)
  - normal: normal (Entre 40 e 60 segundos)
  - slow: lento (Entre 60 e 120 segundos)
 *(ex: `"fast"`)*
  - `customShippingSpeed` (object) — Tempo personalizado para entrega da mensagem (intervalo mínimo e máximo em segundos)
    - `min` (integer) — Valor mínimo do tempo personalizado para entrega da mensagem *(ex: `10`)*
    - `max` (integer) — Valor máximo do tempo personalizado para entrega da mensagem *(ex: `20`)*

**Responses:**
- `201` — Ação criada com sucesso
- `400` — Erro ao criar a ação
- `401` — Erro de autenticação
- `403` — Limite de operações atingido (rate limit) ou acesso negado

---

### `POST` `/sendapi/actions/send-audio-message`

*Enviar mensagem com áudio*

> **Rate limit:** até **10** requisições por segundo por `releaseId` (janela móvel de 1 segundo), compartilhado entre
> `send-text-message`, `send-image-message`, `send-video-message`, `send-audio-message` e `send-message`.
> Ao exceder, `403` com `Limite de operações atingido!`.

**Request body** (`application/json`):
- `accountId` (string) — ID da conta (opcional se accountIds for fornecido) *(ex: `"pwYE3dPNWV5XtrrPbba0"`)*
- `accountIds` (array<string>) — IDs das contas (opcional se accountId for fornecido). Permite enviar para múltiplas contas
- `releaseId` (string) — ID da campanha *(ex: `"De3MLuRlkjk8kGLp2cCnN"`)*
- `caption` (string) — Legenda do áudio *(ex: `"Audio de teste"`)*
- `url` (string) — URL do áudio a ser enviado *(ex: `"https://audio.com/audio.mp3"`)*
- `ptt` (boolean) — Se true, envia como gravação (push-to-talk). Se false ou não informado, envia como áudio normal *(ex: `true`)*
- `scheduledTo` (string) — Data de agendamento (formato ISO 8601)
- `chooseSpecificGroups` (boolean) — Se deve escolher grupos específicos *(ex: `true`)*
- `groupIds` (array<string>) — Lista de GIDs de grupos, sem o @g.us
- `options` (object) — 
  - `shippingSpeed` (string) — Velocidade de entrega da mensagem (none, custom, fast, normal, slow). Opções:
  - none: sem atraso (envio imediato)
  - custom: tempo personalizado definido pelo usuário
  - fast: rápido (Entre 10 e 20 segundos)
  - normal: normal (Entre 40 e 60 segundos)
  - slow: lento (Entre 60 e 120 segundos)
 *(ex: `"fast"`)*
  - `customShippingSpeed` (object) — Tempo personalizado para entrega da mensagem (intervalo mínimo e máximo em segundos)
    - `min` (integer) — Valor mínimo do tempo personalizado para entrega da mensagem *(ex: `10`)*
    - `max` (integer) — Valor máximo do tempo personalizado para entrega da mensagem *(ex: `20`)*

**Responses:**
- `201` — Ação criada com sucesso
- `400` — Erro ao criar a ação
- `401` — Erro de autenticação
- `403` — Limite de operações atingido (rate limit) ou acesso negado

---

### `POST` `/sendapi/actions/send-message`

*Enviar mensagem de qualquer tipo (texto, imagem, áudio, vídeo)*

> **Rate limit:** até **10** requisições por segundo por `releaseId` (janela móvel de 1 segundo), compartilhado entre
> `send-text-message`, `send-image-message`, `send-video-message`, `send-audio-message` e `send-message`.
> Ao exceder, `403` com `Limite de operações atingido!`.

**Request body** (`application/json`):
- `accountId` (string) — ID da conta (opcional se accountIds for fornecido) *(ex: `"pwYE3dPNWV5XtrrPbba0"`)*
- `accountIds` (array<string>) — IDs das contas (opcional se accountId for fornecido). Permite enviar para múltiplas contas
- `releaseId` (string) — ID da campanha *(ex: `"De3MLuRlkjk8kGLp2cCnN"`)*
- `type` (string) — Tipo de mensagem (extendedTextMessage, imageMessage, videoMessage, audioMessage) *(ex: `"extendedTextMessage"`)*
- `text` (string) — Texto da mensagem (para mensagens de texto) *(ex: `"Olá, tudo bem?"`)*
- `linkPreview` (boolean) — Se deve gerar preview do link contido no texto da mensagem (apenas para extendedTextMessage) *(ex: `true`)*
- `caption` (string) — Legenda (para imagens, vídeos ou áudios) *(ex: `"Minha imagem"`)*
- `url` (string) — URL do arquivo (para imagens, vídeos ou áudios) *(ex: `"https://exemplo.com/imagem.jpg"`)*
- `ptt` (boolean) — Se true, envia como gravação (push-to-talk). Apenas para audioMessage. Se false ou não informado, envia como áudio normal *(ex: `true`)*
- `scheduledTo` (string) — Data de agendamento (formato ISO 8601)
- `chooseSpecificGroups` (boolean) — Se deve escolher grupos específicos *(ex: `true`)*
- `groupIds` (array<string>) — Lista de GIDs de grupos, sem o @g.us
- `options` (object) — 
  - `ephemeralExpiration` (integer) — Tempo para expiração da mensagem *(ex: `-1`)*
  - `mentionAllParticipants` (boolean) — Mencionar todos os participantes *(ex: `false`)*
  - `shippingSpeed` (string) — Velocidade de entrega da mensagem (none, custom, fast, normal, slow). Opções:
  - none: sem atraso (envio imediato)
  - custom: tempo personalizado definido pelo usuário
  - fast: rápido (Entre 10 e 20 segundos)
  - normal: normal (Entre 40 e 60 segundos)
  - slow: lento (Entre 60 e 120 segundos)
 *(ex: `"fast"`)*
  - `customShippingSpeed` (object) — Tempo personalizado para entrega da mensagem (intervalo mínimo e máximo em segundos)
    - `min` (integer) — Valor mínimo do tempo personalizado para entrega da mensagem *(ex: `10`)*
    - `max` (integer) — Valor máximo do tempo personalizado para entrega da mensagem *(ex: `20`)*

**Responses:**
- `201` — Ação criada com sucesso
- `400` — Erro ao criar a ação
- `401` — Erro de autenticação
- `403` — Limite de operações atingido (rate limit) ou acesso negado

---

### `POST` `/sendapi/actions/analyze-groups`

*Criar ações de refresh de grupos para contas específicas*

> **Rate limit:** intervalo mínimo de **60 segundos** entre chamadas (`actions-analyze-groups`).
> Ao exceder, `403` com `Limite de operações atingido!`.

**Request body** (`application/json`):
- `accountIds` (array<string>) — IDs das contas. Se não fornecido, usa todas as contas autenticadas do usuário
- `to` (string) — Padrão: anti-spam *(ex: `"anti-spam"`)*

**Responses:**
- `200` — Ações criadas com sucesso
- `400` — Erro ao criar as ações
- `401` — Erro de autenticação
- `403` — Limite de operações atingido (rate limit) ou acesso negado

---

### `POST` `/sendapi/actions/find-participant`

*Buscar se um número está em algum grupo das campanhas da conta (todas as releases com grupos)*

> **Rate limit:** intervalo mínimo de **1 segundo** entre buscas (`actions-find-participant`).
> por `accountId`. Ao exceder, `403` com `Limite de operações atingido!`.

**Request body** (`application/json`):
- `accountId` (string) **required** — ID da conta WhatsApp *(ex: `"pwYE3dPNWV5XtaaaPbba0"`)*
- `phoneNumber` (string) **required** — Número de telefone a ser buscado *(ex: `"5511987654321"`)*
- `timeout` (number) — Timeout em milissegundos (padrão: 60000) *(ex: `60000`)*

**Responses:**
- `200` — Resultado da busca (mesmo formato retornado pelo connector)
- `400` — Erro ao buscar participante
- `401` — Erro de autenticação
- `403` — Limite de operações atingido (rate limit) ou acesso negado

---

## SendAPI - Block Numbers


### `GET` `/sendapi/block-numbers`

*Obter números bloqueados do usuário autenticado*

> **Rate limit:** intervalo mínimo de **60 segundos** entre uma requisição e a próxima.
> Ao exceder, a API responde `403` com a mensagem
> `Limite de operações atingido!`.

**Responses:**
- `200` — Números bloqueados obtidos com sucesso
- `400` — Erro ao obter os números bloqueados
- `401` — Não autenticado ou chave inválida
- `403` — Limite de operações atingido (rate limit) ou acesso negado

---

### `POST` `/sendapi/block-numbers`

*Bloquear um número*

> **Rate limit:** intervalo mínimo de **1 segundo** entre uma requisição e a próxima. Ao exceder, a API responde `403` com a mensagem
> `Limite de operações atingido!`.

**Request body** (`application/json`):
- `number` (string) — Número de telefone a ser bloqueado *(ex: `"5511987654321"`)*
- `name` (string) — Nome do número a ser bloqueado *(ex: `"João"`)*

**Responses:**
- `200` — Número bloqueado com sucesso
- `400` — Erro ao bloquear o número
- `401` — Não autenticado ou chave inválida
- `403` — Limite de operações atingido (rate limit) ou acesso negado

---

## SendAPI - Media


### `GET` `/sendapi/generate-media-id`

*Obter media id de um post no instagram*

> **Rate limit:** intervalo mínimo de **1 segundo** entre requisições (`media-generate-media-id` por usuário da API).
> Ao exceder, a API responde `403` com `Limite de operações atingido!`.

**Parameters:**
- `mediaId` (query) **required** — ID do post no instagram

**Responses:**
- `200` — Obtido com sucesso
- `400` — Erro ao obter media id
- `401` — Não autenticado ou chave inválida
- `403` — Limite de operações atingido (rate limit) ou acesso negado

---

## SendAPI - Message Templates


### `GET` `/sendapi/message-templates`

*Buscar todos os templates de mensagem do usuário*

> **Rate limit:** intervalo mínimo de **60 segundos** entre requisições de listagem.
> Ao exceder, a API responde `403` com `Limite de operações atingido!`.

**Responses:**
- `200` — Lista de templates de mensagem do usuário
- `400` — Erro ao buscar templates
- `401` — Erro de autenticação
- `403` — Limite de operações atingido (rate limit) ou acesso negado

---

### `POST` `/sendapi/message-templates`

*Criar um novo template de mensagem*

> **Rate limit:** intervalo mínimo de **1 segundo** entre criações.
> Ao exceder, a API responde `403` com `Limite de operações atingido!`.

**Request body** (`application/json`):
- `title` (string) **required** — Título do template *(ex: `"Template de boas-vindas"`)*
- `template` (array<object>) **required** — Array de mensagens do template. Pode conter múltiplos tipos de mensagens (texto, imagem, vídeo, áudio, etc.) e quantas mensagens forem necessárias
- `folderId` (string) — ID da pasta do template *(ex: `"abc123"`)*
- `intervalRangeType` (string) — Tipo de intervalo entre mensagens *(ex: `"none"`)*
- `intervalRange` (array<number>) — Intervalo entre mensagens [min, max]
- `archived` (boolean) — Se o template está arquivado *(ex: `false`)*

**Responses:**
- `201` — Template criado com sucesso
- `400` — Erro ao criar template
- `401` — Erro de autenticação
- `403` — Limite de operações atingido (rate limit) ou acesso negado

---

### `PUT` `/sendapi/message-templates/{templateId}`

*Atualizar um template de mensagem*

> **Rate limit (dois controles):** intervalo mínimo de **1 segundo** entre atualizações e de **60 segundos**
> entre alterações no mesmo `templateId`. Ao exceder, a API responde `403` com `Limite de operações atingido!`.

**Parameters:**
- `templateId` (path) **required** — ID do template de mensagem

**Request body** (`application/json`):
- `title` (string) — Título do template *(ex: `"Template de boas-vindas"`)*
- `template` (array<object>) — Array de mensagens do template
- `folderId` (string) — ID da pasta do template *(ex: `"abc123"`)*
- `intervalRangeType` (string) — Tipo de intervalo entre mensagens *(ex: `"none"`)*
- `intervalRange` (array<number>) — Intervalo entre mensagens [min, max]
- `archived` (boolean) — Se o template está arquivado *(ex: `false`)*
- `position` (number) — Posição do template *(ex: `0`)*

**Responses:**
- `200` — Template atualizado com sucesso
- `400` — Erro ao atualizar template
- `401` — Erro de autenticação
- `403` — Limite de operações atingido (rate limit) ou acesso negado
- `404` — Template não encontrado

---

### `DELETE` `/sendapi/message-templates/{templateId}`

*Deletar um template de mensagem*

> **Rate limit (dois controles):** intervalo mínimo de **1 segundo** entre exclusões e de **60 segundos**
> por `templateId`. Ao exceder, a API responde `403` com `Limite de operações atingido!`.

**Parameters:**
- `templateId` (path) **required** — ID do template de mensagem

**Responses:**
- `204` — Template deletado com sucesso
- `400` — Erro ao deletar template
- `401` — Erro de autenticação
- `403` — Limite de operações atingido (rate limit) ou acesso negado
- `404` — Template não encontrado

---

## SendAPI - Messages


### `POST` `/sendapi/send-text-message/{accountId}`

*Enviar mensagem de texto*

> **Rate limit:** intervalo mínimo de **200 milissegundos** entre envios (`messages-send` por usuário da API).
> Ao exceder, a API responde `403` com `Limite de operações atingido!`.

**Parameters:**
- `accountId` (path) **required** — ID da conta

**Request body** (`application/json`):
- `text` (string) — Texto da mensagem *(ex: `"12345"`)*
- `phoneNumber` (string) — Número de telefone a ser enviado a mensagem *(ex: `"5511987654321"`)*

**Responses:**
- `200` — Mensagem enviada com sucesso
- `400` — Erro ao enviar a mensagem
- `401` — Erro de autenticação
- `403` — Limite de operações atingido (rate limit) ou acesso negado

---

### `POST` `/sendapi/send-image-message/{accountId}`

*Enviar mensagem de imagem*

> **Rate limit:** intervalo mínimo de **200 milissegundos** entre envios (`messages-send` por usuário da API).
> Ao exceder, a API responde `403` com `Limite de operações atingido!`.

**Parameters:**
- `accountId` (path) **required** — ID da conta

**Request body** (`application/json`):
- `url` (string) — URL da imagem *(ex: `"https://img.com/image.jpg"`)*
- `caption` (string) — Legenda da imagem *(ex: `"Texto da legenda"`)*

**Responses:**
- `200` — Mensagem enviada com sucesso
- `400` — Erro ao enviar a mensagem
- `401` — Erro de autenticação
- `403` — Limite de operações atingido (rate limit) ou acesso negado

---

### `POST` `/sendapi/send-video-message/{accountId}`

*Enviar mensagem de video*

> **Rate limit:** intervalo mínimo de **200 milissegundos** entre envios (`messages-send` por usuário da API).
> Ao exceder, a API responde `403` com `Limite de operações atingido!`.

**Parameters:**
- `accountId` (path) **required** — ID da conta

**Request body** (`application/json`):
- `url` (string) — URL do video *(ex: `"https://img.com/image.jpg"`)*
- `caption` (string) — Legenda do video *(ex: `"Texto da legenda"`)*

**Responses:**
- `200` — Mensagem enviada com sucesso
- `400` — Erro ao enviar a mensagem
- `401` — Erro de autenticação
- `403` — Limite de operações atingido (rate limit) ou acesso negado

---

### `POST` `/sendapi/send-audio-message/{accountId}`

*Enviar mensagem de audio*

> **Rate limit:** intervalo mínimo de **200 milissegundos** entre envios (`messages-send` por usuário da API).
> Ao exceder, a API responde `403` com `Limite de operações atingido!`.

**Parameters:**
- `accountId` (path) **required** — ID da conta

**Request body** (`application/json`):
- `url` (string) — URL do audio *(ex: `"https://img.com/image.jpg"`)*
- `caption` (string) — Legenda do audio *(ex: `"Texto da legenda"`)*
- `ptt` (boolean) — Se true, envia como gravação (push-to-talk). Se false ou não informado, envia como áudio normal *(ex: `true`)*

**Responses:**
- `200` — Mensagem enviada com sucesso
- `400` — Erro ao enviar a mensagem
- `401` — Erro de autenticação
- `403` — Limite de operações atingido (rate limit) ou acesso negado

---

## SendAPI - Release Groups


### `POST` `/sendapi/release-groups`

*Criar um grupo na campanha*

> **Rate limit:** intervalo mínimo de **1 segundo** entre uma requisição e a próxima.
> Ao exceder, a API responde `403` com a mensagem
> `Limite de operações atingido!`.

**Request body** (`application/json`):
- `gid` (string) — ID do grupo *(ex: `"120363292004848696@g.us"`)*
- `releaseId` (string) — ID da campanha *(ex: `"biuumwkQqFtMcOCbGEgk"`)*
- `count` (number) — Contagem *(ex: `1`)*
- `name` (string) — Nome do grupo *(ex: `"Teste Send #1"`)*
- `inviteCode` (string) — Código de convite *(ex: `"GGbs7JdTIZd6IOYSfETof1"`)*
- `full` (boolean) — Indica se está cheio *(ex: `false`)*
- `type` (string) — Tipo de grupo *(ex: `"group"`)*

**Responses:**
- `201` — Grupo criado com sucesso
- `400` — Erro ao criar o grupo
- `401` — Não autenticado ou chave inválida
- `403` — Limite de operações atingido (rate limit) ou acesso negado

---

### `GET` `/sendapi/release-groups/{releaseGroupId}`

*Obter um grupo na campanha*

> **Rate limit (dois controles):**
> - intervalo mínimo de **1 segundo** entre quaisquer requisições GET neste recurso;
> - intervalo mínimo de **60 segundos** entre requisições para o **mesmo** `releaseGroupId`.
> Ao exceder, a API responde `403` com `Limite de operações atingido!`.

**Parameters:**
- `releaseGroupId` (path) **required** — ID do grupo na campanha

**Responses:**
- `200` — Grupo obtido com sucesso
- `401` — Não autenticado ou chave inválida
- `403` — Limite de operações atingido (rate limit) ou acesso negado
- `404` — Grupo não encontrado

---

### `PUT` `/sendapi/release-groups/{releaseGroupId}`

*Atualizar um grupo na campanha*

> **Rate limit (dois controles):**
> - intervalo mínimo de **1 segundo** entre quaisquer requisições PUT neste recurso;
> - intervalo mínimo de **60 segundos** entre atualizações no **mesmo** `releaseGroupId`.
> Ao exceder, a API responde `403` com `Limite de operações atingido!`.

**Parameters:**
- `releaseGroupId` (path) **required** — ID do grupo na campanha

**Request body** (`application/json`):
- `count` (integer) — Contagem *(ex: `1`)*
- `full` (boolean) — Indica se está cheio *(ex: `false`)*
- `name` (string) — Nome do grupo *(ex: `"Teste Send #1"`)*

**Responses:**
- `200` — Grupo atualizado com sucesso
- `400` — Erro ao atualizar o grupo
- `401` — Não autenticado ou chave inválida
- `403` — Limite de operações atingido (rate limit) ou acesso negado
- `404` — Grupo não encontrado

---

### `DELETE` `/sendapi/release-groups/{releaseGroupId}`

*Excluir um grupo da campanha*

> **Rate limit (dois controles):**
> - intervalo mínimo de **1 segundo** entre quaisquer requisições DELETE neste recurso;
> - intervalo mínimo de **60 segundos** entre exclusões do **mesmo** `releaseGroupId`.
> Ao exceder, a API responde `403` com `Limite de operações atingido!`.

**Parameters:**
- `releaseGroupId` (path) **required** — ID do grupo na campanha

**Responses:**
- `204` — Grupo deletado com sucesso
- `400` — Erro ao deletar o grupo
- `401` — Não autenticado ou chave inválida
- `403` — Limite de operações atingido (rate limit) ou acesso negado
- `404` — Grupo não encontrado

---

## SendAPI - Releases


### `GET` `/sendapi/releases`

*Buscar todas as campanhas do usuário*

> **Rate limit:** intervalo mínimo de **5 minutos** entre uma requisição e a próxima.
> Ao exceder, a API responde `403` com `Limite de operações atingido!`.

**Responses:**
- `200` — Lista de campanhas do usuário
- `400` — Erro ao buscar campanhas
- `401` — Não autenticado ou chave inválida
- `403` — Limite de operações atingido (rate limit) ou acesso negado
- `404` — Nenhuma campanha encontrada

---

### `POST` `/sendapi/releases`

*Criar uma nova campanha*

> **Rate limit:** intervalo mínimo de **1 segundo** entre uma requisição e a próxima.
> Ao exceder, a API responde `403` com `Limite de operações atingido!`.

**Request body** (`application/json`):
- `name` (string) — Nome da campanha *(ex: `"campanha 03"`)*
- `type` (string) —  *(ex: `"WhatsRelease"`)*
- `projectId` (string) — ID do projeto *(ex: `"1234567890"`)*

**Responses:**
- `201` — Campanha criada com sucesso
- `400` — Erro ao criar campanha ou dados inválidos
- `401` — Não autenticado ou chave inválida
- `403` — Limite de operações atingido (rate limit) ou acesso negado

---

### `GET` `/sendapi/releases/{releaseId}`

*Buscar uma única campanha*

> **Rate limit (dois controles):**
> - intervalo mínimo de **1 segundo** entre quaisquer requisições GET que consultem campanha por `releaseId` (inclui grupos, analytics, leadscoring, etc.);
> - intervalo mínimo de **60 segundos** entre requisições para o **mesmo** `releaseId`.
> Ao exceder, a API responde `403` com `Limite de operações atingido!`.

**Parameters:**
- `releaseId` (path) **required** — ID da Campanha

**Responses:**
- `200` — Detalhes da campanha
- `400` — Erro ao buscar campanha
- `401` — Não autenticado ou chave inválida
- `403` — Limite de operações atingido (rate limit) ou acesso negado
- `404` — Campanha não encontrada

---

### `PUT` `/sendapi/releases/{releaseId}`

*Atualizar uma campanha*

> **Rate limit (dois controles):**
> - intervalo mínimo de **1 segundo** entre quaisquer requisições PUT neste recurso;
> - intervalo mínimo de **60 segundos** entre atualizações no **mesmo** `releaseId`.
> Ao exceder, a API responde `403` com `Limite de operações atingido!`.

**Parameters:**
- `releaseId` (path) **required** — ID da Campanha

**Request body** (`application/json`):
- `accountIds` (array<object>) — IDs das contas associadas
- `archived` (boolean) — Se a campanha está arquivada *(ex: `false`)*
- `group` (object) — 
  - `admins` (array<object>) — Lista de administradores do grupo
    - `name` (string) — 
    - `number` (string) — 
  - `communityEnabled` (boolean) —  *(ex: `false`)*
  - `countStart` (integer) —  *(ex: `1`)*
  - `disabledGroupSpawn` (boolean) —  *(ex: `false`)*
  - `disappearingMessagesInChat` (integer) —  *(ex: `-1`)*
  - `fixedDescription` (string) —  *(ex: `"TESTE"`)*
  - `image` (string) —  *(ex: `"https://sendflow.pro/assets/imgs/logo.png"`)*
  - `limit` (integer) —  *(ex: `350`)*
  - `margin` (integer) —  *(ex: `2`)*
  - `name` (string) —  *(ex: `"Exemplo"`)*
  - `numberplacedonstart` (boolean) —  *(ex: `false`)*
  - `onlyAdminsSpeak` (boolean) —  *(ex: `true`)*
- `name` (string) — Nome da campanha *(ex: `"campanha 03"`)*
- `position` (integer) —  *(ex: `-1`)*
- `deepLinking` (boolean) —  *(ex: `false`)*
- `projectId` (string) — 
- `type` (string) —  *(ex: `"WhatsRelease"`)*

**Responses:**
- `200` — Campanha atualizada com sucesso
- `400` — Erro ao atualizar a campanha
- `401` — Não autenticado ou chave inválida
- `403` — Limite de operações atingido (rate limit) ou acesso negado
- `404` — Campanha não encontrada

---

### `DELETE` `/sendapi/releases/{releaseId}`

*Excluir uma campanha*

> **Rate limit (dois controles):**
> - intervalo mínimo de **1 segundo** entre quaisquer requisições DELETE neste recurso;
> - intervalo mínimo de **60 segundos** entre exclusões do **mesmo** `releaseId`.
> Ao exceder, a API responde `403` com `Limite de operações atingido!`.

**Parameters:**
- `releaseId` (path) **required** — ID da campanha

**Responses:**
- `204` — Campanha excluída com sucesso
- `400` — Erro ao excluir campanha
- `401` — Não autenticado ou chave inválida
- `403` — Limite de operações atingido (rate limit) ou acesso negado
- `404` — Campanha não encontrada

---

### `GET` `/sendapi/releases/{releaseId}/groups`

*Buscar os grupos de uma campanha*

> Lista os grupos da campanha com id, nome, gid/jid, inviteCode, indicadores
> **full** (grupo cheio), **participantsAmount** (quantidade de participantes, pode variar
> conforme sincronização com a conta) e **count** (contagem interna do grupo), além do array
> **admins** (administradores configurados na campanha — configuração de grupo da release),
> o mesmo para todos os itens, refletindo a configuração aplicável aos grupos criados por ela.
> 
> **Rate limit (dois controles):** mesmas regras dos outros GET por `releaseId`
> (60 s entre requisições GET relacionadas a campanhas; 10 min por `releaseId`).
> Ao exceder, a API responde `403` com `Limite de operações atingido!`.

**Parameters:**
- `releaseId` (path) **required** — ID da Campanha

**Responses:**
- `200` — Lista de grupos da campanha com administradores configurados
- `400` — Erro ao buscar grupos
- `401` — Não autenticado ou não autorizado
- `403` — Limite de operações atingido (rate limit) ou acesso negado
- `404` — Release not found

---

### `PATCH` `/sendapi/releases/{releaseId}/redirect-link`

*Atualizar link de redirect (slug) da campanha*

> **Rate limit (dois controles):**
> - intervalo mínimo de **1 segundo** entre quaisquer requisições PATCH neste recurso;
> - intervalo mínimo de **60 segundos** entre alterações no **mesmo** `releaseId`.
> Ao exceder, a API responde `403` com `Limite de operações atingido!`.

**Parameters:**
- `releaseId` (path) **required** — ID da campanha

**Request body** (`application/json`):
- `slug` (string) **required** — Novo slug do link de redirect (espaços são removidos e o valor é salvo em minúsculas)

**Responses:**
- `200` — Slug atualizado com sucesso
- `400` — Dados inválidos ou slug vazio após normalização
- `401` — Usuário não autorizado
- `403` — Limite de operações atingido (rate limit) ou acesso negado
- `404` — Campanha não encontrada
- `409` — Slug já utilizado por outra campanha

---

### `GET` `/sendapi/releases/{releaseId}/analytics`

*Buscar métricas de uma campanha*

> **Rate limit (dois controles):** mesmas chaves dos GET por `releaseId`
> (1 s entre requisições GET relacionadas a campanhas; 60 s por `releaseId`).
> Ao exceder, a API responde `403` com `Limite de operações atingido!`.

**Parameters:**
- `releaseId` (path) **required** — ID da campanha

**Responses:**
- `200` — Métricas da campanha retornadas com sucesso
- `400` — Erro ao buscar métricas da campanha
- `401` — Usuário não autorizado
- `403` — Limite de operações atingido (rate limit) ou acesso negado
- `404` — Campanha não encontrada

---

### `GET` `/sendapi/releases/{releaseId}/leadscoring`

*Buscar leadscoring de uma campanha*

> **Rate limit (dois controles):** mesmas chaves dos GET por `releaseId`
> (60 s entre requisições GET relacionadas a campanhas; 10 min por `releaseId`).
> Ao exceder, a API responde `403` com `Limite de operações atingido!`.

**Parameters:**
- `releaseId` (path) **required** — ID da campanha

**Responses:**
- `200` — Métricas da campanha retornadas com sucesso
- `400` — Erro ao buscar métricas da campanha
- `401` — Usuário não autorizado
- `403` — Limite de operações atingido (rate limit) ou acesso negado
- `404` — Campanha não encontrada

---

### `GET` `/sendapi/releases/{releaseId}/leadscoring/download`

*Baixar arquivo de leadscoring*

> **Rate limit (dois controles):** mesmas chaves dos GET por `releaseId`
> (60 s entre requisições GET relacionadas a campanhas; 10 min por `releaseId`).
> Ao exceder, a API responde `403` com `Limite de operações atingido!`.

**Parameters:**
- `releaseId` (path) **required** — ID da campanha

**Responses:**
- `200` — Arquivo de leadscoring baixado com sucesso
- `400` — Erro ao baixar arquivo de leadscoring
- `401` — Usuário não autorizado
- `403` — Limite de operações atingido (rate limit) ou acesso negado
- `404` — Campanha não encontrada

---

## SendAPI - Releases (em desenvolvimento)


### `POST` `/sendapi/releases/{releaseId}/remove-duplicated-participants`

*Remover participantes duplicados (em desenvolvimento)*

> **Rate limit:** intervalo mínimo de **1 segundo** entre uma requisição e a próxima.
> Ao exceder, a API responde `403` com `Limite de operações atingido!`.

**Parameters:**
- `releaseId` (path) **required** — ID da campanha

**Responses:**
- `200` — Ação criada com sucesso
- `400` — Erro ao criar ação
- `401` — Usuário não autorizado
- `403` — Limite de operações atingido (rate limit) ou acesso negado
- `404` — Campanha não encontrada

---

## SendAPI - Verification


### `POST` `/sendapi/verify-number`

*Verificar se o número está na lista de bloqueios*

> Rota pública (sem API key). **Rate limit:** por endereço IP (**1 segundo**) e por combinação
> campanha + número normalizado (**3 segundos**). Ao exceder, a API responde `403` com
> `Limite de operações atingido!`.

**Request body** (`application/json`):
- `releaseId` (string) — ID da campanha *(ex: `"7LLztsEGLPNBBBBBBdtItXfc52"`)*
- `phoneNumber` (string) — Número de telefone a ser verificado *(ex: `"81999999999"`)*

**Responses:**
- `200` — Resultado da verificação retornado com sucesso
- `400` — Dados inválidos ou erro na verificação
- `403` — Limite de operações atingido (rate limit)

---
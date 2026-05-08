# SendFlow SendAPI — Documentação Oficial (extraída de sendflow.pro/whats/sendapi)

**Base URL:** `https://sendflow.pro/sendapi`
**Auth:** `Authorization: Bearer YOUR_API_KEY`

> Na aba Campanhas, `GET /releases/{releaseId}/groups` retorna, por grupo, os campos `full`, `participantsAmount` e `count`, além de `id`, `nome`, `gid/jid`, `inviteCode` e `admins`.

---


## Campanhas

GET
Buscar todas as campanhas do usuário
Endpoint:
/releases
Descrição:

Retorna todas as campanhas (releases) do usuário autenticado.

Respostas:
200

Lista de campanhas retornada com sucesso

400

Erro ao buscar campanhas

404

Nenhuma campanha encontrada para este usuário

Exemplo de Response:
[
  {
    "id": "nGhE4dPNWV5XreeABCDE",
    "accountIds": ["pwYE3dPNWV5XreeABCDE"],
    "archived": false,
    "group": {
      "admins": [
        {
          "name": "Maria",
          "number": "558199999999"
        }
      ],
      "communityEnabled": false,
      "countStart": 1,
      "disabledGroupSpawn": false,
      "disappearingMessagesInChat": -1,
      "fixedDescription": "TESTE",
      "image": "https://sendflow.pro/assets/imgs/logo.png",
      "limit": 350,
      "margin": 2,
      "name": "Exemplo",
      "numberplacedonstart": false,
      "onlyAdminsSpeak": true,
      "groupCreationMode": "normal",
      "createOpenGroupAndCloseAfter": true
    },
    "name": "campanha 03",
    "position": -1,
    "projectId": null,
    "type": "WhatsRelease"
  }
]
POST
Criar uma nova campanha
Endpoint:
/releases
Descrição:

Cria uma nova campanha (release) para o usuário autenticado.

Parâmetros do Body (JSON):

name (string, obrigatório): Nome da campanha

type (string, obrigatório): Tipo da campanha (WhatsRelease, WhatsList, WhatsViralCampaign)

projectId (string, opcional): ID do projeto (opcional)

Exemplo de Request:
{
  "name": "campanha 03",
  "type": "WhatsRelease",
  "projectId": "1234567890"
}
Respostas:
201

Campanha criada com sucesso

400

Dados inválidos ou erro na criação

401

Não autorizado

Exemplo de Response:
{
  "id": "nGhE4dPNWV5XreeABCDE"
}
GET
Buscar uma única campanha
Endpoint:
/releases/{releaseId}
Descrição:

Retorna os detalhes de uma campanha específica.

Parâmetros da URL:

releaseId (string, obrigatório): ID da campanha

Respostas:
200

Detalhes da campanha

404

Campanha não encontrada

401

Usuário não autorizado

400

Erro ao buscar campanha

Exemplo de Response:
{
  "id": "nGhE4dPNWV5XreeABCDE",
  "accountIds": ["pwYE3dPNWV5XreeABCDE"],
  "archived": false,
  "group": {
    "admins": [
      {
        "name": "Maria",
        "number": "558199999999"
      }
    ],
    "communityEnabled": false,
    "countStart": 1,
    "disabledGroupSpawn": false,
    "disappearingMessagesInChat": -1,
    "fixedDescription": "TESTE",
    "image": "https://sendflow.pro/assets/imgs/logo.png",
    "limit": 350,
    "margin": 2,
    "name": "Exemplo",
    "numberplacedonstart": false,
    "onlyAdminsSpeak": true,
	"groupCreationMode": "normal",
	"createOpenGroupAndCloseAfter": true
  },
  "name": "campanha 03",
  "position": -1,
  "projectId": null,
  "type": "WhatsRelease"
}
GET
Buscar os grupos de uma campanha
Endpoint:
/releases/{releaseId}/groups
Descrição:

Retorna a lista de grupos da campanha com id, nome, gid, jid, inviteCode, full (grupo cheio), participantsAmount (quantidade de participantes; pode variar conforme sincronização com a conta) e count (contagem do grupo). Em cada item, o array admins traz os administradores configurados na campanha (nome e número), refletindo a configuração de grupo da release aplicável aos grupos criados por ela.

Parâmetros da URL:

releaseId (string, obrigatório): ID da campanha

Respostas:
200

Lista de grupos da campanha (array vazio se não houver grupos)

404

Campanha não encontrada

401

Usuário não autorizado

400

Erro ao buscar grupos

Exemplo de Response:
[
  {
    "id": "120363292004848696",
    "name": "Grupo 1",
    "gid": "558191080294",
    "jid": "558191080294",
    "inviteCode": "123456",
    "full": false,
    "participantsAmount": 42,
    "count": 1,
    "admins": [
      {
        "name": "Maria",
        "number": "558199999999"
      }
    ]
  },
  {
    "id": "120363292004848697",
    "name": "Grupo 2",
    "gid": "558195216823",
    "jid": "558195216823",
    "inviteCode": "123457",
    "full": true,
    "participantsAmount": 256,
    "count": 2,
    "admins": [
      {
        "name": "Maria",
        "number": "558199999999"
      }
    ]
  }
]
PATCH
Atualizar link de redirect (slug)
Endpoint:
/releases/{releaseId}/redirect-link
Descrição:

Altera apenas o slug usado no link de redirect da campanha. O valor é normalizado: espaços são removidos e o slug é salvo em minúsculas. Não é possível reutilizar um slug já usado por outra campanha.

Parâmetros da URL:

releaseId (string, obrigatório): ID da campanha

Parâmetros do Body (JSON):

slug (string, obrigatório): Novo slug do redirect

Exemplo de Request:
{
  "slug": "minha-campanha-vip"
}
Respostas:
200

Slug atualizado com sucesso

400

Dados inválidos ou slug vazio após normalização

401

Usuário não autorizado

404

Campanha não encontrada

409

Slug já em uso por outra campanha

Exemplo de Response:
{
  "message": "Link de redirect atualizado com sucesso",
  "success": true,
  "id": "nGhE4dPNWV5XreeABCDE",
  "slug": "minha-campanha-vip"
}
PUT
Atualizar uma campanha
Endpoint:
/releases/{releaseId}
Descrição:

Atualiza os dados de uma campanha existente.

Parâmetros da URL:

releaseId (string, obrigatório): ID da campanha

Parâmetros do Body (JSON):

accountIds (array, opcional): IDs das contas associadas

archived (boolean, opcional): Se a campanha está arquivada

group (object, opcional): Configurações do grupo

group.admins (array, opcional): Lista de administradores do grupo

group.communityEnabled (boolean, opcional): Se comunidade está habilitada

group.groupCreationMode (string, opcional): Modo de criação do grupo (normal ou safe)

group.createOpenGroupAndCloseAfter (boolean, opcional): Se deve criar um grupo aberto e fechar depois

group.countStart (integer, opcional): Número inicial da contagem

group.disabledGroupSpawn (boolean, opcional): Se criação de grupos está desabilitada

group.disappearingMessagesInChat (integer, opcional): Tempo para mensagens desaparecerem (-1 para desabilitado)

group.fixedDescription (string, opcional): Descrição fixa do grupo

group.image (string, opcional): URL da imagem do grupo

group.limit (integer, opcional): Limite de membros por grupo

group.margin (integer, opcional): Margem de segurança

group.name (string, opcional): Nome base do grupo

group.numberplacedonstart (boolean, opcional): Se número é colocado no início

group.onlyAdminsSpeak (boolean, opcional): Se apenas admins podem falar

name (string, opcional): Nome da campanha

position (integer, opcional): Posição da campanha

projectId (string, opcional): ID do projeto (nullable)

type (string, opcional): Tipo da campanha

deepLinking (boolean, opcional): Se o deep linking está habilitado

Exemplo de Request:
{
  "accountIds": ["pwYE3dPNWV5XreeABCDE"],
  "archived": false,
  "group": {
    "admins": [
      {
        "name": "Maria",
        "number": "558199999999"
      },
      {
        "name": "João",
        "number": "558199999999"
      }
    ],
    "communityEnabled": false,
    "countStart": 1,
    "disabledGroupSpawn": false,
    "disappearingMessagesInChat": -1,
    "fixedDescription": "TESTE",
    "image": "https://sendflow.pro/assets/imgs/logo.png",
    "limit": 350,
    "margin": 2,
    "name": "Exemplo",
    "numberplacedonstart": false,
    "onlyAdminsSpeak": true,
	"groupCreationMode": "normal",
	"createOpenGroupAndCloseAfter": true
  },
  "name": "campanha 03",
  "position": -1,
  "projectId": null,
  "type": "WhatsRelease",
  "deepLinking": false
}
Respostas:
200

Campanha atualizada com sucesso

404

Campanha não encontrada

401

Usuário não autorizado

400

Dados inválidos

Exemplo de Response:
{
  "message": "Campanha atualizada com sucesso",
  "success": true,
  "id": "nGhE4dPNWV5XreeABCDE"
}
DELETE
Deletar uma campanha
Endpoint:
/releases/{releaseId}
Descrição:

Remove permanentemente uma campanha do sistema.

Parâmetros da URL:

releaseId (string, obrigatório): ID da campanha

Respostas:
204

Campanha deletada com sucesso

404

Campanha não encontrada

401

Usuário não autorizado

400

Erro ao deletar campanha

Exemplo de Response:
{
  "message": "Campanha deletada com sucesso"
}
POST
Remover participantes duplicados [EM DESENVOLVIMENTO]
Endpoint:
/releases/{releaseId}/remove-duplicated-participants
Descrição:

Cria uma ação para remover participantes duplicados de uma campanha. Esta funcionalidade está em desenvolvimento.

Parâmetros da URL:

releaseId (string, obrigatório): ID da campanha

Respostas:
200

Ação criada com sucesso

400

Erro ao criar ação

404

Campanha não encontrada

401

Usuário não autorizado

Exemplo de Response:
{
  "message": "Ação criada com sucesso",
  "success": true
}
Atenção: Esta funcionalidade está em desenvolvimento e pode sofrer alterações.
GET
Buscar métricas de uma campanha (Analytics)
Endpoint:
/releases/{releaseId}/analytics
Descrição:

Retorna as métricas e analytics de uma campanha específica.

Parâmetros da URL:

releaseId (string, obrigatório): ID da campanha

Respostas:
200

Métricas da campanha retornadas com sucesso

400

Erro ao buscar métricas da campanha

401

Usuário não autorizado

404

Campanha não encontrada

Exemplo de Response:
{
	"add": {
			"dates": {
					"10072025": 20,
					"11072025": 30,
					"12072025": 5,
					"13072025": 40,
					"14072025": 5
			},
			"total": 100
	},
	"remove": {
			"dates": {
					"10072025": 3,
					"11072025": 5,
					"12072025": 5,
					"13072025": 6,
					"14072025": 1
			},
			"total": 20
	},
	"clicks": {
		"dates": {
					"10072025": 130,
					"11072025": 210,
					"12072025": 174,
					"13072025": 20,
					"14072025": 6
			},
			"total": 540
	}
}
GET
Buscar leadscoring de uma campanha
Endpoint:
/releases/{releaseId}/leadscoring
Descrição:

Ao ser acionado, gera o leadscoring de uma campanha.

Parâmetros da URL:

releaseId (string, obrigatório): ID da campanha

Respostas:
200

Dados de leadscoring gerados com sucesso

400

Erro ao gerar leadscoring

401

Usuário não autorizado

404

Campanha não encontrada

Exemplo de Response:
{
  "success": true
}
GET
Baixar arquivo de leadscoring
Endpoint:
/releases/{releaseId}/leadscoring/download
Descrição:

Retorna a URL para download do arquivo de leadscoring da campanha.

Parâmetros da URL:

releaseId (string, obrigatório): ID da campanha

Respostas:
200

URL do arquivo retornada com sucesso

400

Arquivo de leadscoring não encontrado

401

Usuário não autorizado

404

Campanha não encontrada

Exemplo de Response:
"https://storage.sendflow.pro/leadscoring/nGhE4dPNWV5XreeABCDE/leadscoring-2025-01-21.xlsx"
Informações sobre Releases

Tipos de Campanha: WhatsRelease (campanhas padrão), WhatsList (listas de transmissão), WhatsViralCampaign (campanhas virais).

Estrutura de Grupos: Cada release pode ter configurações específicas para criação e gerenciamento de grupos do WhatsApp.

Projetos: Releases podem ser associadas a projetos para melhor organização e segmentação.

Posicionamento: O campo position define a ordem das campanhas. Valores menores aparecem primeiro.

Arquivamento: Campanhas arquivadas (archived: true) são mantidas no sistema mas não aparecem nas listagens principais.

Exclusão: Campanhas deletadas são removidas permanentemente e não podem ser recuperadas.

Analytics: Métricas incluem dados como total de participantes, grupos ativos, mensagens enviadas e taxas de conversão.

Leadscoring: Sistema de pontuação automática baseado no engajamento e interações dos participantes. O arquivo pode ser baixado em formato Excel.

Remoção de Duplicatas: Funcionalidade em desenvolvimento para identificar e remover participantes duplicados automaticamente.

Códigos de Erro Comuns
400

Bad Request: Dados inválidos ou parâmetros obrigatórios ausentes

401

Unauthorized: API Key inválida ou usuário não autorizado

404

Not Found: Recurso não encontrado

500

Internal Server Error: Erro interno do servidor



## Grupos de Campanhas

Release Groups

API para gerenciamento de grupos em campanhas do WhatsApp. Permite criar, consultar, atualizar e deletar grupos associados a campanhas específicas.

POST
Adicionar um grupo a uma campanha
Endpoint:
/sendapi/release-groups
Descrição:

Adiciona um grupo a uma campanha específica. O grupo pode ser do tipo group, community, community_default ou community_group.

Parâmetros do Body (JSON):

gid (string, obrigatório): ID do grupo do WhatsApp

releaseId (string, obrigatório): ID da campanha

count (number, opcional): Contagem

name (string, obrigatório): Nome do grupo

full (boolean, opcional): Indica se o grupo está cheio

type (string, opcional): Tipo do grupo (group, community, community_default, community_group)

Exemplo de Request:
{
  "gid": "120363292004848696@g.us",
  "releaseId": "biuumwkQqFtMcOCbGEgk",
  "count": 1,
  "name": "Teste Send #1",
  "full": false,
  "type": "group"
}
Respostas:
201

Grupo criado com sucesso

400

Dados inválidos

401

Usuário não autorizado

Exemplo de Response:
{
  "message": "Grupo criado com sucesso",
  "id": "generated_group_id"
}
GET
Obter um grupo na campanha
Endpoint:
/sendapi/release-groups/{releaseGroupId}
Descrição:

Obtém informações detalhadas de um grupo específico associado a uma campanha.

Parâmetros da URL:

releaseGroupId (string, obrigatório): ID do grupo na campanha

Respostas:
200

Grupo obtido com sucesso

401

Usuário não autorizado

404

Grupo não encontrado

Exemplo de Response:
{
  "id": "release_group_id",
  "gid": "120363292004848696@g.us",
  "userId": "user_id",
  "releaseId": "biuumwkQqFtMcOCbGEgk",
  "count": 1,
  "name": "Teste Send #1",
  "inviteCode": "invite_code",
  "full": false,
  "clicks": 0,
  "clicksAmount": 0,
  "participantsAmount": 0,
  "clicksMap": {}
}
PUT
Atualizar um grupo na campanha
Endpoint:
/sendapi/release-groups/{releaseGroupId}
Descrição:

Atualiza informações de um grupo existente. Apenas o proprietário do grupo pode atualizá-lo.

Parâmetros da URL:

releaseGroupId (string, obrigatório): ID do grupo na campanha

Parâmetros do Body (JSON):

count (integer, opcional): Contagem

full (boolean, opcional): Indica se o grupo está cheio

name (string, opcional): Nome do grupo

Exemplo de Request:
{
  "count": 5,
  "full": true,
  "name": "Grupo Atualizado #1"
}
Respostas:
200

Grupo atualizado com sucesso

400

Dados inválidos

401

Usuário não autorizado

404

Grupo não encontrado

Exemplo de Response:
{
  "message": "Grupo atualizado com sucesso",
  "id": "release_group_id"
}
DELETE
Deletar um grupo na campanha
Endpoint:
/sendapi/release-groups/{releaseGroupId}
Descrição:

Remove permanentemente um grupo da campanha. Apenas o proprietário do grupo pode deletá-lo.

Parâmetros da URL:

releaseGroupId (string, obrigatório): ID do grupo na campanha

Respostas:
204

Grupo deletado com sucesso

400

Erro ao deletar o grupo

401

Usuário não autorizado

404

Grupo não encontrado

Exemplo de Response:
{
  "message": "Grupo deletado com sucesso"
}
Atenção: Esta operação é irreversível. Uma vez deletado, o grupo não pode ser recuperado.
Modelo de Dados - Release Group

Estrutura completa do objeto Release Group retornado pela API:

id (string): ID único do grupo

gid (string): ID do grupo do WhatsApp

userId (string): ID do usuário proprietário

releaseId (string): ID da campanha associada

count (number): Contagem do grupo

name (string): Nome do grupo

inviteCode (string): Código de convite do grupo

full (boolean): Indica se o grupo está cheio

clicks (number): Número de cliques

clicksAmount (number): Quantidade de cliques

participantsAmount (number): Quantidade de participantes

clicksMap (object): Mapa de cliques

Códigos de Erro Comuns
400

Bad Request: Dados inválidos ou parâmetros obrigatórios ausentes

401

Unauthorized: API Key inválida ou usuário não autorizado

404

Not Found: Recurso não encontrado

500

Internal Server Error: Erro interno do servidor



## Ações

Actions

API para gerenciamento de ações automatizadas no WhatsApp. Permite criar grupos, gerenciar administradores, enviar mensagens multimídia e executar operações em massa nas campanhas.

POST
Criar um grupo
Endpoint:
/sendapi/actions/group-create
Descrição:

Cria um novo grupo no WhatsApp com participantes específicos através de uma ação programada.

Parâmetros do Body (JSON):

accountId (string, obrigatório): ID da conta

releaseId (string, obrigatório): ID da campanha

assistantId (string, opcional): ID do assistente

payload.name (string, obrigatório): Nome do grupo

payload.participants (array, obrigatório): Lista de participantes (números com formato WhatsApp)

payload.associatedUserIds (array, opcional): IDs de usuários associados

payload.standardization (boolean, opcional): Se deve ser padronizado (padrão: false)

Exemplo de Request:
{
  "accountId": "7LLztsEGLPNAAAAAAAAXfc52",
  "releaseId": "7LLztsEGLPNBBBBBBdtItXfc52",
  "assistantId": "assistant_id_optional",
  "payload": {
    "name": "grupo teste 123",
    "participants": ["557581133148@s.whatsapp.net"],
    "associatedUserIds": ["user1", "user2"],
    "standardization": false
  }
}
Respostas:
201

Ação criada com sucesso

400

Dados inválidos

401

Erro de autenticação

403

Acesso negado

404

Ação não encontrada

500

Erro interno do servidor

Exemplo de Response:
{
  "message": "Ação de criação de grupo criada com sucesso",
  "id": "action_id_generated"
}
POST
Tornar usuário admin de grupo
Endpoint:
/sendapi/actions/make-group-admin
Descrição:

Torna um ou mais usuários administradores de grupos específicos ou de todos os grupos de uma campanha.

Parâmetros do Body (JSON):

accountId (string, obrigatório): ID da conta

releaseId (string, obrigatório): ID da campanha

participants (array, obrigatório): Lista de participantes com número e nome

participants[].number (string, obrigatório): Número do participante (sem formatação WhatsApp)

participants[].name (string, obrigatório): Nome do participante

chooseSpecificGroups (boolean, opcional): Se deve escolher grupos específicos (padrão: false)

groupIds (array, opcional): Lista de GIDs de grupos (sem @g.us) - obrigatório se chooseSpecificGroups for true

Exemplo de Request:
{
  "accountId": "7LLztsEGLPNAAAAAAAAXfc52",
  "releaseId": "7LLztsEGLPNBBBBBBdtItXfc52",
  "participants": [
    {
      "number": "557581133148",
      "name": "João"
    }
  ],
  "chooseSpecificGroups": true,
  "groupIds": ["120363420152631339", "120363359314057310"]
}
Respostas:
201

Ação criada com sucesso

400

Dados inválidos ou campanha não encontrada

401

Usuário não autorizado

403

Acesso negado

404

Ação não encontrada

500

Erro interno do servidor

Exemplo de Response:
{
  "message": "Ação de criação de grupo criada com sucesso",
  "id": "action_id_generated"
}
POST
Enviar mensagem de texto
Endpoint:
/sendapi/actions/send-text-message
Descrição:

Envia uma mensagem de texto para os grupos da campanha com opções de agendamento e velocidade de envio.

Parâmetros do Body (JSON):

accountId (string, opcional): ID da conta (opcional se accountIds for fornecido)

accountIds (array, opcional): IDs das contas (opcional se accountId for fornecido). Permite enviar para múltiplas contas. Não pode ser usado junto com accountId

releaseId (string, obrigatório): ID da campanha

messageText (string, obrigatório): Texto a ser enviado

linkPreview (boolean, opcional): Se deve gerar preview do link

scheduled (boolean, opcional): Se a mensagem deve ser agendada

scheduledTo (string, opcional): Data de agendamento (formato ISO 8601)

chooseSpecificGroups (boolean, opcional): Se deve escolher grupos específicos (padrão: false)

groupIds (array, opcional): Lista de GIDs de grupos (sem @g.us) - obrigatório se chooseSpecificGroups for true

options.shippingSpeed (string, opcional): Velocidade de entrega (none, custom, fast, normal, slow)

options.customShippingSpeed.min (integer, opcional): Tempo mínimo personalizado (segundos)

options.customShippingSpeed.max (integer, opcional): Tempo máximo personalizado (segundos)

Exemplo de Request:
{
  "accountId": "pwYE3dPNWV5XtrrPbba0",
  "releaseId": "De3MLuRlkjk8kGLp2cCnN",
  "messageText": "Confira este link: https://exemplo.com",
  "linkPreview": true,
  "scheduled": true,
  "scheduledTo": "2025-04-21T10:00:00.000Z",
  "chooseSpecificGroups": true,
  "groupIds": ["120363420152631339", "120363359314057310"],
  "options": {
    "shippingSpeed": "custom",
    "customShippingSpeed": {
      "min": 10,
      "max": 20
    }
  }
}

// Exemplo com múltiplas contas (accountIds):
{
  "accountIds": ["pwYE3dPNWV5XtrrPbba0", "pwYE3dPNWV5XtrrPbba1"],
  "releaseId": "De3MLuRlkjk8kGLp2cCnN",
  "messageText": "Confira este link: https://exemplo.com",
  "linkPreview": true,
  "scheduled": true,
  "scheduledTo": "2025-04-21T10:00:00.000Z",
  "chooseSpecificGroups": true,
  "groupIds": ["120363420152631339", "120363359314057310"],
  "options": {
    "shippingSpeed": "custom",
    "customShippingSpeed": {
      "min": 10,
      "max": 20
    }
  }
}
Respostas:
201

Ação criada com sucesso

400

Erro ao criar a ação

401

Erro de autenticação

Exemplo de Response:
{
  "message": "Ação criada com sucesso",
  "id": "action_id_generated"
}
Atenção: É necessário fornecer accountId ou accountIds, mas não ambos ao mesmo tempo.
POST
Enviar mensagem com imagem
Endpoint:
/sendapi/actions/send-image-message
Descrição:

Envia uma mensagem contendo uma imagem para os grupos da campanha.

Parâmetros do Body (JSON):

accountId (string, opcional): ID da conta (opcional se accountIds for fornecido)

accountIds (array, opcional): IDs das contas (opcional se accountId for fornecido). Permite enviar para múltiplas contas. Não pode ser usado junto com accountId

releaseId (string, obrigatório): ID da campanha

caption (string, opcional): Legenda da imagem

url (string, obrigatório): URL da imagem a ser enviada

scheduledTo (string, opcional): Data de agendamento (formato ISO 8601)

chooseSpecificGroups (boolean, opcional): Se deve escolher grupos específicos (padrão: false)

groupIds (array, opcional): Lista de GIDs de grupos (sem @g.us) - obrigatório se chooseSpecificGroups for true

options.shippingSpeed (string, opcional): Velocidade de entrega (none, custom, fast, normal, slow)

options.customShippingSpeed.min (integer, opcional): Tempo mínimo personalizado (segundos)

options.customShippingSpeed.max (integer, opcional): Tempo máximo personalizado (segundos)

Exemplo de Request:
{
  "accountId": "pwYE3dPNWV5XtrrPbba0",
  "releaseId": "De3MLuRlkjk8kGLp2cCnN",
  "caption": "Imagem de teste",
  "url": "https://www.google.com.br/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png",
  "scheduledTo": null,
  "chooseSpecificGroups": true,
  "groupIds": ["120363420152631339", "120363359314057310"],
  "options": {
    "shippingSpeed": "fast"
  }
}

// Exemplo com múltiplas contas (accountIds):
{
  "accountIds": ["pwYE3dPNWV5XtrrPbba0", "pwYE3dPNWV5XtrrPbba1"],
  "releaseId": "De3MLuRlkjk8kGLp2cCnN",
  "caption": "Imagem de teste",
  "url": "https://www.google.com.br/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png",
  "scheduledTo": null,
  "chooseSpecificGroups": true,
  "groupIds": ["120363420152631339", "120363359314057310"],
  "options": {
    "shippingSpeed": "fast"
  }
}
Respostas:
201

Ação criada com sucesso

400

Erro ao criar a ação

401

Erro de autenticação

Exemplo de Response:
{
  "message": "Ação criada com sucesso",
  "id": "action_id_generated"
}
Atenção: É necessário fornecer accountId ou accountIds, mas não ambos ao mesmo tempo.
POST
Enviar mensagem com vídeo
Endpoint:
/sendapi/actions/send-video-message
Descrição:

Envia uma mensagem contendo um vídeo para os grupos da campanha.

Parâmetros do Body (JSON):

accountId (string, opcional): ID da conta (opcional se accountIds for fornecido)

accountIds (array, opcional): IDs das contas (opcional se accountId for fornecido). Permite enviar para múltiplas contas. Não pode ser usado junto com accountId

releaseId (string, obrigatório): ID da campanha

caption (string, opcional): Legenda do vídeo

url (string, obrigatório): URL do vídeo a ser enviado

scheduledTo (string, opcional): Data de agendamento (formato ISO 8601)

chooseSpecificGroups (boolean, opcional): Se deve escolher grupos específicos (padrão: false)

groupIds (array, opcional): Lista de GIDs de grupos (sem @g.us) - obrigatório se chooseSpecificGroups for true

options.shippingSpeed (string, opcional): Velocidade de entrega (none, custom, fast, normal, slow)

options.customShippingSpeed.min (integer, opcional): Tempo mínimo personalizado (segundos)

options.customShippingSpeed.max (integer, opcional): Tempo máximo personalizado (segundos)

Exemplo de Request:
{
  "accountId": "pwYE3dPNWV5XtrrPbba0",
  "releaseId": "De3MLuRlkjk8kGLp2cCnN",
  "caption": "Video de teste",
  "url": "https://video.com/video.mp4",
  "scheduledTo": null,
  "chooseSpecificGroups": false,
  "options": {
    "shippingSpeed": "normal"
  }
}

// Exemplo com múltiplas contas (accountIds):
{
  "accountIds": ["pwYE3dPNWV5XtrrPbba0", "pwYE3dPNWV5XtrrPbba1"],
  "releaseId": "De3MLuRlkjk8kGLp2cCnN",
  "caption": "Video de teste",
  "url": "https://video.com/video.mp4",
  "scheduledTo": null,
  "chooseSpecificGroups": false,
  "options": {
    "shippingSpeed": "normal"
  }
}
Respostas:
201

Ação criada com sucesso

400

Erro ao criar a ação

401

Erro de autenticação

Exemplo de Response:
{
  "message": "Ação criada com sucesso",
  "id": "action_id_generated"
}
Atenção: É necessário fornecer accountId ou accountIds, mas não ambos ao mesmo tempo.
POST
Enviar mensagem com áudio
Endpoint:
/sendapi/actions/send-audio-message
Descrição:

Envia uma mensagem contendo um áudio para os grupos da campanha.

Parâmetros do Body (JSON):

accountId (string, opcional): ID da conta (opcional se accountIds for fornecido)

accountIds (array, opcional): IDs das contas (opcional se accountId for fornecido). Permite enviar para múltiplas contas. Não pode ser usado junto com accountId

releaseId (string, obrigatório): ID da campanha

caption (string, opcional): Legenda do áudio

url (string, obrigatório): URL do áudio a ser enviado

ptt (boolean, opcional): Se true, envia como gravação (push-to-talk). Se false ou não informado, envia como áudio normal

scheduledTo (string, opcional): Data de agendamento (formato ISO 8601)

chooseSpecificGroups (boolean, opcional): Se deve escolher grupos específicos (padrão: false)

groupIds (array, opcional): Lista de GIDs de grupos (sem @g.us) - obrigatório se chooseSpecificGroups for true

options.shippingSpeed (string, opcional): Velocidade de entrega (none, custom, fast, normal, slow)

options.customShippingSpeed.min (integer, opcional): Tempo mínimo personalizado (segundos)

options.customShippingSpeed.max (integer, opcional): Tempo máximo personalizado (segundos)

Exemplo de Request:
{
  "accountId": "pwYE3dPNWV5XtrrPbba0",
  "releaseId": "De3MLuRlkjk8kGLp2cCnN",
  "caption": "Audio de teste",
  "url": "https://audio.com/audio.mp3",
  "ptt": true,
  "scheduledTo": null,
  "options": {
    "shippingSpeed": "slow"
  }
}

// Exemplo com múltiplas contas (accountIds):
{
  "accountIds": ["pwYE3dPNWV5XtrrPbba0", "pwYE3dPNWV5XtrrPbba1"],
  "releaseId": "De3MLuRlkjk8kGLp2cCnN",
  "caption": "Audio de teste",
  "url": "https://audio.com/audio.mp3",
  "ptt": true,
  "scheduledTo": null,
  "options": {
    "shippingSpeed": "slow"
  }
}
Respostas:
201

Ação criada com sucesso

400

Erro ao criar a ação

401

Erro de autenticação

Exemplo de Response:
{
  "message": "Ação criada com sucesso",
  "id": "action_id_generated"
}
Atenção: É necessário fornecer accountId ou accountIds, mas não ambos ao mesmo tempo.
POST
Enviar mensagem universal
Endpoint:
/sendapi/actions/send-message
Descrição:

Envia uma mensagem de qualquer tipo (texto, imagem, áudio, vídeo) com configurações avançadas.

Parâmetros do Body (JSON):

accountId (string, opcional): ID da conta (opcional se accountIds for fornecido)

accountIds (array, opcional): IDs das contas (opcional se accountId for fornecido). Permite enviar para múltiplas contas. Não pode ser usado junto com accountId

releaseId (string, obrigatório): ID da campanha

type (string, obrigatório): Tipo de mensagem (extendedTextMessage, imageMessage, videoMessage, audioMessage)

text (string, opcional): Texto da mensagem (para mensagens de texto)

linkPreview (boolean, opcional): Se deve gerar preview do link

caption (string, opcional): Legenda (para imagens, vídeos ou áudios)

url (string, opcional): URL do arquivo (para imagens, vídeos ou áudios)

ptt (boolean, opcional): Se true, envia como gravação (push-to-talk). Apenas para audioMessage. Se false ou não informado, envia como áudio normal

scheduledTo (string, opcional): Data de agendamento (formato ISO 8601)

chooseSpecificGroups (boolean, opcional): Se deve escolher grupos específicos (padrão: false)

groupIds (array, opcional): Lista de GIDs de grupos (sem @g.us) - obrigatório se chooseSpecificGroups for true

options.ephemeralExpiration (integer, opcional): Tempo para expiração da mensagem

options.mentionAllParticipants (boolean, opcional): Mencionar todos os participantes

options.shippingSpeed (string, opcional): Velocidade de entrega (none, custom, fast, normal, slow)

options.customShippingSpeed.min (integer, opcional): Tempo mínimo personalizado (segundos)

options.customShippingSpeed.max (integer, opcional): Tempo máximo personalizado (segundos)

Exemplo de Request:
{
  "accountId": "pwYE3dPNWV5XtrrPbba0",
  "releaseId": "De3MLuRlkjk8kGLp2cCnN",
  "type": "extendedTextMessage",
  "text": "Confira este link: https://exemplo.com",
  "linkPreview": true,
  "scheduledTo": null,
  "chooseSpecificGroups": true,
  "groupIds": ["120363420152631339", "120363359314057310"],
  "options": {
    "ephemeralExpiration": -1,
    "mentionAllParticipants": false,
    "shippingSpeed": "fast",
    "customShippingSpeed": {
      "min": 10,
      "max": 20
    }
  }
}

// Exemplo com múltiplas contas (accountIds):
{
  "accountIds": ["pwYE3dPNWV5XtrrPbba0", "pwYE3dPNWV5XtrrPbba1"],
  "releaseId": "De3MLuRlkjk8kGLp2cCnN",
  "type": "extendedTextMessage",
  "text": "Confira este link: https://exemplo.com",
  "linkPreview": true,
  "scheduledTo": null,
  "chooseSpecificGroups": true,
  "groupIds": ["120363420152631339", "120363359314057310"],
  "options": {
    "ephemeralExpiration": -1,
    "mentionAllParticipants": false,
    "shippingSpeed": "fast",
    "customShippingSpeed": {
      "min": 10,
      "max": 20
    }
  }
}
Respostas:
201

Ação criada com sucesso

400

Erro ao criar a ação

401

Erro de autenticação

Exemplo de Response:
{
  "message": "Ação criada com sucesso",
  "id": "action_id_generated"
}
Atenção: É necessário fornecer accountId ou accountIds, mas não ambos ao mesmo tempo.
POST
Criar ações de analise de grupos
Endpoint:
/sendapi/actions/analyze-groups
Descrição:

Cria ações de refresh de grupos para contas específicas. Se accountIds não for fornecido, usa todas as contas autenticadas do usuário.

Parâmetros do Body (JSON):

accountIds (array, obrigatório): IDs das contas. Se não fornecido, usa todas as contas autenticadas do usuário

to (string, opcional): padrão: "anti-spam"

Exemplo de Request:
{
  "accountIds": ["pwYE3dPNWV5XtaaaPbba0", "pwYE3dPNWV5XtaaaPbba1"],
  "to": "anti-spam"
}
Respostas:
200

Ações criadas com sucesso

400

Erro ao criar as ações

401

Erro de autenticação

Exemplo de Response:
{
  "message": "Ação enviada com sucesso!",
  "actionsCreated": 3
}
POST
Buscar participante nos grupos das campanhas
Endpoint:
/sendapi/actions/find-participant
Descrição:

Verifica se um número está em algum grupo WhatsApp associado às suas campanhas. A busca cobre todas as campanhas que possuem grupos cadastrados para o usuário; não é necessário informar uma campanha específica. A resposta retorna após o processamento no servidor (ou até o timeout).

Parâmetros do Body (JSON):

accountId (string, obrigatório): ID da conta WhatsApp

phoneNumber (string, obrigatório): Número a buscar (com ou sem formatação; será normalizado)

timeout (number, opcional): Tempo máximo de espera em ms pelo resultado (padrão: 60000)

Exemplo de Request:
{
  "accountId": "pwYE3dPNWV5XtaaaPbba0",
  "phoneNumber": "5511987654321",
  "timeout": 60000
}
Respostas:
200

Resultado da busca (sucesso, não encontrado, erro ou timeout)

400

Dados inválidos ou conta não encontrada

401

API Key inválida ou conta não pertence ao usuário

Exemplo de Response:
{
  "phoneNumber": "5511987654321",
  "found": true,
  "releases": [
    {
      "releaseId": "De3MLuRlkjk8kGLp2cCnN",
      "groupIds": ["120363405635781177@g.us"]
    }
  ]
}

// Em falha processada pelo servidor ou timeout:
{
  "phoneNumber": "5511987654321",
  "found": false,
  "releases": [],
  "error": "Timeout ao aguardar resultado da ação"
}
Velocidades de Envio (shippingSpeed)

Opções de velocidade de entrega para as mensagens:

none: Sem atraso - envio imediato

fast: Rápido - Entre 10 e 20 segundos

normal: Normal - Entre 40 e 60 segundos

slow: Lento - Entre 60 e 120 segundos

custom: Tempo personalizado - Use customShippingSpeed.min e customShippingSpeed.max para definir o intervalo

Tipos de Mensagem (type)

Tipos disponíveis para o endpoint send-message:

extendedTextMessage: Mensagem de texto - requer campo "text". Use "linkPreview": true para gerar preview de links no texto.

imageMessage: Mensagem com imagem - requer campos "url" e opcionalmente "caption"

videoMessage: Mensagem com vídeo - requer campos "url" e opcionalmente "caption"

audioMessage: Mensagem com áudio - requer campos "url" e opcionalmente "caption". Use "ptt": true para enviar como gravação (push-to-talk)

Informações Importantes - Actions

Pontos importantes sobre o uso da API de Actions:

AccountId vs AccountIds: Para rotas de envio de mensagens, você pode usaraccountId (string) para uma única conta ouaccountIds (array) para múltiplas contas.Não é possível usar ambos ao mesmo tempo. É necessário fornecer pelo menos um deles.

Formato de Números: Use o formato completo do WhatsApp com "@s.whatsapp.net" para participantes em group-create, mas apenas o número sem formatação para make-group-admin.

Group IDs: Para make-group-admin, use apenas o ID do grupo sem "@g.us" (ex: "120363420152631339" ao invés de "120363420152631339@g.us").

Seleção de Grupos: Use chooseSpecificGroups como true e forneça uma lista de groupIds para enviar mensagens apenas para grupos específicos. Se false ou omitido, a mensagem será enviada para todos os grupos da campanha.

Autorização: Apenas o proprietário da campanha pode criar ações para ela. Verifique se o releaseId pertence ao usuário autenticado.

Execução: A maioria das ações é assíncrona: o endpoint retorna o ID da ação criada, não o resultado da execução. Exceção: find-participant aguarda o resultado (até timeout) e devolve found, releases e opcionalmente error.

Agendamento: Use o formato ISO 8601 para scheduledTo (ex: "2025-04-21T10:00:00.000Z"). Se não informado ou null, a ação será executada imediatamente.

URLs de Mídia: Para imagens, vídeos e áudios, certifique-se de que as URLs sejam acessíveis publicamente e apontem para arquivos válidos.

Áudio como Gravação (PTT): Para mensagens de áudio, use "ptt": true para enviar como gravação (push-to-talk). Quando true, o áudio aparece como uma gravação de voz no WhatsApp. Quando false ou não informado, o áudio é enviado como arquivo de áudio normal. Disponível nos endpoints send-audio-message e send-message (quando type for "audioMessage").

Códigos de Erro Comuns
400

Bad Request: Dados inválidos ou parâmetros obrigatórios ausentes

401

Unauthorized: API Key inválida ou usuário não autorizado

404

Not Found: Recurso não encontrado

500

Internal Server Error: Erro interno do servidor



## Mensagens

Messages

API para envio direto de mensagens no WhatsApp. Permite enviar mensagens de texto, imagens, vídeos e áudios para números específicos com suporte a agendamento.

POST
Enviar mensagem de texto
Endpoint:
/sendapi/send-text-message/{accountId}
Descrição:

Envia uma mensagem de texto diretamente para um número específico do WhatsApp.

Parâmetros da URL:

accountId (string, obrigatório): ID da conta do WhatsApp

Parâmetros do Body (JSON):

text (string, obrigatório): Texto da mensagem

phoneNumber (string, obrigatório): Número de telefone de destino (formato: 5511987654321)

scheduledTo (string, opcional): Data de agendamento (formato ISO 8601)

timeout (number, opcional): Timeout em milissegundos (padrão: 60000)

Exemplo de Request:
{
  "text": "Olá! Esta é uma mensagem de teste.",
  "phoneNumber": "5511987654321",
  "scheduledTo": "2025-04-21T10:00:00.000Z",
  "timeout": 60000
}
Respostas:
200

Mensagem enviada com sucesso

400

Dados inválidos ou timeout inválido

401

Usuário não autorizado

404

Conta não encontrada ou phoneNumber não informado

Exemplo de Response:
{
  "success": true
}
POST
Enviar mensagem com imagem
Endpoint:
/sendapi/send-image-message/{accountId}
Descrição:

Envia uma mensagem contendo uma imagem para um número específico do WhatsApp.

Parâmetros da URL:

accountId (string, obrigatório): ID da conta do WhatsApp

Parâmetros do Body (JSON):

url (string, obrigatório): URL da imagem a ser enviada

caption (string, opcional): Legenda da imagem

phoneNumber (string, obrigatório): Número de telefone de destino (formato: 5511987654321)

scheduledTo (string, opcional): Data de agendamento (formato ISO 8601)

timeout (number, opcional): Timeout em milissegundos (padrão: 60000)

Exemplo de Request:
{
  "url": "https://exemplo.com/imagem.jpg",
  "caption": "Esta é uma imagem de exemplo",
  "phoneNumber": "5511987654321",
  "scheduledTo": null,
  "timeout": 60000
}
Respostas:
200

Mensagem enviada com sucesso

400

Dados inválidos ou timeout inválido

401

Usuário não autorizado

404

Conta não encontrada ou phoneNumber não informado

Exemplo de Response:
{
  "success": true
}
POST
Enviar mensagem com vídeo
Endpoint:
/sendapi/send-video-message/{accountId}
Descrição:

Envia uma mensagem contendo um vídeo para um número específico do WhatsApp.

Parâmetros da URL:

accountId (string, obrigatório): ID da conta do WhatsApp

Parâmetros do Body (JSON):

url (string, obrigatório): URL do vídeo a ser enviado

caption (string, opcional): Legenda do vídeo

phoneNumber (string, obrigatório): Número de telefone de destino (formato: 5511987654321)

scheduledTo (string, opcional): Data de agendamento (formato ISO 8601)

timeout (number, opcional): Timeout em milissegundos (padrão: 60000)

Exemplo de Request:
{
  "url": "https://exemplo.com/video.mp4",
  "caption": "Este é um vídeo de exemplo",
  "phoneNumber": "5511987654321",
  "scheduledTo": null,
  "timeout": 60000
}
Respostas:
200

Mensagem enviada com sucesso

400

Dados inválidos ou timeout inválido

401

Usuário não autorizado

404

Conta não encontrada ou phoneNumber não informado

Exemplo de Response:
{
  "success": true
}
POST
Enviar mensagem com áudio
Endpoint:
/sendapi/send-audio-message/{accountId}
Descrição:

Envia uma mensagem contendo um áudio para um número específico do WhatsApp.

Parâmetros da URL:

accountId (string, obrigatório): ID da conta do WhatsApp

Parâmetros do Body (JSON):

url (string, obrigatório): URL do áudio a ser enviado

caption (string, opcional): Legenda do áudio

ptt (boolean, opcional): Se true, envia como gravação (push-to-talk). Se false ou não informado, envia como áudio normal

phoneNumber (string, obrigatório): Número de telefone de destino (formato: 5511987654321)

scheduledTo (string, opcional): Data de agendamento (formato ISO 8601)

timeout (number, opcional): Timeout em milissegundos (padrão: 60000)

Exemplo de Request:
{
  "url": "https://exemplo.com/audio.mp3",
  "caption": "Este é um áudio de exemplo",
  "ptt": true,
  "phoneNumber": "5511987654321",
  "scheduledTo": null,
  "timeout": 60000
}
Respostas:
200

Mensagem enviada com sucesso

400

Dados inválidos ou timeout inválido

401

Usuário não autorizado

404

Conta não encontrada ou phoneNumber não informado

Exemplo de Response:
{
  "success": true
}
Formato de Números de Telefone

Formato esperado para o campo phoneNumber:

Formato: [código do país][código da área][número]

Exemplo Brasil: 5511987654321 (55 + 11 + 987654321)

Exemplo EUA: 14155551234 (1 + 415 + 5551234)

Observação: Não incluir símbolos como +, -, (, ), espaços

Tipos de Arquivo Suportados

MIME types automaticamente detectados pela API:

Imagens: image/jpeg, image/png, image/gif, image/webp

Vídeos: video/mp4, video/avi, video/mov, video/webm

Áudios: audio/mpeg, audio/wav, audio/ogg, audio/m4a

Observação: O MIME type é detectado automaticamente pela URL do arquivo. Certifique-se de que a URL seja acessível publicamente.

Timeout e Execução

Como funciona o timeout e a execução das mensagens:

Timeout Padrão: 60.000ms (60 segundos)

Execução: As mensagens são processadas de forma assíncrona

Response: Retorna { success: true } quando a mensagem foi processada com sucesso ou { success: false } em caso de timeout

Agendamento: Use scheduledTo com formato ISO 8601 para agendar o envio. Se null ou não informado, envia imediatamente

Autorização: Apenas o proprietário da conta pode enviar mensagens através dela

Informações Importantes - Messages

Pontos importantes sobre o uso da API de Messages:

URLs de Mídia: Certifique-se de que as URLs sejam acessíveis publicamente e apontem para arquivos válidos

Limitações: Respeite os limites de tamanho do WhatsApp (imagens: 16MB, vídeos: 16MB, áudios: 16MB)

Formato de Data: Use formato ISO 8601 para scheduledTo (ex: "2025-04-21T10:00:00.000Z")

Validação: Números de telefone são validados automaticamente. Números inválidos retornarão erro 404

Autenticação: Utilize Bearer Token no header Authorization para autenticação via API Key

Rate Limiting: Respeite os limites de taxa do WhatsApp para evitar bloqueios de conta

Áudio como Gravação (PTT): Use "ptt": true para enviar áudio como gravação (push-to-talk). Quando true, o áudio aparece como uma gravação de voz no WhatsApp. Quando false ou não informado, o áudio é enviado como arquivo de áudio normal

Códigos de Erro Comuns
400

Bad Request: Dados inválidos ou parâmetros obrigatórios ausentes

401

Unauthorized: API Key inválida ou usuário não autorizado

404

Not Found: Recurso não encontrado

500

Internal Server Error: Erro interno do servidor



## Templates de Mensagens

GET
Buscar todos os templates de mensagem do usuário
Endpoint:
/sendapi/message-templates
Descrição:

Retorna todos os templates de mensagem do usuário autenticado.

Respostas:
200

Lista de templates de mensagem do usuário

400

Erro ao buscar templates

401

Erro de autenticação

Exemplo de Response:
[
  {
    "id": "abc123def456",
    "userId": "user123",
    "title": "Template de boas-vindas",
    "template": [
      {
        "type": "extendedTextMessage",
        "message": {
          "text": "Olá! Bem-vindo!"
        },
        "options": {
          "ephemeralExpiration": -1
        }
      }
    ],
    "folderId": null,
    "tags": [],
    "position": 0,
    "archived": false,
    "intervalRangeType": "none",
    "intervalRange": [1, 1],
    "createdAt": "2025-01-20T10:00:00.000Z",
    "updatedAt": "2025-01-20T10:00:00.000Z"
  }
]
POST
Criar um novo template de mensagem
Endpoint:
/sendapi/message-templates
Descrição:

Cria um novo template de mensagem para o usuário autenticado. O template pode conter múltiplos tipos de mensagens (texto, imagem, vídeo, áudio, etc.) e quantas mensagens forem necessárias.

Parâmetros do Body (JSON):

title (string, obrigatório): Título do template

template (array, obrigatório): Array de mensagens do template. Cada mensagem é um objeto com "type", "message" e "options". Veja detalhes abaixo sobre os tipos de mensagem suportados.

folderId (string, opcional): ID da pasta do template (opcional)

intervalRangeType (string, opcional): Tipo de intervalo entre mensagens (opcional, padrão: "none")

intervalRange (array[number, number], opcional): Intervalo entre mensagens [min, max] em segundos (opcional, padrão: [1, 1])

archived (boolean, opcional): Se o template está arquivado (opcional, padrão: false)

Exemplo de Request:
{
  "title": "Template de boas-vindas",
  "template": [
    {
      "type": "imageMessage",
      "message": {
        "caption": "Bem-vindo!",
        "image": {
          "originalUrl": "url da imagem original",
          "url": "url da imagem"
        },
        "mimetype": "image/webp"
      },
      "options": {
        "ephemeralExpiration": -1,
        "mentionAllParticipants": false
      }
    },
    {
      "type": "extendedTextMessage",
      "message": {
        "text": "Olá! Esta é uma mensagem de boas-vindas."
      },
      "options": {
        "ephemeralExpiration": -1
      }
    }
  ],
  "folderId": null,
  "intervalRangeType": "none",
  "intervalRange": [1, 2],
  "archived": false
}
Respostas:
201

Template criado com sucesso

400

Dados inválidos ou erro ao criar template

401

Erro de autenticação

Exemplo de Response:
{
  "id": "abc123def456"
}
Detalhamento do campo template

O campo template é um array de objetos de mensagem. Cada mensagem deve ter a estrutura com type, message e options.

Exemplo completo:
"template": [
  {
    "type": "imageMessage",
    "message": {
      "caption": "Bem-vindo!",
      "image": {
        "originalUrl": "url da imagem original",
        "url": "url da imagem"
      },
      "mimetype": "image/webp"
    },
    "options": {
      "ephemeralExpiration": -1,
      "mentionAllParticipants": false
    }
  },
  {
    "type": "extendedTextMessage",
    "message": {
      "text": "Olá! Esta é uma mensagem de boas-vindas."
    },
    "options": {
      "ephemeralExpiration": -1
    }
  }
]
Explicação dos campos:

Primeira mensagem (imageMessage):

type (string, obrigatório): Tipo da mensagem. Para imagem, use "imageMessage"

message.caption (string, opcional): Legenda que aparece junto com a imagem. Exemplo: "Bem-vindo!"

message.image.originalUrl (string, obrigatório): URL da imagem original antes de qualquer processamento

message.image.url (string, obrigatório): URL da imagem que será enviada (pode ser uma versão processada/otimizada)

message.mimetype (string, opcional): Tipo MIME da imagem. Exemplos: "image/webp", "image/jpeg", "image/png"

options.ephemeralExpiration (number, opcional): Tempo em segundos para a mensagem desaparecer automaticamente. Use -1 para desabilitar mensagens temporárias (padrão)

options.mentionAllParticipants (boolean, opcional): Se true, menciona todos os participantes do grupo. Use false para não mencionar ninguém

Segunda mensagem (extendedTextMessage):

type (string, obrigatório): Tipo da mensagem. Para texto formatado, use "extendedTextMessage"

message.text (string, obrigatório): Texto da mensagem que será enviado. Exemplo: "Olá! Esta é uma mensagem de boas-vindas."

options.ephemeralExpiration (number, opcional): Tempo em segundos para a mensagem desaparecer automaticamente. Use -1 para desabilitar mensagens temporárias

Terceira mensagem (videoMessage):

{ "type": "videoMessage", "message": { "video": { "url": "url do vídeo" }, "caption": "Legenda do vídeo (opcional)", "mimetype": "video/mp4", "gifPlayback": false, "width": 1280, "height": 720 }, "options": { "ephemeralExpiration": -1 } }

type (string, obrigatório): Tipo da mensagem. Para vídeo, use "videoMessage"

message.video.url (string, obrigatório): URL do arquivo de vídeo que será enviado

message.caption (string, opcional): Legenda que aparece junto com o vídeo

message.mimetype (string, opcional): Tipo MIME do vídeo. Exemplos: "video/mp4", "video/gif", "video/quicktime"

message.gifPlayback (boolean, opcional): Se true, o vídeo será reproduzido como GIF animado (sem som e em loop). Use false para vídeo normal

message.width (number, opcional): Largura do vídeo em pixels

message.height (number, opcional): Altura do vídeo em pixels

options.ephemeralExpiration (number, opcional): Tempo em segundos para a mensagem desaparecer automaticamente. Use -1 para desabilitar mensagens temporárias

Quarta mensagem (audioMessage):

{ "type": "audioMessage", "message": { "audio": { "url": "url do áudio" }, "mimetype": "audio/ogg; codecs=opus", "ptt": false }, "options": { "ephemeralExpiration": -1 } }

type (string, obrigatório): Tipo da mensagem. Para áudio, use "audioMessage"

message.audio.url (string, obrigatório): URL do arquivo de áudio que será enviado

message.mimetype (string, opcional): Tipo MIME do áudio. Exemplos: "audio/ogg; codecs=opus" (nota de voz), "audio/mp4" (música), "audio/mpeg"

message.ptt (boolean, opcional): Se true, envia como nota de voz (push-to-talk). Se false, envia como arquivo de áudio normal. Nota de voz é reproduzida automaticamente quando aberta

options.ephemeralExpiration (number, opcional): Tempo em segundos para a mensagem desaparecer automaticamente. Use -1 para desabilitar mensagens temporárias

Informações gerais:

• O array template pode conter quantas mensagens forem necessárias

• As mensagens serão enviadas na ordem em que aparecem no array

• Você pode misturar diferentes tipos de mensagem no mesmo template (imagem, texto, vídeo, áudio, etc.)

• O intervalo entre mensagens pode ser configurado com os campos intervalRangeType e intervalRange

• Para vídeos, use gifPlayback: true para enviar como GIF animado (sem som, em loop)

• Para áudios, use ptt: true para enviar como nota de voz (reprodução automática) ou ptt: false para arquivo de áudio normal

PUT
Atualizar um template de mensagem
Endpoint:
/sendapi/message-templates/{templateId}
Descrição:

Atualiza um template de mensagem existente. Todos os campos são opcionais - apenas os campos enviados serão atualizados.

Parâmetros da URL:

templateId (string, obrigatório): ID do template de mensagem

Parâmetros do Body (JSON):

title (string, opcional): Título do template

template (array, opcional): Array de mensagens do template. Cada mensagem é um objeto com "type", "message" e "options". Veja detalhes na seção abaixo sobre os tipos de mensagem suportados.

folderId (string, opcional): ID da pasta do template (nullable)

intervalRangeType (string, opcional): Tipo de intervalo entre mensagens (nullable)

intervalRange (array[number, number], opcional): Intervalo entre mensagens [min, max] em segundos (nullable)

archived (boolean, opcional): Se o template está arquivado (nullable)

position (number, opcional): Posição do template

Exemplo de Request:
{
  "title": "Template de boas-vindas atualizado",
  "template": [
    {
      "type": "extendedTextMessage",
      "message": {
        "text": "Olá! Bem-vindo atualizado!"
      },
      "options": {
        "ephemeralExpiration": -1
      }
    }
  ],
  "archived": false
}
Respostas:
200

Template atualizado com sucesso

400

Dados inválidos

401

Erro de autenticação

404

Template não encontrado

Exemplo de Response:
{
  "message": "Template atualizado com sucesso",
  "success": true,
  "id": "abc123def456"
}
DELETE
Deletar um template de mensagem
Endpoint:
/sendapi/message-templates/{templateId}
Descrição:

Deleta permanentemente um template de mensagem. Esta ação não pode ser desfeita.

Parâmetros da URL:

templateId (string, obrigatório): ID do template de mensagem

Respostas:
204

Template deletado com sucesso

400

Erro ao deletar template

401

Erro de autenticação

404

Template não encontrado

Exemplo de Response:
{
  "message": "Template deletado com sucesso"
}
Códigos de Erro Comuns
400

Bad Request: Dados inválidos ou parâmetros obrigatórios ausentes

401

Unauthorized: API Key inválida ou usuário não autorizado

404

Not Found: Recurso não encontrado

500

Internal Server Error: Erro interno do servidor



## Contas

Accounts

API para gerenciamento de contas WhatsApp e Email. Permite criar, consultar, atualizar, deletar e gerenciar a conexão de contas associadas ao usuário.

POST
Criar uma nova conta
Endpoint:
/sendapi/accounts/create
Descrição:

Cria uma nova conta WhatsApp ou Email associada ao usuário autenticado. A conta pode ser vinculada a um projeto específico.

Parâmetros do Body (JSON):

data.name (string, obrigatório): Nome da conta

data.type (string, obrigatório): Tipo da conta (whatsapp, email)

data.provider (string, opcional): Provedor de email (aws-ses, google-api, gmail) - apenas para contas de email

data.senderName (string, opcional): Nome do remetente - apenas para contas de email

data.senderEmail (string, opcional): Email do remetente - apenas para contas de email

projectId (string, opcional): ID do projeto para vincular a conta

Exemplo de Request:
{
  "data": {
    "name": "Minha Conta WhatsApp",
    "type": "whatsapp"
  },
  "projectId": "projeto123"
}
Respostas:
200

Conta criada com sucesso

400

Dados inválidos

401

Usuário não autorizado

404

Projeto não encontrado

Exemplo de Response:
{
  "success": true,
  "id": "conta_id_gerado"
}
GET
Obter contas do usuário
Endpoint:
/sendapi/accounts
Descrição:

Lista todas as contas do usuário autenticado.

Respostas:
200

Contas obtidas com sucesso

401

Usuário não autorizado

400

Erro ao obter contas

Exemplo de Response:
[
  {
    "id": "conta1",
    "name": "Minha Conta WhatsApp",
    "type": "whatsapp",
    "status": "connected",
    "userId": "user123",
    "projectId": "projeto123",
    "createdAt": "2024-01-01T10:00:00Z"
  },
  {
    "id": "conta2",
    "name": "Conta Email",
    "type": "email",
    "status": "processing",
    "userId": "user123",
    "projectId": null,
    "createdAt": "2024-01-02T10:00:00Z"
  }
]
PUT
Atualizar conta
Endpoint:
/sendapi/accounts/{accountId}
Descrição:

Atualiza informações de uma conta existente. Apenas o proprietário pode atualizar.

Parâmetros da URL:

accountId (string, obrigatório): ID da conta a ser atualizada

Parâmetros do Body (JSON):

data.name (string, obrigatório): Nome da conta

data.type (string, obrigatório): Tipo da conta (whatsapp, email)

data.provider (string, opcional): Provedor de email (aws-ses, google-api, gmail) - apenas para contas de email

data.senderName (string, opcional): Nome do remetente - apenas para contas de email

data.senderEmail (string, opcional): Email do remetente - apenas para contas de email

Exemplo de Request:
{
  "data": {
    "name": "Nome Atualizado da Conta",
    "type": "whatsapp"
  }
}
Respostas:
200

Conta atualizada com sucesso

400

Dados inválidos

401

Usuário não autorizado

404

Conta não encontrada

Exemplo de Response:
{
  "success": true,
  "id": "conta_id"
}
DELETE
Remover conta
Endpoint:
/sendapi/accounts/{accountId}
Descrição:

Remove permanentemente uma conta. Apenas o proprietário pode deletar.

Parâmetros da URL:

accountId (string, obrigatório): ID da conta a ser removida

Respostas:
204

Conta removida com sucesso

401

Usuário não autorizado

404

Conta não encontrada

Exemplo de Response:
{
  "success": true
}
Atenção: Esta operação é irreversível. Uma vez deletada, a conta não pode ser recuperada.
POST
Conectar conta
Endpoint:
/sendapi/accounts/connect-account/{accountId}
Descrição:

Inicia o processo de conexão de uma conta WhatsApp. Para contas WhatsApp, gera um QR code para autenticação.

Parâmetros da URL:

accountId (string, obrigatório): ID da conta a ser conectada

Respostas:
200

Processo de conexão iniciado com sucesso

400

Erro ao conectar conta

401

Usuário não autorizado

404

Conta não encontrada

Exemplo de Response:
{
  "success": true,
  "result": {
    "status": "connecting",
    "qrCode": "data:image/png;base64,..."
  }
}
POST
Desconectar conta
Endpoint:
/sendapi/accounts/disconnect-account/{accountId}
Descrição:

Desconecta uma conta WhatsApp, alterando seu status para "disconnected".

Parâmetros da URL:

accountId (string, obrigatório): ID da conta a ser desconectada

Respostas:
204

Conta desconectada com sucesso

400

Erro ao desconectar conta

401

Usuário não autorizado

404

Conta não encontrada

Exemplo de Response:
{
  "success": true
}
GET
Obter dados do QR code
Endpoint:
/sendapi/accounts/{accountId}/qrcode
Descrição:

Obtém informações da conta incluindo QR code para conexão WhatsApp (se disponível).

Parâmetros da URL:

accountId (string, obrigatório): ID da conta

Respostas:
200

Dados obtidos com sucesso

401

Usuário não autorizado

404

Conta não encontrada

Exemplo de Response:
{
  "status": "connecting",
  "id": "conta123",
  "qrCode": "2@ABC123...",
  "image": "data:image/png;base64,...",
  "name": "Minha Conta",
  "jid": "5511987654321@s.whatsapp.net",
  "isAuthenticated": false,
  "attempt": 1
}
GET
Obter imagem do QR code
Endpoint:
/sendapi/accounts/{accountId}/qrcode-image
Descrição:

Gera e retorna uma imagem PNG do QR code com os dados da conta para autenticação WhatsApp.

Parâmetros da URL:

accountId (string, obrigatório): ID da conta

Respostas:
200

Imagem do QR code gerada com sucesso

401

Usuário não autorizado

404

Conta não encontrada

Exemplo de Response:
Content-Type: image/png
[Dados binários da imagem PNG]
Modelo de Dados - Account

Estrutura completa do objeto Account retornado pela API:

id (string): ID único da conta

name (string): Nome da conta

type (string): Tipo da conta (whatsapp, email)

status (string): Status da conta (processing, connecting, connected, disconnected, error)

userId (string): ID do usuário proprietário

projectId (string | null): ID do projeto associado

jid (string): JID do WhatsApp (apenas para contas WhatsApp conectadas)

qrCode (string): Código QR para conexão (quando disponível)

image (string): Imagem base64 do QR code

isAuthenticated (boolean): Se a conta está autenticada

attempt (number): Número de tentativas de conexão

provider (string): Provedor de email (apenas para contas de email)

senderName (string): Nome do remetente (apenas para contas de email)

senderEmail (string): Email do remetente (apenas para contas de email)

Status de Contas

Possíveis status de uma conta:

processing: Conta criada, processando configurações iniciais

connecting: Tentando conectar ao WhatsApp (aguardando QR code)

connected: Conta conectada e funcionando normalmente

disconnected: Conta desconectada pelo usuário ou por erro

error: Erro na conexão ou configuração da conta

Tipos de Conta

Tipos de conta suportados:

whatsapp: Conta WhatsApp para envio de mensagens e gerenciamento de grupos

email: Conta de email para envio de emails (requer configuração de provedor)

Provedores de Email

Provedores suportados para contas de email:

aws-ses: Amazon Simple Email Service

google-api: API do Gmail (Google Workspace)

gmail: Gmail pessoal

Informações Importantes - Accounts

Pontos importantes sobre o uso da API de Accounts:

Propriedade: Apenas o proprietário de uma conta pode visualizar, atualizar ou deletar ela

QR Code WhatsApp: Use os endpoints de QR code para obter o código necessário para conectar uma conta WhatsApp

Conexão: Para contas WhatsApp, use connect-account para iniciar o processo e monitore o status através do endpoint de QR code

Projetos: Contas podem ser associadas a projetos específicos ou permanecer sem projeto (projectId: null)

Validação: Dados são validados usando Zod schema. Verifique os tipos e campos obrigatórios

Rate Limiting: Evite fazer muitas tentativas de conexão seguidas para não sobrecarregar o sistema

Endpoint Deprecated: O endpoint GET /:userId está descontinuado, use GET / para listar contas

Códigos de Erro Comuns
400

Bad Request: Dados inválidos ou parâmetros obrigatórios ausentes

401

Unauthorized: API Key inválida ou usuário não autorizado

404

Not Found: Recurso não encontrado

500

Internal Server Error: Erro interno do servidor



## Números Bloqueados

Block Numbers

API para gerenciamento de números bloqueados. Permite adicionar e listar números no anti-spam.

GET
Obter números bloqueados
Endpoint:
/sendapi/block-numbers
Descrição:

Lista todos os números bloqueados pelo usuário autenticado. Retorna uma lista de números bloqueados no anti-spam.

Respostas:
200

Números bloqueados obtidos com sucesso

400

Erro ao obter os números bloqueados

401

Usuário não autorizado

Exemplo de Response:
[
  "5511987654321",
  "5511987654321",
  "5511999448421",
  "5515612313121"
]
POST
Bloquear um número
Endpoint:
/sendapi/block-numbers
Descrição:

Adiciona um número à lista de bloqueados do usuário no anti-spam.

Parâmetros do Body (JSON):

number (string, obrigatório): Número de telefone a ser bloqueado (formato: 5511987654321)

name (string, obrigatório): Nome ou identificação do número a ser bloqueado

Exemplo de Request:
{
  "number": "5511987654321",
  "name": "João Silva"
}
Respostas:
200

Número bloqueado com sucesso

400

Dados inválidos ou erro ao bloquear o número

401

Usuário não autorizado

Exemplo de Response:
{
  "message": "Número bloqueado com sucesso!",
  "name": "João Silva",
  "number": "5511987654321"
}
Modelo de Dados - Block Number

Estrutura completa do objeto Block Number retornado pela API:

id (string): ID único do bloqueio

number (string): Número de telefone bloqueado (apenas números)

name (string): Nome ou identificação do número

userId (string): ID do usuário que criou o bloqueio

global (boolean): Se o bloqueio é global (sempre false para bloqueios via API)

createdAt (string): Data de criação do bloqueio (formato ISO 8601)

Formato de Números

Formato esperado para números de telefone:

Formato de Entrada: Pode incluir símbolos (+, -, espaços, parênteses)

Formato Armazenado: Apenas números sem formatação

Exemplo de Entrada: "+55 (11) 98765-4321" ou "5511987654321"

Exemplo Armazenado: "5511987654321"

Processamento: A API remove automaticamente todos os caracteres não numéricos

Como Funciona o Bloqueio

Entenda como o sistema de anti-spam funciona:

Sistema Anti-Spam: A API adiciona os números no sistema de anti-spam do usuário

Persistência: Os números permanecem no sistema de anti-spam até serem removidos explicitamente

Informações Importantes - Block Numbers

Pontos importantes sobre o uso da API de Block Numbers:

Validação: Ambos os campos "number" e "name" são obrigatórios ao criar um bloqueio

Normalização: Números são automaticamente normalizados (apenas dígitos) antes do armazenamento

Escopo Individual: Cada usuário gerencia sua própria lista de bloqueios

Limitações: Atualmente não há endpoint para remoção de bloqueios via API (apenas criação e listagem)

Códigos de Erro Comuns
400

Bad Request: Dados inválidos ou parâmetros obrigatórios ausentes

401

Unauthorized: API Key inválida ou usuário não autorizado

404

Not Found: Recurso não encontrado

500

Internal Server Error: Erro interno do servidor



## Verificação de Números

Verification

API para verificação de números de telefone. Permite verificar se um número está bloqueado ou pode receber mensagens para uma campanha específica.

POST
Verificar número
Endpoint:
/sendapi/verify-number
Descrição:

Verifica se um número de telefone está na lista de bloqueios para uma campanha específica. Útil para validar números antes de enviar mensagens.

Parâmetros do Body (JSON):

releaseId (string, obrigatório): ID da campanha para verificação

phoneNumber (string, obrigatório): Número de telefone a ser verificado (formato: 81999999999)

Exemplo de Request:
{
  "releaseId": "7LLztsEGLPNBBBBBBdtItXfc52",
  "phoneNumber": "81999999999"
}
Respostas:
200

Verificação realizada com sucesso

400

Dados inválidos ou erro na verificação

401

Usuário não autorizado

404

Campanha não encontrada

Exemplo de Response:
{
  "response": true
}
Formato de Números para Verificação

Formato esperado para o campo phoneNumber:

Formato: Apenas números, sem código do país

Exemplo Brasil: "11987654321" (sem o 55)

Exemplo Pernambuco: "81999999999" (como no exemplo)

Observação: Não incluir símbolos (+, -, espaços, parênteses)

Processamento: O sistema normaliza automaticamente o número antes da verificação

Tipos de Bloqueio Verificados

Tipos de bloqueio que podem ser detectados:

Bloqueio do Usuário: Números bloqueados pelo proprietário da campanha

Bloqueio Global: Números bloqueados em todo o sistema

Lista de Opt-out: Usuários que solicitaram não receber mensagens

Números Inválidos: Números identificados como inválidos ou problemáticos

Restrições de Campanha: Bloqueios específicos para a campanha em questão

Casos de Uso da Verificação

Situações onde a verificação é útil:

Pré-validação: Verificar números antes de criar campanhas ou enviar mensagens

Limpeza de Lista: Filtrar números válidos de uma lista de contatos

Compliance: Garantir que não enviará para números bloqueados ou opt-out

Otimização: Evitar tentativas de envio para números que falharão

Auditoria: Verificar status de números específicos para relatórios

Integração: Validar números em sistemas externos antes da importação

Informações Importantes - Verification

Pontos importantes sobre o uso da API de Verification:

Autenticação: Requer autenticação via API Key no header Authorization

Escopo da Campanha: A verificação é sempre contextual a uma campanha específica (releaseId)

Performance: Endpoint otimizado para verificações em lote - pode ser chamado múltiplas vezes

Formato de Número: Use apenas números locais sem código do país (diferente dos endpoints de envio)

Cache: Resultados podem ser cacheados temporariamente para melhor performance

Consistência: Use este endpoint antes de enviar mensagens para garantir que o número pode receber

Rate Limiting: Respeite os limites de taxa para evitar bloqueios temporários

Códigos de Erro Comuns
400

Bad Request: Dados inválidos ou parâmetros obrigatórios ausentes

401

Unauthorized: API Key inválida ou usuário não autorizado

404

Not Found: Recurso não encontrado

500

Internal Server Error: Erro interno do servidor


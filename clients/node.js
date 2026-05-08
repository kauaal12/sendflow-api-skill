/**
 * SendFlow SendAPI — minimal Node.js client.
 *
 * Requires Node 18+ (uses global fetch). Zero external dependencies.
 *
 * Usage:
 *   const { SendFlow } = require('./node.js');
 *   const sf = SendFlow.fromCredentials('~/Documents/credentials/sendflow/main.json');
 *   await sf.sendText({ releaseId: '...', accountId: '...', text: 'Olá!' });
 */

const fs = require('fs');
const os = require('os');
const path = require('path');

const DEFAULT_BASE_URL = 'https://sendflow.pro/sendapi';
const DEFAULT_MIN_INTERVAL_MS = 1000;
const DEFAULT_MAX_RETRIES = 5;

class SendFlowError extends Error {
  constructor(message, status) {
    super(message);
    this.name = 'SendFlowError';
    this.status = status;
  }
}

class SendFlow {
  constructor({ apiKey, baseUrl = DEFAULT_BASE_URL, userId = null, minIntervalMs = DEFAULT_MIN_INTERVAL_MS, maxRetries = DEFAULT_MAX_RETRIES }) {
    if (!apiKey) throw new SendFlowError('apiKey is required');
    this.apiKey = apiKey;
    this.baseUrl = baseUrl.replace(/\/$/, '');
    this.userId = userId;
    this.minIntervalMs = minIntervalMs;
    this.maxRetries = maxRetries;
    this._lastCallAt = 0;
  }

  static fromCredentials(filePath) {
    const expanded = filePath.startsWith('~') ? path.join(os.homedir(), filePath.slice(1)) : filePath;
    const cred = JSON.parse(fs.readFileSync(expanded, 'utf8'));
    return new SendFlow({
      apiKey: cred.apiKey,
      baseUrl: cred.baseUrl || DEFAULT_BASE_URL,
      userId: cred.userId,
    });
  }

  static fromEnv() {
    const key = process.env.SENDFLOW_API_KEY;
    if (!key) throw new SendFlowError('SENDFLOW_API_KEY env var not set');
    return new SendFlow({
      apiKey: key,
      baseUrl: process.env.SENDFLOW_BASE_URL || DEFAULT_BASE_URL,
      userId: process.env.SENDFLOW_USER_ID,
    });
  }

  // --- Generic request ---

  async request(method, urlPath, { body = null, params = null, timeoutMs = 30000 } = {}) {
    let url = `${this.baseUrl}${urlPath}`;
    if (params) {
      const qs = new URLSearchParams(params).toString();
      if (qs) url += `?${qs}`;
    }

    const headers = { Authorization: `Bearer ${this.apiKey}` };
    if (body !== null) headers['Content-Type'] = 'application/json';

    for (let attempt = 0; attempt < this.maxRetries; attempt++) {
      await this._throttle();

      const ctrl = new AbortController();
      const timeout = setTimeout(() => ctrl.abort(), timeoutMs);

      let res;
      try {
        res = await fetch(url, {
          method,
          headers,
          body: body !== null ? JSON.stringify(body) : undefined,
          signal: ctrl.signal,
        });
      } finally {
        clearTimeout(timeout);
      }

      const text = await res.text();
      if (res.status === 403 && /Limite/.test(text)) {
        const sleepMs = (2 ** attempt) * 1000 + Math.random() * 1000;
        await new Promise((r) => setTimeout(r, sleepMs));
        continue;
      }
      if (!res.ok) {
        throw new SendFlowError(`${method} ${urlPath} → ${res.status}: ${text.slice(0, 500)}`, res.status);
      }
      try {
        return JSON.parse(text);
      } catch {
        return text;
      }
    }

    throw new SendFlowError(`${method} ${urlPath} — gave up after ${this.maxRetries} retries`);
  }

  async _throttle() {
    const elapsed = Date.now() - this._lastCallAt;
    if (elapsed < this.minIntervalMs) {
      await new Promise((r) => setTimeout(r, this.minIntervalMs - elapsed));
    }
    this._lastCallAt = Date.now();
  }

  // --- Releases ---

  listReleases() { return this.request('GET', '/releases'); }
  getRelease(releaseId) { return this.request('GET', `/releases/${releaseId}`); }

  createRelease({ name, type = 'WhatsRelease', projectId = null }) {
    const body = { name, type };
    if (projectId) body.projectId = projectId;
    return this.request('POST', '/releases', { body });
  }

  getReleaseAnalytics(releaseId) { return this.request('GET', `/releases/${releaseId}/analytics`); }
  getReleaseLeadscoring(releaseId) { return this.request('GET', `/releases/${releaseId}/leadscoring`); }
  downloadLeadscoring(releaseId) { return this.request('GET', `/releases/${releaseId}/leadscoring/download`); }
  getReleaseGroups(releaseId) { return this.request('GET', `/releases/${releaseId}/groups`); }

  // --- Send messages (rate limit: 10 req/s per releaseId) ---

  sendText({ releaseId, text, accountId, accountIds, linkPreview = false, scheduledTo = null, groupIds = null, shippingSpeed = 'normal' }) {
    const body = {
      releaseId,
      messageText: text,
      linkPreview,
      options: { shippingSpeed },
    };
    this._setAccounts(body, accountId, accountIds);
    if (scheduledTo) { body.scheduled = true; body.scheduledTo = scheduledTo; }
    if (groupIds) { body.chooseSpecificGroups = true; body.groupIds = groupIds; }
    return this.request('POST', '/actions/send-text-message', { body });
  }

  sendImage({ releaseId, url, caption = '', accountId, accountIds, scheduledTo = null, groupIds = null, shippingSpeed = 'normal' }) {
    return this._sendMedia('/actions/send-image-message', { releaseId, url, caption, accountId, accountIds, scheduledTo, groupIds, shippingSpeed });
  }

  sendVideo({ releaseId, url, caption = '', accountId, accountIds, scheduledTo = null, groupIds = null, shippingSpeed = 'normal' }) {
    return this._sendMedia('/actions/send-video-message', { releaseId, url, caption, accountId, accountIds, scheduledTo, groupIds, shippingSpeed });
  }

  sendAudio({ releaseId, url, caption = '', accountId, accountIds, scheduledTo = null, groupIds = null, shippingSpeed = 'normal' }) {
    return this._sendMedia('/actions/send-audio-message', { releaseId, url, caption, accountId, accountIds, scheduledTo, groupIds, shippingSpeed });
  }

  _sendMedia(path, { releaseId, url, caption, accountId, accountIds, scheduledTo, groupIds, shippingSpeed }) {
    const body = {
      releaseId,
      url,
      caption,
      options: { shippingSpeed },
    };
    this._setAccounts(body, accountId, accountIds);
    if (scheduledTo) body.scheduledTo = scheduledTo;
    if (groupIds) { body.chooseSpecificGroups = true; body.groupIds = groupIds; }
    return this.request('POST', path, { body });
  }

  _setAccounts(body, accountId, accountIds) {
    if (accountIds && accountIds.length) body.accountIds = accountIds;
    else if (accountId) body.accountId = accountId;
    else throw new SendFlowError('Either accountId or accountIds must be provided');
  }

  // --- Direct 1-to-1 ---

  sendTextDirect({ accountId, phoneNumber, text, scheduledTo = null }) {
    const body = { text, phoneNumber, timeout: 60000 };
    if (scheduledTo) body.scheduledTo = scheduledTo;
    return this.request('POST', `/send-text-message/${accountId}`, { body });
  }

  // --- Accounts ---

  listAccounts() { return this.request('GET', '/accounts'); }

  createAccount({ name, type = 'whatsapp', projectId = null, ...extra }) {
    const body = { data: { name, type, ...extra } };
    if (projectId) body.projectId = projectId;
    return this.request('POST', '/accounts/create', { body });
  }

  connectAccount(accountId) { return this.request('POST', `/accounts/connect-account/${accountId}`); }
  disconnectAccount(accountId) { return this.request('POST', `/accounts/disconnect-account/${accountId}`); }
  getQrCode(accountId) { return this.request('GET', `/accounts/${accountId}/qrcode`); }
  getQrImage(accountId) { return this.request('GET', `/accounts/${accountId}/qrcode-image`); }

  // --- Block / verify ---

  listBlockedNumbers() { return this.request('GET', '/block-numbers'); }
  blockNumber({ number, name }) { return this.request('POST', '/block-numbers', { body: { number, name } }); }

  verifyNumber({ releaseId, phoneNumber }) {
    return this.request('POST', '/verify-number', { body: { releaseId, phoneNumber } });
  }

  // --- Find participant ---

  findParticipant({ accountId, phoneNumber }) {
    return this.request('POST', '/actions/find-participant', { body: { accountId, phoneNumber } });
  }
}

module.exports = { SendFlow, SendFlowError };

// CLI quick test
if (require.main === module) {
  (async () => {
    const sf = SendFlow.fromCredentials('~/Documents/credentials/sendflow/main.json');
    console.log('Releases:', await sf.listReleases());
  })().catch((err) => { console.error(err); process.exit(1); });
}

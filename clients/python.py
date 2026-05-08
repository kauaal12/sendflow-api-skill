"""
SendFlow SendAPI — minimal Python client.

Usage:
    from python import SendFlow
    sf = SendFlow.from_credentials("~/Documents/credentials/sendflow/main.json")
    sf.send_text(account_id="...", release_id="...", text="Olá!")

Includes:
- Bearer auth from credential file
- Polite default rate limit (1 req/s) + exponential backoff on 403 "Limite de operações atingido!"
- Convenience methods for the most common endpoints
- Generic .request() for everything else
"""

from __future__ import annotations

import json
import os
import random
import time
from typing import Any

import requests


class SendFlowError(RuntimeError):
    pass


class RateLimited(SendFlowError):
    pass


class SendFlow:
    DEFAULT_BASE_URL = "https://sendflow.pro/sendapi"
    DEFAULT_MIN_INTERVAL_S = 1.0  # polite default
    DEFAULT_MAX_RETRIES = 5

    def __init__(
        self,
        api_key: str,
        base_url: str = DEFAULT_BASE_URL,
        user_id: str | None = None,
        min_interval_s: float = DEFAULT_MIN_INTERVAL_S,
        max_retries: int = DEFAULT_MAX_RETRIES,
        session: requests.Session | None = None,
    ):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.user_id = user_id
        self.min_interval_s = min_interval_s
        self.max_retries = max_retries
        self._session = session or requests.Session()
        self._last_call_at = 0.0

    @classmethod
    def from_credentials(cls, path: str) -> "SendFlow":
        path = os.path.expanduser(path)
        with open(path) as f:
            cred = json.load(f)
        return cls(
            api_key=cred["apiKey"],
            base_url=cred.get("baseUrl", cls.DEFAULT_BASE_URL),
            user_id=cred.get("userId"),
        )

    @classmethod
    def from_env(cls) -> "SendFlow":
        key = os.environ.get("SENDFLOW_API_KEY")
        if not key:
            raise SendFlowError("SENDFLOW_API_KEY env var not set")
        return cls(
            api_key=key,
            base_url=os.environ.get("SENDFLOW_BASE_URL", cls.DEFAULT_BASE_URL),
            user_id=os.environ.get("SENDFLOW_USER_ID"),
        )

    # --- Generic request ---

    def request(
        self,
        method: str,
        path: str,
        *,
        json_body: Any = None,
        params: dict | None = None,
        timeout_s: float = 30.0,
    ) -> Any:
        url = f"{self.base_url}{path}"
        headers = {"Authorization": f"Bearer {self.api_key}"}

        for attempt in range(self.max_retries):
            self._throttle()
            r = self._session.request(
                method, url,
                headers=headers,
                json=json_body,
                params=params,
                timeout=timeout_s,
            )
            if r.status_code == 403 and "Limite" in r.text:
                sleep_s = (2 ** attempt) + random.random()
                time.sleep(sleep_s)
                continue
            if not r.ok:
                raise SendFlowError(
                    f"{method} {path} → {r.status_code}: {r.text[:500]}"
                )
            try:
                return r.json()
            except ValueError:
                return r.content

        raise RateLimited(f"{method} {path} — gave up after {self.max_retries} retries")

    def _throttle(self):
        elapsed = time.time() - self._last_call_at
        if elapsed < self.min_interval_s:
            time.sleep(self.min_interval_s - elapsed)
        self._last_call_at = time.time()

    # --- Releases (campanhas) ---

    def list_releases(self):
        """GET /releases — rate limit 5min between calls. Cache on the caller side."""
        return self.request("GET", "/releases")

    def get_release(self, release_id: str):
        return self.request("GET", f"/releases/{release_id}")

    def create_release(self, name: str, type_: str = "WhatsRelease", project_id: str | None = None):
        body = {"name": name, "type": type_}
        if project_id:
            body["projectId"] = project_id
        return self.request("POST", "/releases", json_body=body)

    def get_release_analytics(self, release_id: str):
        return self.request("GET", f"/releases/{release_id}/analytics")

    def get_release_leadscoring(self, release_id: str):
        return self.request("GET", f"/releases/{release_id}/leadscoring")

    def download_leadscoring(self, release_id: str) -> bytes:
        return self.request("GET", f"/releases/{release_id}/leadscoring/download")

    def get_release_groups(self, release_id: str):
        return self.request("GET", f"/releases/{release_id}/groups")

    # --- Send messages (rate limit: 10 req/s per releaseId) ---

    def send_text(
        self,
        *,
        release_id: str,
        text: str,
        account_id: str | None = None,
        account_ids: list[str] | None = None,
        link_preview: bool = False,
        scheduled_to: str | None = None,
        group_ids: list[str] | None = None,
        shipping_speed: str = "normal",
    ):
        """POST /actions/send-text-message — broadcast text to a release."""
        body: dict[str, Any] = {
            "releaseId": release_id,
            "messageText": text,
            "linkPreview": link_preview,
            "options": {"shippingSpeed": shipping_speed},
        }
        self._set_accounts(body, account_id, account_ids)
        if scheduled_to:
            body["scheduled"] = True
            body["scheduledTo"] = scheduled_to
        if group_ids is not None:
            body["chooseSpecificGroups"] = True
            body["groupIds"] = group_ids
        return self.request("POST", "/actions/send-text-message", json_body=body)

    def send_image(
        self,
        *,
        release_id: str,
        url: str,
        caption: str = "",
        account_id: str | None = None,
        account_ids: list[str] | None = None,
        scheduled_to: str | None = None,
        group_ids: list[str] | None = None,
        shipping_speed: str = "normal",
    ):
        body: dict[str, Any] = {
            "releaseId": release_id,
            "url": url,
            "caption": caption,
            "options": {"shippingSpeed": shipping_speed},
        }
        self._set_accounts(body, account_id, account_ids)
        if scheduled_to:
            body["scheduledTo"] = scheduled_to
        if group_ids is not None:
            body["chooseSpecificGroups"] = True
            body["groupIds"] = group_ids
        return self.request("POST", "/actions/send-image-message", json_body=body)

    def send_video(self, *, release_id: str, url: str, caption: str = "", **kw):
        return self._send_media("/actions/send-video-message", release_id, url, caption, kw)

    def send_audio(self, *, release_id: str, url: str, caption: str = "", **kw):
        return self._send_media("/actions/send-audio-message", release_id, url, caption, kw)

    def _send_media(self, path: str, release_id: str, url: str, caption: str, kw: dict):
        body = {
            "releaseId": release_id,
            "url": url,
            "caption": caption,
            "options": {"shippingSpeed": kw.get("shipping_speed", "normal")},
        }
        self._set_accounts(body, kw.get("account_id"), kw.get("account_ids"))
        if kw.get("scheduled_to"):
            body["scheduledTo"] = kw["scheduled_to"]
        if kw.get("group_ids") is not None:
            body["chooseSpecificGroups"] = True
            body["groupIds"] = kw["group_ids"]
        return self.request("POST", path, json_body=body)

    @staticmethod
    def _set_accounts(body: dict, account_id, account_ids):
        if account_ids:
            body["accountIds"] = account_ids
        elif account_id:
            body["accountId"] = account_id
        else:
            raise SendFlowError("Either account_id or account_ids must be provided")

    # --- Direct 1-to-1 (no release) ---

    def send_text_direct(self, *, account_id: str, phone_number: str, text: str, scheduled_to: str | None = None):
        body = {"text": text, "phoneNumber": phone_number, "timeout": 60000}
        if scheduled_to:
            body["scheduledTo"] = scheduled_to
        return self.request("POST", f"/send-text-message/{account_id}", json_body=body)

    # --- Accounts ---

    def list_accounts(self):
        return self.request("GET", "/accounts")

    def create_account(self, name: str, type_: str = "whatsapp", project_id: str | None = None, **extra):
        data = {"name": name, "type": type_, **extra}
        body = {"data": data}
        if project_id:
            body["projectId"] = project_id
        return self.request("POST", "/accounts/create", json_body=body)

    def connect_account(self, account_id: str):
        return self.request("POST", f"/accounts/connect-account/{account_id}")

    def disconnect_account(self, account_id: str):
        return self.request("POST", f"/accounts/disconnect-account/{account_id}")

    def get_qr_code(self, account_id: str):
        return self.request("GET", f"/accounts/{account_id}/qrcode")

    def get_qr_image(self, account_id: str) -> bytes:
        return self.request("GET", f"/accounts/{account_id}/qrcode-image")

    # --- Block / verify ---

    def list_blocked_numbers(self):
        return self.request("GET", "/block-numbers")

    def block_number(self, number: str, name: str):
        return self.request("POST", "/block-numbers", json_body={"number": number, "name": name})

    def verify_number(self, release_id: str, phone_number: str):
        return self.request(
            "POST", "/verify-number",
            json_body={"releaseId": release_id, "phoneNumber": phone_number},
        )

    # --- Find participant ---

    def find_participant(self, account_id: str, phone_number: str):
        return self.request(
            "POST", "/actions/find-participant",
            json_body={"accountId": account_id, "phoneNumber": phone_number},
        )


if __name__ == "__main__":
    sf = SendFlow.from_credentials("~/Documents/credentials/sendflow/main.json")
    print("Releases:", sf.list_releases())

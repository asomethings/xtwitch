from __future__ import annotations

from typing import Optional, Type

import httpx
from httpx import Response

from xtwitch import Authorization

__all__ = ['Manager']


class Manager:

    def __init__(self, authorization: Optional[Authorization] = None) -> None:
        self.timeout: int = 3
        self.__authorization = authorization

    def use_auth(self, profile: str) -> Manager:
        auth_profile = Authorization.get(profile_name=profile)
        o = self._clone()
        o.__authorization = auth_profile
        return o

    async def _get(self, url: str, use_oauth: bool = False) -> Response:
        return await httpx.get(f'https://api.twitch.tv/kraken/{url}',
                               headers=self._get_headers(use_oauth),
                               timeout=self.timeout)

    def _get_headers(self, use_oauth: bool) -> dict:
        headers = self._accept_header
        headers.update(self._client_id_header)
        if not use_oauth:
            return headers

        headers.update(self._oauth_token_header)
        return headers

    @property
    def _authorization(self) -> Authorization:
        if not self.__authorization:
            return Authorization.get(Authorization.DEFAULT_PROFILE_NAME)

        return self.__authorization

    @property
    def _accept_header(self) -> dict:
        return dict(Accept='application/vnd.twitchtv.v5+json')

    @property
    def _client_id_header(self) -> dict:
        return {'Client-Id': self._authorization.client_id}

    @property
    def _oauth_token_header(self) -> dict:
        return dict(Authorization=f'OAuth {self._authorization.oauth_token}')

    def _clone(self) -> Manager:
        new_class: Type[Manager] = self.__class__
        return new_class(authorization=self._authorization)

from __future__ import annotations

import re
from collections import OrderedDict
from typing import Optional

from xtwitch.exceptions import ClientImproperlyConfigured, ClientProfileNotFound

__all__ = ['Authorization']


class Authorization:
    DEFAULT_PROFILE_NAME = 'default'
    _AVAILABLE_PROFILES = OrderedDict()

    def __init__(self,
                 *,
                 client_id: Optional[str] = None,
                 oauth_token: Optional[str] = None) -> None:
        self.client_id = client_id
        self.oauth_token = oauth_token

    @property
    def client_id(self) -> str:
        if not self._client_id:
            raise ClientImproperlyConfigured('client_id was not configured properly')

        return self._client_id

    @client_id.setter
    def client_id(self, new_client_id: Optional[str]) -> None:
        if new_client_id is None:
            self._client_id = None
            return

        if not isinstance(new_client_id, str):
            raise ClientImproperlyConfigured("client_id should be supplied as string")

        client_id = re.match(r'[a-z0-9]{30}', new_client_id)
        if not client_id:
            raise ClientImproperlyConfigured('client_id does not match format [a-z0-9]{30}')

        self._client_id = new_client_id

    @property
    def oauth_token(self) -> str:
        if not self._oauth_token:
            raise ClientImproperlyConfigured('oauth_token was not configured properly')

        return self._oauth_token

    @oauth_token.setter
    def oauth_token(self, new_oauth_token: Optional[str]) -> None:
        if new_oauth_token is None:
            self._oauth_token = None
            return

        if not isinstance(new_oauth_token, str):
            raise ClientImproperlyConfigured("oauth_token should be supplied as string")

        # TODO: Add validation for oauth_token
        self._oauth_token = new_oauth_token

    @classmethod
    def add(cls, profile_name: Optional[str] = None, *, client_id: str, oauth_token: str) -> None:
        """Adds authorization profile

        Args:
            profile_name: Optional profile name to specify. If not specified it will be default.
            client_id: Twitch App client id.
            oauth_token: Twitch Users OAuth Token

        Returns:
            None

        Raises:
            ClientImproperlyConfigured
        """
        authorization_credentials = cls(client_id=client_id, oauth_token=oauth_token)
        authorization_profile_name = profile_name or cls.DEFAULT_PROFILE_NAME
        cls._AVAILABLE_PROFILES[authorization_profile_name] = authorization_credentials

    @classmethod
    def remove(cls, profile_name: str) -> None:
        """Removes Authorization Profile

        Args:
            profile_name: Profile name to remove

        Returns:
            None

        Raises:
            ClientProfileNotFound
        """
        if profile_name not in cls._AVAILABLE_PROFILES:
            raise ClientProfileNotFound(f'Could not find profile "{profile_name}"')

        cls._AVAILABLE_PROFILES.pop(profile_name)

    @classmethod
    def get(cls, profile_name: str) -> Authorization:
        profile = cls._AVAILABLE_PROFILES.get(profile_name)
        if not profile:
            raise ClientProfileNotFound(f'Could not find requested profile "{profile_name}"')

        return profile

    @classmethod
    def get_profiles(cls) -> OrderedDict:
        return cls._AVAILABLE_PROFILES

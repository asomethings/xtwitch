from __future__ import annotations

from typing import Optional, Type

from xtwitch import Authorization


class Manager:

    def __init__(self, authorization: Optional[Authorization] = None) -> None:
        self._authorization = authorization

    def use_auth(self, profile: str) -> Manager:
        auth_profile = Authorization.get(profile_name=profile)
        o = self._clone()
        o._authorization = auth_profile
        return o

    def _clone(self) -> Manager:
        new_class: Type[Manager] = self.__class__
        return new_class(authorization=self._authorization)

from xtwitch.exceptions.base import TwitchException

__all__ = ['ClientException', 'ClientImproperlyConfigured', 'ClientProfileNotFound']


class ClientException(TwitchException):
    """
    Base exception for all client exceptions
    """


class ClientImproperlyConfigured(ClientException):
    """
    Client is improperly configured
    """


class ClientProfileNotFound(ClientException):
    """
    Could not find matching profile
    """

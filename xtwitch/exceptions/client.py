from xtwitch.exceptions.base import TwitchException

__all__ = ['ClientException', 'ClientImproperlyConfigured']


class ClientException(TwitchException):
    """
    Base exception for all client exceptions
    """


class ClientImproperlyConfigured(ClientException):
    """
    Client is improperly configured
    """

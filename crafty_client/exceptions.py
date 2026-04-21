class CraftyError(Exception):
    pass


class CraftyAuthError(CraftyError):
    pass


class CraftyPermissionError(CraftyError):
    pass


class CraftyNotFoundError(CraftyError):
    pass


class CraftyNetworkError(CraftyError):
    pass

"""core exceptions for the short links"""

class LinkNotFoundError(Exception):
    pass


class LinkExpiredError(Exception):
    pass # 410

class LinkAlreadyExistsError(Exception):
    pass # custom alias already taken

class InvalidUrlError(Exception):
    pass

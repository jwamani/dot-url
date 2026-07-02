"""exceptions for the user"""

class UserNotFoundError(Exception):
    pass

class InvalidApiKeyError(Exception):
    pass # 429

class RateLimitExceededError(Exception):
    pass

class EmailAlreadyExistsError(Exception):
    def __init__(self, email: str):
        self.email = email
        super().__init__(f"Email '{email}' already exists.")

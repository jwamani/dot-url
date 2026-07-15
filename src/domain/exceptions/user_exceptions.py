"""exceptions for the user"""

class UserNotFoundError(Exception):
    pass

class InvalidApiKeyError(Exception):
    pass # 429

class RateLimitExceededError(Exception):
    def __init__(self, limit: int, window_seconds: int, current_count: int):
        self.limit = limit
        self.window_seconds = window_seconds
        self.current_count = current_count
        super().__init__(f"Rate limit exceeded: {current_count}/{limit} requests in {window_seconds} seconds.")

class EmailAlreadyExistsError(Exception):
    def __init__(self, email: str):
        self.email = email
        super().__init__(f"Email '{email}' already exists.")

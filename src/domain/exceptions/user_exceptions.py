"""exceptions for the user"""

class UserNotFoundError(Exception):
    pass

class InvalidApiKeyError(Exception):
    pass # 429

class RateLimitExceededError(Exception):
    pass


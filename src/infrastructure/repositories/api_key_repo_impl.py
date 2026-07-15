import hashlib
import os

from src.application.interfaces.api_key_gen_repository import IApiKeyGenRepository
from src.infrastructure.config import Settings
# format sk_[environment]_[random_string]

class APIKeyGen(IApiKeyGenRepository):
    def generate(self, length: int = 32) -> str:
        environ = os.getenv("environment")
        if not environ:
            environ = Settings().environment # type: ignore
        if environ == "production":
            env = "live"
        else:
            env = "test"
        
        random_string = os.urandom(length).hex()
        
        return f"sk_{env}_{random_string}"
    
    def hash_key(self, api_key: str) -> str:
        return hashlib.sha256(api_key.encode()).hexdigest()
    
    def verify_key(self, api_key: str, hashed_key: str) -> bool:
        return self.hash_key(api_key) == hashed_key
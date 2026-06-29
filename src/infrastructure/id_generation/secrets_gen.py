from secrets import token_urlsafe

from src.application.interfaces.id_gen_repository import AbstractIdGenerator


class SecretsIdGenerator(AbstractIdGenerator):
    def generate(self, length: int = 6) -> str:
        return token_urlsafe(length)[:length]

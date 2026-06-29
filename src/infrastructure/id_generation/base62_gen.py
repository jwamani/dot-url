import secrets

from src.application.interfaces.id_gen_repository import AbstractIdGenerator

ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


class Base62IdGenerator(AbstractIdGenerator):
    def generate(self, length: int = 6) -> str:
        return "".join(secrets.choice(ALPHABET) for _ in range(length))

from secrets import choice

from src.application.interfaces.id_gen_repository import AbstractIdGenerator

ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz-"


class NanoidIdGenerator(AbstractIdGenerator):
    def generate(self, length: int = 6) -> str:
        return "".join(choice(ALPHABET) for _ in range(length))

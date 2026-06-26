from abc import ABC, abstractmethod

class AbstractIdGenerator(ABC):
    @abstractmethod
    def generate(self, length: int = 6) -> str:
        pass
    
    """-<<>>-
    """
from abc import ABC, abstractmethod


class Religion(ABC):
    """Represents a religion followed by people"""

    @abstractmethod
    def pray(self) -> str:
        """returns the prayer offered to the god they belive in"""

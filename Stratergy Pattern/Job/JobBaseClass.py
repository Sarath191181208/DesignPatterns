from abc import ABC, abstractmethod


class Job(ABC):
    """Represents a job"""
    payment_amount = 0

    @abstractmethod
    def pay(self) -> float:
        """returns the pay offered by the company"""

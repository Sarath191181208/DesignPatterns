from .JobBaseClass import Job


class Job1(Job):
    payment_amount = 10.0

    def pay(self) -> float:
        return self.payment_amount

    def __str__(self) -> str:
        return f"the pay is: {self.payment_amount} "


class Job2(Job):
    payment_amount = 20.0

    def pay(self) -> float:
        return self.payment_amount

    def __str__(self) -> str:
        return f"the pay is: {self.payment_amount} "


class Job3(Job):
    payment_amount = 30.0

    def pay(self) -> float:
        return self.payment_amount

    def __str__(self) -> str:
        return f"the pay is: {self.payment_amount} "

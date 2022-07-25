from .ReligionBaseClass import Religion


class AReligion(Religion):
    god = "God A"

    def pray(self) -> str:
        return "Yay! Paying to "+self.god

    def __str__(self) -> str:
        return self.god


class BReligion(Religion):
    god = "God B"

    def pray(self) -> str:
        return "Hurray! Paying to "+self.god

    def __str__(self) -> str:
        return self.god


class CReligion(Religion):
    god = "God C"

    def pray(self) -> str:
        return "Yep! Paying to "+self.god

    def __str__(self) -> str:
        return self.god

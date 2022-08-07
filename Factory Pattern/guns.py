
from abc import ABC


class Gun(ABC):
    damage: int

    def shoot(self) -> int:
        """returns the damage delt by the gun"""


class Pistol(Gun):
    damage = 20

    def shoot(self) -> int:
        return self.damage


class ShortGun(Gun):
    damage = 30

    def shoot(self) -> int:
        return self.damage


class Sniper(Gun):
    damage = 50

    def shoot(self) -> int:
        return self.damage

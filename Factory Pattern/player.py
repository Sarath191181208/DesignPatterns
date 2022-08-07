from guns import Gun
from typing import Optional


class Player:
    gun: Optional[Gun]

    def shoot(self) -> int:
        if self.gun is None:
            return 0
        else:
            return self.gun.shoot()

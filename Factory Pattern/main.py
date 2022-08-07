from typing import Optional
from enemy import Enemy
from guns import Pistol, Sniper, ShortGun, Gun
from player import Player

gun_types = {
    "Pistol": Pistol(),
    "Sniper": Sniper(),
    "ShortGun": ShortGun(),
}


def gun_factory(gun_name: str) -> Optional[Gun]:
    return gun_types.get(gun_name, None)


def take_input() -> str:
    all_gun_types = ", ".join(gun_types.keys())
    return input(f"Enter the gun type {all_gun_types} q to quit: ").strip()


def main() -> None:
    player = Player()
    enemy = Enemy()

    while True:
        gun_type = take_input()
        if gun_type == 'q':
            break

        player.gun = gun_factory(gun_type)
        attack_damage = player.shoot()
        enemy.take_damage(attack_damage)


if __name__ == "__main__":
    main()

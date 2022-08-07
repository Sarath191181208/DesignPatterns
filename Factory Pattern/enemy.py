
class Enemy:
    def __init__(self) -> None:
        self.health = 100

    def take_damage(self, damage: int) -> None:
        self.health -= damage

        if self.health <= 0:
            print("----------------------")
            print(f"Enemy dead, YOU WIN !")
            print("----------------------")
        else:
            print(f"Enemy health : {self.health}")

#!/usr/bin/env python3

class Plant:
    def __init__(
            self,
            name: str,
            age: int,
            height: float,
            grow_rate: float = 0
            ) -> None:
        self._name = name
        if name == "Rose":
            self._height = 25
            self._age = 30
            self.__grow_rate = 0.3
        elif name == "Sunflower":
            self.__grow_rate = 1.5
            self._height = 80
            self._age = 45
        elif name == "Cactus":
            self.__grow_rate = 0.1
            self._height = 15
            self._age = 120
        elif name == "Bamboo":
            self.__grow_rate = 1
            self._height = 240
            self._age = 600
        elif name == "Cauliflower":
            self.__grow_rate = 0.15
            self._height = 12
            self._age = 60
        else:
            self._age = age
            self._height = height
            self._grow_rate = grow_rate
        print("Plant created:", end=" ")
        self.show()
        print(" ")

    def grow(self) -> float:
        self._height += self._grow_rate
        return (round(self._height, 3))

    def age(self) -> None:
        self._age += 1

    def show(self) -> None:
        print(self)

    def __repr__(self) -> str:
        return (
                f"{self._name}: {round(self._height, 3)}cm, "
                f"{self._age} days old"
        )

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = height
            print(f"Height updated: {self._height} cm")
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._age = age
            print(f"Age updated: {self._age} days")
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def get_height(self) -> float:
        return (self._height)

    def get_age(self) -> int:
        return (self._age)


def ft_garden_security(name: str, age: int, height: float) -> None:
    plant_object = Plant(name, age, height)
    plant_object.set_height(height)
    plant_object.set_age(age)
    print("\nCurrent state:", end=" ")
    plant_object.show()
    new_height = plant_object.get_height()
    new_age = plant_object.get_age()
    print(new_height)
    print(f"{new_age}\n\n")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    ft_garden_security("Rose", -30, -25)
    ft_garden_security("Sunflower", 100, 100)
    ft_garden_security("Cactus", 1, 1)
    ft_garden_security("Bamboo", 0, 0)
    ft_garden_security("Cauliflower", 600, -1)

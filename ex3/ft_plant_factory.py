#!/usr/bin/env python3

class Plant:
    def __init__(
            self,
            name: str,
            age: int,
            height: float,
            grow_rate: float = 0
            ) -> None:
        self.__name = name
        self.__age = age
        self.__height = height
        if name == "Rose":
            self.__grow_rate = 0.3
        elif name == "Sunflower":
            self.__grow_rate = 1.5
        elif name == "Cactus":
            self.__grow_rate = 0.1
        elif name == "Bamboo":
            self.__grow_rate = 1
        elif name == "Cauliflower":
            self.__grow_rate = 0.15
        else:
            self.__grow_rate = grow_rate

    def grow(self) -> float:
        self.__height += self.__grow_rate
        return (round(self.__height, 3))

    def age(self) -> None:
        self.__age += 1

    def show(self) -> None:
        print(self)

    def __repr__(self) -> str:
        return (
                f"{self.__name}: {round(self.__height, 3)}cm, "
                f"{self.__age} days old"
        )


def ft_plant_factory(name: str, age: int, height: float) -> None:
    plant_object = Plant(name, age, height)
    print("Created:", end=" ")
    plant_object.show()


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    ft_plant_factory("Rose", 30, 25)
    ft_plant_factory("Sunflower", 45, 80)
    ft_plant_factory("Cactus", 120, 15)
    ft_plant_factory("Bamboo", 600, 240)
    ft_plant_factory("Cauliflower", 60, 12)

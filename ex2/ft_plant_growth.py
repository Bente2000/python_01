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


def show_grow_age(plant: Plant) -> float:
    plant.show()
    height = plant.grow()
    plant.age()
    return (height)


def ft_plant_growth(name: str, age: int, height: float) -> None:
    plant_object = Plant(name, age, height)
    starting_height = height
    for day in range(8):
        print(f"=== Day {day} ===")
        height = show_grow_age(plant_object)
    growth = round((height - starting_height) * 7/8, 3)
    print(f"Growth this week: {growth}\n")


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    ft_plant_growth("Rose", 30, 25)
    ft_plant_growth("Sunflower", 45, 80)
    ft_plant_growth("Cactus", 120, 15)

#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, age: int, height: int) -> None:
        self.__name = name
        self.__age = age
        self.__height = height

    def show(self) -> None:
        print(self)

    def __repr__(self) -> str:
        return (
                f"{self.__name}: {self.__height}cm tall, "
                f"{self.__age} days old"
        )

    def __str__(self) -> str:
        return self.__repr__()

def ft_garden_data(name: str, age: int, height: int) -> None:
    plant_object = Plant(name, age, height)
    plant_object.show()

def ft_garden_data_2() -> None:
    garden: list[Plant] = []
    garden.append(Plant("Rose", 30, 25))
    garden.append(Plant("Sunflower", 80, 45))
    garden.append(Plant("Cactus", 15, 120))
    print(garden)

if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    ft_garden_data("Rose", 30, 25)
    ft_garden_data("Sunflower", 45, 80)
    ft_garden_data("Cactus", 120, 15)

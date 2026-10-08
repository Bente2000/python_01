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
                f"{self.__name}: {self.__height}cm, {self.__age} days old"
        )


def ft_garden_data(name: str, age: int, height: int) -> None:
    plant_object = Plant(name, age, height)
    plant_object.show()


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    ft_garden_data("Rose", 30, 25)
    ft_garden_data("Sunflower", 45, 80)
    ft_garden_data("Cactus", 120, 15)

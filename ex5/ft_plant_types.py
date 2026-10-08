#!/usr/bin/env python3

from sys import stderr


class Plant:
    def __init__(
        self, name: str, height: float, age: int, grow_rate: float = 0.0
    ) -> None:
        self._name = name
        self._height = 0
        self.set_height(height)
        self._age = 0
        self.set_age(age)
        self._grow_rate = grow_rate

    def grow(self) -> float:
        self._height += self._grow_rate
        return round(self._height, 3)

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
            print(
                f"{self._name}: Error, height can't be negative", file=stderr
            )
            print("Height update rejected", file=stderr)

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._age = age
            print(f"Age updated: {self._age} days")
        else:
            print(f"{self._name}: Error, age can't be negative", file=stderr)
            print("Age update rejected", file=stderr)

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age


class Flower(Plant):
    def __init__(
        self,
        name: str,
        age: int,
        height: float,
        colour: str,
        grow_rate: float = 0.3,
    ) -> None:
        super().__init__(name, height, age, grow_rate=grow_rate)
        self._colour = colour
        self._in_bloom = False

    def __repr__(self) -> str:
        blooming = "is blooming beautifully"
        not_blooming = "has not bloomed yet"
        return (
            f"{super().__repr__()}, a beautiful {self._colour} colour\n"
            f"{self._name} {blooming if self._in_bloom else not_blooming}"
        )

    def get_colour(self) -> str:
        return self._colour

    def bloom(self) -> None:
        self._in_bloom = True


class Tree(Plant):
    def __init__(
        self,
        name: str,
        age: int,
        height: float,
        trunk_diameter: float,
        grow_rate: float = 0.0,
    ) -> None:
        super().__init__(name, height, age, grow_rate=grow_rate)
        self._trunk_diameter = trunk_diameter

    def __repr__(self) -> str:
        return f"{super().__repr__()}, {self._trunk_diameter}cm thick"

    def produce_shade(self) -> None:
        print(
            f"{self._name} tree now produces shade of {self._height}"
            f"cm long and {self._trunk_diameter}cm wide"
        )


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        age: int,
        height: float,
        harvest_season: str,
        grow_rate: float = 0.0,
    ) -> None:
        super().__init__(name, height, age, grow_rate=grow_rate)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def __repr__(self) -> str:
        return (
            f"{super().__repr__()}\nHarvest season: {self._harvest_season}"
            f"\nNutritional value: {self._nutritional_value}"
        )

    def ripen(self) -> None:
        super().grow()
        super().age()
        self._nutritional_value += 1


if __name__ == "__main__":
    rose = Flower("Rose", 30, 25, "yellow", grow_rate=0.3)
    walnut = Tree("Walnut", 40000, 700, 80)
    cauliflower = Vegetable("Cauliflower", 60, 12, "August", grow_rate=1.5)

    Plant("Guava", -6, 0)
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print("\n=== Tree")
    walnut.show()
    print("[asking the walnut tree to produce shade]")
    walnut.produce_shade()
    print("\n=== Vegetable")
    cauliflower.show()
    print("[make cauliflower grow and age for 20 days]")
    for _ in range(20):
        cauliflower.ripen()
    cauliflower.show()

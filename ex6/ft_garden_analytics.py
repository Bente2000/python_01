#!/usr/bin/env python3

from sys import stderr


class Plant:
    class _Statistical_data:
        def __init__(self) -> None:
            self.__age = 0
            self.__grow = 0
            self.__show = 0

        def increment_grow(self) -> None:
            self.__grow += 1

        def increment_age(self) -> None:
            self.__age += 1

        def increment_show(self) -> None:
            self.__show += 1

        def __repr__(self) -> str:
            return (
                f"stats: {self.__grow} grow, {self.__age} age, "
                f"{self.__show} show"
            )

        def show_data(self) -> None:
            print(self)

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        grow_rate: float = 0.0,
    ) -> None:
        self.__name = name
        self.__height = 0
        self.set_height(height)
        self.__age = 0
        self.set_age(age)
        self.__grow_rate = grow_rate
        self.__statistics_manager = self._Statistical_data()

    def grow(self) -> float:
        self.__statistics_manager.increment_grow()
        self.__height += self.__grow_rate
        return round(self.__height, 3)

    def age(self) -> None:
        self.__statistics_manager.increment_age()
        self.__age += 1

    def show(self) -> None:
        self.__statistics_manager.increment_show()
        print(self)

    def show_data(self) -> None:
        self.__statistics_manager.show_data()

    def __repr__(self) -> str:
        return (
            f"{self.__name.capitalize()}: {round(self.__height, 3)}cm tall, "
            f"{self.__age} days old"
        )

    def set_height(self, height: float) -> None:
        if height >= 0:
            self.__height = height
            print(f"Height updated: {self.__height} cm")
        else:
            print(
                f"{self.__name.capitalize()}: Error, height can't be negative",
                file=stderr,
            )
            print("Height update rejected", file=stderr)

    def set_age(self, age: int) -> None:
        if age >= 0:
            self.__age = age
            print(f"Age updated: {self.__age} days")
        else:
            print(
                f"{self.__name.capitalize()}: Error, age can't be negative",
                file=stderr,
            )
            print("Age update rejected", file=stderr)

    def get_height(self) -> float:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def get_name(self) -> str:
        return self.__name

    @staticmethod
    def age_checker(days: int) -> str:
        if days > 365:
            return f"Is {days} days more than a year? -> True"
        else:
            return f"Is {days} days more than a year? -> False"

    @classmethod
    def create_anonymous_plant(cls) -> "Plant":
        return cls("Unknown", 0.0, 0)


class Flower(Plant):
    class _Statistical_data(Plant._Statistical_data):
        def __repr__(self) -> str:
            return f"{super().__repr__()}\nim a flower"

    def __init__(
        self,
        name: str,
        age: int,
        height: float,
        colour: str,
        grow_rate: float = 0.0,
    ) -> None:
        super().__init__(name, height, age, grow_rate=grow_rate)
        self.__statistics_manager = self._Statistical_data()
        self.__colour = colour
        self.__in_bloom = False

    def __repr__(self) -> str:
        blooming = "is blooming beautifully"
        not_blooming = "has not bloomed yet"
        return (
            f"{super().__repr__()}\n"
            f"Colour: a beautiful {self.__colour.capitalize()} colour\n"
            f"{self.get_name().capitalize()} "
            f"{blooming if self.__in_bloom else not_blooming}"
        )

    def get_colour(self) -> str:
        return self.__colour

    def bloom(self) -> None:
        self.__in_bloom = True


class Seed(Flower):
    class _Statistical_data(Plant._Statistical_data):
        def __repr__(self) -> str:
            return f"{super().__repr__()}\nim seeds"

    def __init__(
        self,
        name: str,
        age: int,
        height: float,
        colour: str,
        seeds: int = 0,
        grow_rate: float = 0.0,
    ) -> None:
        super().__init__(name, age, height, colour, grow_rate)
        self.__statistics_manager = self._Statistical_data()
        self.__seeds = seeds
        self.__grow_rate = grow_rate

    def __repr__(self) -> str:
        return f"{super().__repr__()}\nSeeds: {self.__seeds}"

    def grow(self) -> float:
        self.__seeds = round(self.__seeds + 2.10, 3)
        return super().grow()


class Tree(Plant):
    class _Statistical_data(Plant._Statistical_data):
        def __init__(self) -> None:
            super().__init__()
            self.__shade = 0

        def increment_shade(self) -> None:
            self.__shade += 1

        def __repr__(self) -> str:
            return f"{super().__repr__()}\n{self.__shade} shade\nim a tree"

    def __init__(
        self,
        name: str,
        age: int,
        height: float,
        trunk_diameter: float,
        grow_rate: float = 0.0,
    ) -> None:
        super().__init__(name, height, age, grow_rate=grow_rate)
        self.__statistics_manager: Tree._Statistical_data = (
            self._Statistical_data()
        )
        self.__trunk_diameter = trunk_diameter

    def __repr__(self) -> str:
        return f"{super().__repr__()}, {self.__trunk_diameter}cm thick"

    def produce_shade(self) -> None:
        self.__statistics_manager.increment_shade()
        print(
            f"{self.get_name().capitalize()} "
            f"tree now produces shade of {self.get_height()}"
            f"cm long and {self.__trunk_diameter}cm wide"
        )


class Vegetable(Plant):
    class _Statistical_data(Plant._Statistical_data):
        def __repr__(self) -> str:
            return f"{super().__repr__()}\nim a vegetable"

    def __init__(
        self,
        name: str,
        age: int,
        height: float,
        harvest_season: str,
        grow_rate: float = 0.0,
    ) -> None:
        super().__init__(name, height, age, grow_rate=grow_rate)
        self.__statistics_manager = self._Statistical_data()
        self.__harvest_season = harvest_season
        self.__nutritional_value = 0

    def __repr__(self) -> str:
        return (
            f"{super().__repr__()}\nHarvest season: {self.__harvest_season}"
            f"\nNutritional value: {self.__nutritional_value}"
        )

    def ripen(self) -> None:
        super().grow()
        super().age()
        self.__nutritional_value += 1


def display_any_plant(plant: Plant) -> None:
    plant.show_data()


if __name__ == "__main__":
    rose = Flower("Rose", 10, 15, "red", 0.3)
    walnut = Tree("walnut", 40000, 700, 80)
    plant = Plant.create_anonymous_plant()
    sunflower = Seed("Sunflower", 45, 80, "yellow")
    statistical_data = plant._Statistical_data()
    print(sunflower._Plant__name)

    print("=== Garden statistics ===")
    print("=== Check year-old ===")
    print(Plant.age_checker(30))
    print(Plant.age_checker(400))
    print("")

    print("=== Flower")
    rose.show()
    print("[statistics for Rose]")
    # rose_statistics.show_data()
    rose.show_data()
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    rose.show_data()
    print("")

    print("=== Tree")
    walnut.show()
    print("[statistics for walnut tree]")
    walnut.show_data()
    print("[asking the walnut tree to produce shade]")
    walnut.produce_shade()
    print("[statistics for walnut tree]")
    walnut.show_data()
    print("")

    print("=== Seed")
    sunflower.show()
    for _ in range(20):
        sunflower.grow()
        sunflower.age()
    sunflower.show()
    sunflower.show_data()
    sunflower.show_data()

    print("=== Anonymous")
    plant.show()
    print("[statistics for Unknown plant]")
    plant.show_data()
    print("")

    display_any_plant(plant)
    display_any_plant(rose)
    display_any_plant(walnut)
    display_any_plant(sunflower)

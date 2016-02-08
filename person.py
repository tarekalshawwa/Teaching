#!/usr/bin/eng python3


class Person:
    digestive_system_capacity = 3
    exercise_reduction_factor = 0.02
    defecation_reduction_factor = 0.2
    min_weight_factor = 0.4

    def __init__(self, name: str, weight: float, height: float):
        self._name = name
        self._weight = weight
        self._height = height
        self._digestive_system = []

        if self._weight < self.min_weight:
            raise ValueError("Weight must be > {} * height".format(Person.min_weight_factor))

    def eat(self, food_weight: float):
        if not 0.0 < food_weight <= 1.5:
            raise ValueError("Invalid Food Weight. Must be between 0.0 and 1.5")

        if self.is_full:
            raise RuntimeError("{} is full. Can't eat".format(self._name))

        self._weight += food_weight
        self._digestive_system.append(food_weight)

    def exercise(self):
        self._weight -= (self._weight - self.min_weight) * Person.exercise_reduction_factor

    def defecate(self):
        if len(self._digestive_system) == 0:
            raise RuntimeError("No food to defecate!")

        last_eaten_weight = self._digestive_system.pop(0)
        self._weight -= last_eaten_weight * Person.defecation_reduction_factor
        self._weight = max(self._weight, self.min_weight)

    @property
    def is_full(self):
        return len(self._digestive_system) == Person.digestive_system_capacity

    @property
    def name(self):
        return self._name

    @property
    def weight(self):
        return self._weight

    @property
    def height(self):
        return self._height

    @property
    def min_weight(self):
        return Person.min_weight_factor * self._height


def example_usage():
    joe = Person("Joe", 80.0, 175.0)

    # Feed the man
    sandwich_weight = 0.2  # kg
    if not joe.is_full:
        joe.eat(sandwich_weight)

    print('{} weighs {}'.format(joe.name, joe.weight))

    joe.exercise()
    joe.exercise()

    print('{} weighs {}'.format(joe.name, joe.weight))

    joe.defecate()

    try:
        joe.defecate()
    except RuntimeError:
        print('joe needs to eat more!')


if __name__ == '__main__':
    example_usage()
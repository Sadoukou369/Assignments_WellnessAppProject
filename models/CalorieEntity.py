class Meal:
    def __init__(self, items: str, calories: int):
        self.__items = items
        self.__calories = calories

    @property
    def items(self) -> str:
        return self.__items

    @items.setter
    def items(self, value: str):
        self.__items = value

    @property
    def calories(self) -> int:
        return self.__calories

    @calories.setter
    def calories(self, value: int):
        if value > 0:
            self.__calories = value

    def __str__(self):
        return f"Meal/Items: {self.__items}, Calories Consumed: {self.__calories}"


class Workout:
    def __init__(self, details: str, calories: int):
        self.__details = details
        self.__calories = calories

    @property
    def details(self) -> str:
        return self.__details

    @details.setter
    def details(self, value: str):
        self.__details = value

    @property
    def calories(self) -> int:
        return self.__calories

    @calories.setter
    def calories(self, value: int):
        if value > 0:
            self.__calories = value

    def __str__(self):
        return f"Workout: {self.__details}, Calories Burned: {self.__calories}"
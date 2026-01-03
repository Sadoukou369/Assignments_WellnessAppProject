from datetime import date
from models.CalorieEntity import Meal, Workout

class Day:
    def __init__(self, day_date: date):
        self.__date = day_date
        self.__meals = []
        self.__workouts = []

    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, value: date):
        self.__date = value

    @property
    def meals(self) -> list:
        return self.__meals

    @meals.setter
    def meals(self, value: list):
        self.__meals = value

    @property
    def workouts(self) -> list:
        return self.__workouts

    @workouts.setter
    def workouts(self, value: list):
        self.__workouts = value

    def add_meal(self, meal: Meal):
        self.__meals.append(meal)

    def add_workout(self, workout: Workout):
        self.__workouts.append(workout)

    def meal_calories(self) -> int:
        total = 0
        for meal in self.__meals:
            total += meal.calories
        return total

    def workout_calories(self) -> int:
        total = 0
        for workout in self.__workouts:
            total += workout.calories
        return total

    @property
    def net_calories(self) -> int:
        return self.meal_calories() - self.workout_calories()

    def __eq__(self, other) -> bool:
        if isinstance(other, Day):
            return self.__date == other.date
        return False

    def meals_to_string(self) -> str:
        result = ""
        for meal in self.__meals:
            result += f"\t{meal}\n"
        return result

    def workouts_to_string(self) -> str:
        result = ""
        for workout in self.__workouts:
            result += f"\t{workout}\n"
        return result

    def __str__(self):
        result = f"Date: {self.__date}\n"
        result += "Meals:\n"
        if self.__meals:
            result += self.meals_to_string()
        else:
            result += "\n"

        result += "Workouts:\n"
        if self.__workouts:
            result += self.workouts_to_string()
        else:
            result += "\n"

        result += f"Net Calories: {self.net_calories}"
        return result
from models.HealthEntry import HealthEntry
from models.EntryType import MealType, WorkoutType

class Meal(HealthEntry):

    def init(self, description: str, calories: int, meal_type: MealType):
        super().init(description, calories)
        self. meal_type = meal_type

    @property
    def meal_type(self) -> MealType:
        return self.__meal_type

    @meal_type.setter
    def meal_type(self, value: MealType):
        self.meal_type = value

    def str(self) -> str:
        return f"Entry: {self._description}, Calories: {self._calories}, Type: {self.__meal_type}"

class Workout(HealthEntry):

    def init(self, description: str, calories: int, workout_type: WorkoutType):
        super().init(description, calories)
        self.workout_type = workout_type

    @property
    def workout_type(self) -> WorkoutType:
        return self.workout_type

    @workout_type.setter
    def workout_type(self, value: WorkoutType):
        self.workout_type = value

    def str(self) -> str:
        return f"Entry: {self._description}, Calories: {self._calories}, Type: {self.workout_type}"
from models.HealthEntry import HealthEntry
from models.EntryType import MealType, WorkoutType


class Meal(HealthEntry):
    """Represents a meal entry with type classification."""

    def __init__(self, description: str, calories: int, meal_type: MealType):
        """Initialize meal with type."""
        super().__init__(description, calories)
        self._meal_type = meal_type

    @property
    def meal_type(self) -> MealType:
        """Get the meal type."""
        return self._meal_type

    @meal_type.setter
    def meal_type(self, value: MealType):
        """Set the meal type."""
        self._meal_type = value

    def __str__(self) -> str:
        """String representation of meal."""
        return f"Entry: {self._description}, Calories: {self._calories}, Type: {self._meal_type}"

    def get_type_display_name(self) -> str:
        """Get the display name of the meal type."""
        return str(self._meal_type)


class Workout(HealthEntry):
    """Represents a workout entry with type classification."""

    def __init__(self, description: str, calories: int, workout_type: WorkoutType):
        """Initialize workout with type."""
        super().__init__(description, calories)
        self._workout_type = workout_type

    @property
    def workout_type(self) -> WorkoutType:
        """Get the workout type."""
        return self._workout_type

    @workout_type.setter
    def workout_type(self, value: WorkoutType):
        """Set the workout type."""
        self._workout_type = value

    def __str__(self) -> str:
        """String representation of workout."""
        return f"Entry: {self._description}, Calories: {self._calories}, Type: {self._workout_type}"

    def get_type_display_name(self) -> str:
        """Get the display name of the workout type."""
        return str(self._workout_type)
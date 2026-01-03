from models.HealthEntry import HealthEntry
from models.EntryType import MealType, WorkoutType


class Meal(HealthEntry):
    """Represents a meal entry with type classification."""

    def __init__(self, description: str, calories: int, meal_type: MealType):
        """Initialize meal with type."""
        # Call parent constructor with description and calories
        super().__init__(description, calories)
        # Private variable for meal type
        self.__meal_type = meal_type

    @property
    def meal_type(self) -> MealType:
        """Get the meal type."""
        return self.__meal_type

    @meal_type.setter
    def meal_type(self, value: MealType):
        """Set the meal type."""
        self.__meal_type = value

    def __str__(self) -> str:
        """String representation of meal - overrides parent method."""
        # Get the base string from parent and add meal type
        base_str = super().__str__()
        return f"{base_str}, Type: {self.__meal_type}"


class Workout(HealthEntry):
    """Represents a workout entry with type classification."""

    def __init__(self, description: str, calories: int, workout_type: WorkoutType):
        """Initialize workout with type."""
        # Call parent constructor with description and calories
        super().__init__(description, calories)
        # Private variable for workout type
        self.__workout_type = workout_type

    @property
    def workout_type(self) -> WorkoutType:
        """Get the workout type."""
        return self.__workout_type

    @workout_type.setter
    def workout_type(self, value: WorkoutType):
        """Set the workout type."""
        self.__workout_type = value

    def __str__(self) -> str:
        """String representation of workout - overrides parent method."""
        # Get the base string from parent and add workout type
        base_str = super().__str__()
        return f"{base_str}, Type: {self.__workout_type}"
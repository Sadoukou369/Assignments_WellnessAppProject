# models/CalorieEntity.py - Ensure exact formatting
from models.HealthEntry import HealthEntry
from models.EntryType import MealType, WorkoutType


class Meal(HealthEntry):
    """Represents a meal entry with type classification."""

    def __init__(self, description: str, calories: int, meal_type: MealType):
        """Initialize meal with type."""
        super().__init__(description, calories)
        # Use property setter for validation
        self.meal_type = meal_type

    @property
    def meal_type(self) -> MealType:
        """Get the meal type."""
        return self.__meal_type

    @meal_type.setter
    def meal_type(self, value):
        """Set the meal type with validation."""
        if isinstance(value, MealType):
            self.__meal_type = value
        else:
            # Default to SNACK if invalid type
            self.__meal_type = MealType.SNACK

    def __str__(self) -> str:
        """Format exactly like the example: Entry: Eggs + toast, Calories: 410, Type: Breakfast"""
        return f"Entry: {self._description}, Calories: {self._calories}, Type: {self.__meal_type}"


class Workout(HealthEntry):
    """Represents a workout entry with type classification."""

    def __init__(self, description: str, calories: int, workout_type: WorkoutType):
        """Initialize workout with type."""
        super().__init__(description, calories)
        # Use property setter for validation
        self.workout_type = workout_type

    @property
    def workout_type(self) -> WorkoutType:
        """Get the workout type."""
        return self.__workout_type

    @workout_type.setter
    def workout_type(self, value):
        """Set the workout type with validation."""
        if isinstance(value, WorkoutType):
            self.__workout_type = value
        else:
            # Default to OTHER if invalid type
            self.__workout_type = WorkoutType.OTHER

    def __str__(self) -> str:
        """Format exactly like the example: Entry: Morning walk, Calories: 200, Type: Cardio"""
        return f"Entry: {self._description}, Calories: {self._calories}, Type: {self.__workout_type}"
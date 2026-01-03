from enum import Enum


class MealType(Enum):
    """Enumeration for meal types with human-readable display."""

    Breakfast = 1
    Lunch = 2
    Dinner = 3
    Snack = 4

    def __str__(self):
        """Return human-readable string for each enum value."""
        if self == MealType.Breakfast:
            return "Breakfast"
        elif self == MealType.Lunch:
            return "Lunch"
        elif self == MealType.Dinner:
            return "Dinner"
        elif self == MealType.Snack:
            return "Snack"
        else:
            return super().__str__()

    @classmethod
    def from_string(cls, text: str):
        """Convert string to MealType enum."""
        text_lower = text.lower().strip()
        if text_lower == "breakfast":
            return cls.Breakfast
        elif text_lower == "lunch":
            return cls.Lunch
        elif text_lower == "dinner":
            return cls.Dinner
        elif text_lower == "snack":
            return cls.Snack
        else:
            raise ValueError(f"Invalid meal type: {text}")


class WorkoutType(Enum):
    """Enumeration for workout types with human-readable display."""

    Cardio = 1
    Strength = 2
    Flexibility = 3
    High_Intensity = 4
    Group_Fitness = 5
    Other = 6

    def __str__(self):
        """Return human-readable string for each enum value."""
        if self == WorkoutType.Cardio:
            return "Cardio"
        elif self == WorkoutType.Strength:
            return "Strength"
        elif self == WorkoutType.Flexibility:
            return "Flexibility"
        elif self == WorkoutType.High_Intensity:
            return "High Intensity Interval"
        elif self == WorkoutType.Group_Fitness:
            return "Group Fitness Class"
        elif self == WorkoutType.Other:
            return "Other"
        else:
            return super().__str__()

    @classmethod
    def from_string(cls, text: str):
        """Convert string to WorkoutType enum."""
        text_lower = text.lower().strip()
        if text_lower == "cardio":
            return cls.Cardio
        elif text_lower == "strength":
            return cls.Strength
        elif text_lower == "flexibility":
            return cls.Flexibility
        elif text_lower == "high intensity interval" or text_lower == "high intensity":
            return cls.High_Intensity
        elif text_lower == "group fitness class" or text_lower == "group fitness":
            return cls.Group_Fitness
        elif text_lower == "other":
            return cls.Other
        else:
            raise ValueError(f"Invalid workout type: {text}")


# Helper functions for displaying choices
def display_meal_type_menu():
    """Display meal type choices as a numbered menu."""
    print("Select Meal Type:")
    meal_types = list(MealType)
    for i, meal_type in enumerate(meal_types, 1):
        print(f"{i}. {meal_type}")
    return meal_types


def display_workout_type_menu():
    """Display workout type choices as a numbered menu."""
    print("Select Workout Type:")
    workout_types = list(WorkoutType)
    for i, workout_type in enumerate(workout_types, 1):
        print(f"{i}. {workout_type}")
    return workout_types


def get_meal_type_by_index(index: int) -> MealType:
    """Get meal type by menu index (1-based)."""
    meal_types = list(MealType)
    if 1 <= index <= len(meal_types):
        return meal_types[index - 1]
    raise ValueError(f"Invalid meal type index: {index}. Must be between 1 and {len(meal_types)}")


def get_workout_type_by_index(index: int) -> WorkoutType:
    """Get workout type by menu index (1-based)."""
    workout_types = list(WorkoutType)
    if 1 <= index <= len(workout_types):
        return workout_types[index - 1]
    raise ValueError(f"Invalid workout type index: {index}. Must be between 1 and {len(workout_types)}")


# Testing the enums to see if run directly
if __name__ == "__main__":
    print("Testing MealType enum:")
    for meal_type in MealType:
        print(f"  {meal_type.name} -> {meal_type}")

    print("\nTesting WorkoutType enum:")
    for workout_type in WorkoutType:
        print(f"  {workout_type.name} -> {workout_type}")

    print("\nTesting display menus:")
    display_meal_type_menu()
    print()
    display_workout_type_menu()
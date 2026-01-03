# models/EntryType.py - Ensure proper string formatting
from enum import Enum


class MealType(Enum):
    """Enumeration for meal types with human-readable display."""

    BREAKFAST = 1
    LUNCH = 2
    DINNER = 3
    SNACK = 4

    def __str__(self):
        """Return human-readable string for each enum value."""
        if self == MealType.BREAKFAST:
            return "Breakfast"
        elif self == MealType.LUNCH:
            return "Lunch"
        elif self == MealType.DINNER:
            return "Dinner"
        elif self == MealType.SNACK:
            return "Snack"
        else:
            return self.name


class WorkoutType(Enum):
    """Enumeration for workout types with human-readable display."""

    CARDIO = 1
    STRENGTH = 2
    FLEXIBILITY = 3
    HIGH_INTENSITY = 4
    GROUP_FITNESS = 5
    OTHER = 6

    def __str__(self):
        """Return human-readable string for each enum value."""
        if self == WorkoutType.CARDIO:
            return "Cardio"
        elif self == WorkoutType.STRENGTH:
            return "Strength"
        elif self == WorkoutType.FLEXIBILITY:
            return "Flexibility"
        elif self == WorkoutType.HIGH_INTENSITY:
            return "High Intensity Interval"
        elif self == WorkoutType.GROUP_FITNESS:
            return "Group Fitness Class"
        elif self == WorkoutType.OTHER:
            return "Other"
        else:
            return self.name
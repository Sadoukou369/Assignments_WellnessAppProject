# This is to help displaying enum choices to users

from models.CalorieEntity import MealType, WorkoutType

def display_meal_type_choices():
    """Display meal type choices as a numbered menu."""
    print("Select Meal Type:")
    for i, meal_type in enumerate(MealType, 1):
        print(f"{i}. {meal_type.value}")
    return list(MealType)

def display_workout_type_choices():
    """Display workout type choices as a numbered menu."""
    print("Select Workout Type:")
    for i, workout_type in enumerate(WorkoutType, 1):
        print(f"{i}. {workout_type.value}")
    return list(WorkoutType)

def get_meal_type_by_choice(choice: int) -> MealType:
    """Get meal type based on user choice."""
    meal_types = list(MealType)
    if 1 <= choice <= len(meal_types):
        return meal_types[choice - 1]
    return None

def get_workout_type_by_choice(choice: int) -> WorkoutType:
    """Get workout type based on user choice."""
    workout_types = list(WorkoutType)
    if 1 <= choice <= len(workout_types):
        return workout_types[choice - 1]
    return None
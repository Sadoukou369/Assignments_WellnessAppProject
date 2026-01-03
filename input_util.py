# input_util.py - Updated to match PDF error messages
from datetime import date
from models.EntryType import MealType, WorkoutType


# INTEGER VALIDATION

def get_int(num):
    try:
        return int(num)
    except:
        return None


def get_int_range(num, low, high):
    value = get_int(num)

    if value is None:
        return None

    if value < low or value > high:
        return None

    return value


# DATE VALIDATION

def get_date(str_date):
    # Format check: MM/DD/YYYY -> must be length 10 & slashes at 2 and 5
    if len(str_date) != 10 or str_date[2] != "/" or str_date[5] != "/":
        return None

    parts = str_date.split("/")

    if len(parts) != 3:
        return None

    month = get_int(parts[0])
    day = get_int(parts[1])
    year = get_int(parts[2])

    if month is None or day is None or year is None:
        return None

    try:
        return date(year, month, day)
    except:
        return None


# ENUM INPUT HELPERS (matching PDF format)
def prompt_meal_type():
    """Prompt user to select a meal type - matches PDF format."""
    print("Select Meal Type:")
    meal_types = list(MealType)
    for i, meal_type in enumerate(meal_types, 1):
        print(f"{i}. {meal_type}")

    return None  # Let main.py handle the input logic


def prompt_workout_type():
    """Prompt user to select a workout type - matches PDF format."""
    print("Select Workout Type:")
    workout_types = list(WorkoutType)
    for i, workout_type in enumerate(workout_types, 1):
        print(f"{i}. {workout_type}")

    return None  # Let main.py handle the input logic
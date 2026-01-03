# This is the UI for the Health and Wellness system
from input_util import *
import health_data as db
from models.CalorieEntity import Meal, Workout


def prompt_int(prompt):
    while True:
        value = get_int(input(prompt))
        if value is not None:
            return value
        print("Error, enter a valid number.")


def prompt_int_range(prompt, low, high):
    while True:
        value = get_int_range(input(prompt), low, high)
        if value is not None:
            return value
        print(f"Error, enter a valid number between {low} and {high}.")


def prompt_date(prompt):
    while True:
        value = get_date(input(prompt))
        if value is not None:
            return value
        print("Error, enter a valid date.")


def get_meal_type_from_user():
    """Get meal type from user - matches PDF format."""
    from models.EntryType import MealType

    print("Select Meal Type:")
    meal_types = list(MealType)
    for i, meal_type in enumerate(meal_types, 1):
        print(f"{i}. {meal_type}")

    # Choose with validation
    while True:
        choice = get_int(input("\nChoice: "))
        if choice is not None and 1 <= choice <= len(meal_types):
            return meal_types[choice - 1]
        print(f"Error, enter a valid number between 1 and {len(meal_types)}.")


def get_workout_type_from_user():
    """Get workout type from user - matches PDF format."""
    from models.EntryType import WorkoutType

    print("Select Workout Type:")
    workout_types = list(WorkoutType)
    for i, workout_type in enumerate(workout_types, 1):
        print(f"{i}. {workout_type}")

    while True:
        choice = get_int(input("\nChoice: "))
        if choice is not None and 1 <= choice <= len(workout_types):
            return workout_types[choice - 1]
        print(f"Error, enter a valid number between 1 and {len(workout_types)}.")


def add_meal():
    print("## Add Meal Entry ##")

    meal_date = prompt_date("Enter date of meal(MM/DD/YYYY): ")

    items = input("Enter item details: ")
    calories = prompt_int("Enter calories: ")

    meal_type = get_meal_type_from_user()

    # Manage day, create if doesn't exist
    day = db.get_day(meal_date)
    if day is None:
        day = db.add_day(meal_date)

    # Create Meal object with type
    try:
        meal = Meal(items, calories, meal_type)
    except ValueError as e:
        print(f"Error: {e}")
        return

    if db.add_meal(meal_date, meal):
        print("* Entry added in.\n")
    else:
        print("Error, could not add meal.")


def add_workout():
    print("## Add Workout Information ##")

    workout_date = prompt_date("Enter date of workout(MM/DD/YYYY): ")

    details = input("Enter workout details: ")
    burned = prompt_int("Enter calories burned: ")

    workout_type = get_workout_type_from_user()

    day = db.get_day(workout_date)
    if day is None:
        day = db.add_day(workout_date)

    try:
        workout = Workout(details, burned, workout_type)
    except ValueError as e:
        print(f"Error: {e}")
        return

    if db.add_workout(workout_date, workout):
        print("* Workout added in.\n")
    else:
        print("Error, could not add workout.")


def search_date():
    print("## Search for Entry ##")
    search_date = prompt_date("Enter date to search(MM/DD/YYYY): ")

    day = db.get_day(search_date)

    if day is None:
        print("\nSorry, no date information found.")
    else:
        print()  # Empty line before date display
        print(day)
        print()  # Empty line after output


def main():
    while True:
        print("\n### Health and Wellness App ###")
        print("1. Add Meal")
        print("2. Add Workout")
        print("3. Search Date")
        print("4. Exit")
        print()

        choice = prompt_int_range("Choose operation: ", 1, 4)

        if choice == 1:
            add_meal()
        elif choice == 2:
            add_workout()
        elif choice == 3:
            search_date()
        elif choice == 4:
            print("System Exiting...")
            break


if __name__ == "__main__":
    main()
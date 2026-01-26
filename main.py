# This is the UI for the Health and Wellness system
from input_util import *
import health_data as db
from models.CalorieEntity import Meal, Workout
from models.EntryType import MealType, WorkoutType
from datetime import date


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


def modify_meal():
    """Modify an existing meal entry."""
    print("## Modify Meal ##")
    modify_date = prompt_date("Enter date to modify(MM/DD/YYYY): ")

    day = db.get_day(modify_date)
    if day is None:
        print("\nSorry, no date information found.")
        return

    if not day.meals:
        print("\nNo meals found for this date.")
        return

    # List meals for modification
    while True:
        print("# Meal List #")
        for i, meal in enumerate(day.meals, 1):
            print(f"{i}. {meal}")
        print(f"{len(day.meals) + 1}. Exit Day Meal Modification")

        choice = prompt_int_range("\nMeal to modify: ", 1, len(day.meals) + 1)

        if choice == len(day.meals) + 1:
            print()  # Empty line before returning to main menu
            break

        # Modify selected meal
        selected_meal = day.meals[choice - 1]
        modify_meal_attributes(selected_meal)


def modify_meal_attributes(meal):
    """Modify attributes of a specific meal."""
    while True:
        print("# Current Meal #")
        print(meal)
        print("1. Modify Description")
        print("2. Modify Calories")
        print("3. Modify Type")
        print("4. Exit Current Meal Modification")

        choice = prompt_int_range("\nModify Attribute: ", 1, 4)

        if choice == 1:
            new_description = input("Enter new item details: ")
            meal.description = new_description
        elif choice == 2:
            new_calories = prompt_int("Enter new calories: ")
            meal.calories = new_calories
        elif choice == 3:
            print("\nSelect new meal type:")
            meal_types = list(MealType)
            for i, meal_type in enumerate(meal_types, 1):
                print(f"{i}. {meal_type}")

            type_choice = prompt_int_range("\nChoice: ", 1, len(meal_types))
            meal.meal_type = meal_types[type_choice - 1]
        elif choice == 4:
            print("Exiting current meal...")
            print()  # Empty line
            break


def delete_meal():
    """Delete an existing meal entry."""
    print("## Delete Meal ##")
    delete_date = prompt_date("Enter date to delete meal(MM/DD/YYYY): ")

    day = db.get_day(delete_date)
    if day is None:
        print("\nSorry, no date information found.")
        return

    if not day.meals:
        print("\nNo meals found for this date.")
        return

    # List meals for deletion
    while True:
        print("# Meal List #")
        for i, meal in enumerate(day.meals, 1):
            print(f"{i}. {meal}")
        print(f"{len(day.meals) + 1}. Exit Meal Delete")

        choice = prompt_int_range("\nMeal to delete: ", 1, len(day.meals) + 1)

        if choice == len(day.meals) + 1:
            print()  # Empty line before returning to main menu
            break

        # Delete selected meal
        deleted_meal = day.meals.pop(choice - 1)
        print(f"# Meal List #")
        for i, meal in enumerate(day.meals, 1):
            print(f"{i}. {meal}")
        print(f"{len(day.meals) + 1}. Exit Meal Delete")

        if not day.meals:
            print("No more meals left for this date.")
            print()  # Empty line
            break


def modify_workout():
    """Modify an existing workout entry."""
    print("## Modify Workout ##")
    modify_date = prompt_date("Enter date to modify(MM/DD/YYYY): ")

    day = db.get_day(modify_date)
    if day is None:
        print("\nSorry, no date information found.")
        return

    if not day.workouts:
        print("\nNo workouts found for this date.")
        return

    # List workouts for modification
    while True:
        print("# Workout List #")
        for i, workout in enumerate(day.workouts, 1):
            print(f"{i}. {workout}")
        print(f"{len(day.workouts) + 1}. Exit Day Workout Modification")

        choice = prompt_int_range("\nWorkout to modify: ", 1, len(day.workouts) + 1)

        if choice == len(day.workouts) + 1:
            print()  # Empty line before returning to main menu
            break

        # Modify selected workout
        selected_workout = day.workouts[choice - 1]
        modify_workout_attributes(selected_workout)


def modify_workout_attributes(workout):
    """Modify attributes of a specific workout."""
    while True:
        print("# Current Workout #")
        print(workout)
        print("1. Modify Description")
        print("2. Modify Calories")
        print("3. Modify Type")
        print("4. Exit Current Workout Modification")

        choice = prompt_int_range("\nModify Attribute: ", 1, 4)

        if choice == 1:
            new_description = input("Enter new item details: ")
            workout.description = new_description
        elif choice == 2:
            new_calories = prompt_int("Enter new calories: ")
            workout.calories = new_calories
        elif choice == 3:
            print("\nSelect new workout type:")
            workout_types = list(WorkoutType)
            for i, workout_type in enumerate(workout_types, 1):
                print(f"{i}. {workout_type}")

            type_choice = prompt_int_range("\nChoice: ", 1, len(workout_types))
            workout.workout_type = workout_types[type_choice - 1]
        elif choice == 4:
            print("Exiting current workout...")
            print()  # Empty line
            break


def delete_workout():
    """Delete an existing workout entry."""
    print("## Delete Workout ##")
    delete_date = prompt_date("Enter date to delete workout(MM/DD/YYYY): ")

    day = db.get_day(delete_date)
    if day is None:
        print("\nSorry, no date information found.")
        return

    if not day.workouts:
        print("\nNo workouts found for this date.")
        return

    # List workouts for deletion
    while True:
        print("# Workout List #")
        for i, workout in enumerate(day.workouts, 1):
            print(f"{i}. {workout}")
        print(f"{len(day.workouts) + 1}. Exit Workout Delete")

        choice = prompt_int_range("\nWorkout to delete: ", 1, len(day.workouts) + 1)

        if choice == len(day.workouts) + 1:
            print()  # Empty line before returning to main menu
            break

        # Delete selected workout
        deleted_workout = day.workouts.pop(choice - 1)
        print(f"# Workout List #")
        for i, workout in enumerate(day.workouts, 1):
            print(f"{i}. {workout}")
        print(f"{len(day.workouts) + 1}. Exit Workout Delete")

        if not day.workouts:
            print("No more workouts left for this date.")
            print()  # Empty line
            break


def filter_by_date():
    """Filter entries by date range, year, or month."""
    print("## Filter by Date ##")
    print("1. Filter by Year")
    print("2. Filter by Month(in our current year 2025)")
    print("3. Filter by Date Range")

    choice = prompt_int_range("\nFilter operation: ", 1, 3)

    if choice == 1:
        # Filter by year
        year = prompt_int("Enter year to filter: ")
        if year is None:
            print("Invalid year entered.")
            return

        filtered_days = db.filter_by_year(year)
        if not filtered_days:
            print(f"\nNo data found for year {year}.")
            return

        # Sort days by date
        filtered_days.sort(key=lambda day: day.date)

        print(f"\n* Days in {year}")
        total_net_calories = 0

        for day in filtered_days:
            print()
            print(day)
            total_net_calories += day.net_calories

        print(f"\nNet calories for range: {total_net_calories}")

    elif choice == 2:
        # Filter by month (in current year 2025)
        month = prompt_int_range("Enter month to filter: ", 1, 12)
        if month is None:
            return

        filtered_days = db.filter_by_month(month, 2025)
        if not filtered_days:
            month_names = ["January", "February", "March", "April", "May", "June",
                           "July", "August", "September", "October", "November", "December"]
            month_name = month_names[month - 1]
            print(f"\nNo data found for {month_name} 2025.")
            return

        # Sort days by date
        filtered_days.sort(key=lambda day: day.date)

        month_names = ["January", "February", "March", "April", "May", "June",
                       "July", "August", "September", "October", "November", "December"]
        month_name = month_names[month - 1]
        print(f"\n* Days in {month_name}")
        total_net_calories = 0

        for day in filtered_days:
            print()
            print(day)
            total_net_calories += day.net_calories

        print(f"\nNet calories for range: {total_net_calories}")

    elif choice == 3:
        # Filter by date range
        while True:
            start_date = prompt_date("Enter start date: ")
            if start_date is None:
                print("Invalid start date.")
                continue

            end_date = prompt_date("Enter end date: ")
            if end_date is None:
                print("Invalid end date.")
                continue

            if start_date > end_date:
                print("* Error, start date must come before end date.")
                continue

            break

        filtered_days = db.filter_by_date_range(start_date, end_date)
        if not filtered_days:
            print(f"\nNo data found between {start_date} and {end_date}.")
            return

        # Sort days by date
        filtered_days.sort(key=lambda day: day.date)

        print(f"\n* Days between {start_date} and {end_date}")
        total_net_calories = 0

        for day in filtered_days:
            print()
            print(day)
            total_net_calories += day.net_calories

        print(f"\nNet calories for range: {total_net_calories}")


def main():
    # Generate test data at startup
    db.generate_test_data()

    while True:
        print("\n### Health and Wellness App ###")
        print("1. Add Meal")
        print("2. Add Workout")
        print("3. Search Date")
        print("4. Modify Meal")
        print("5. Delete Meal")
        print("6. Modify Workout")
        print("7. Delete Workout")
        print("8. Filter By Date")
        print("9. Exit")
        print()

        choice = prompt_int_range("Choose operation: ", 1, 9)

        if choice == 1:
            add_meal()
        elif choice == 2:
            add_workout()
        elif choice == 3:
            search_date()
        elif choice == 4:
            modify_meal()
        elif choice == 5:
            delete_meal()
        elif choice == 6:
            modify_workout()
        elif choice == 7:
            delete_workout()
        elif choice == 8:
            filter_by_date()
        elif choice == 9:
            print("System Exiting...")
            break


if __name__ == "__main__":
    main()
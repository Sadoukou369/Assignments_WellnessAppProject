'''
    INFO 1501 - Python I
    Welcome to the Health and Wellness System
    You will be working on this throughout the course and adding to it

    Please read instructions for each assignment clearly and don't go beyond the functionality
    required as we will be adding more each week.

    Make sure to merge branches and create new branches for each week's assignment.
'''

# This is the UI for the Health and Wellness system

# global dictionaries for meal and workout
# keys are date - in string format - for now
mealTracker = {}
workoutTracker = {}

from input_util import *
import health_data as db


# INPUT HELPERS

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


# FEATURE FUNCTIONS

def add_meal():
    print("## Add Meal Entry ##")
    meal_date = prompt_date("Enter date of meal(MM/DD/YYYY): ")
    items = input("Enter item details: ")
    calories = prompt_int("Enter calories: ")

    if db.add_meal(meal_date, {"items": items, "calories": calories}):
        print("* Entry added in.")
    else:
        print("Error, date entry already added in, try modifying it.")


def add_workout():
    print("## Add Workout Information ##")
    workout_date = prompt_date("Enter date of workout(MM/DD/YYYY): ")
    details = input("Enter workout details: ")
    burned = prompt_int("Enter calories burned: ")

    if db.add_workout(workout_date, {"details": details, "calories": burned}):
        print("* Workout added in.")
    else:
        print("Error, workout already added in, modify if needed.")


def search_date():
    print("## Search for Entry ##")
    search_date = prompt_date("Enter date to search(MM/DD/YYYY): ")

    meal = db.get_meal(search_date)
    workout = db.get_workout(search_date)

    print("\nMeals:")
    if meal is None:
        print("None")
        meal_cal = 0
    else:
        print("Meal Items:", meal["items"])
        print("Meal Calories:", meal["calories"])
        meal_cal = meal["calories"]

    print("\nWorkout:")
    if workout is None:
        print("None")
        workout_cal = 0
    else:
        print("Details:", workout["details"])
        print("Calories Burned:", workout["calories"])
        workout_cal = workout["calories"]

    difference = meal_cal - workout_cal
    print(f"\nCalorie Difference: {difference:+}")


# MAIN LOOP

def main():
    while True:
        print("\n### Health and Wellness App ###")
        print("1. Add Meal")
        print("2. Add Workout")
        print("3. Search Date")
        print("4. Exit")

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

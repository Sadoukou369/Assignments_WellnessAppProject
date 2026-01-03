'''
    INFO 1501 - Python I
    Welcome to the Health and Wellness System
    You will be working on this throughout the course and adding to it

    Please read instructions for each assignment clearly and don't go beyond the functionality
    required as we will be adding more each week.

    Make sure to merge branches and create new branches for each week's assignment.
'''

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

# Function will be added next time
def add_meal():
    print("## Add Meal Entry ##")
    meal_date = prompt_date("Enter date of meal(MM/DD/YYYY): ")

    # Managing day, if does not exist create it
    day = db.get_day(meal_date)
    if day is None:
        day = db.add_day(meal_date)

    items = input("Enter item details: ")
    calories = prompt_int("Enter calories: ")

    # Creating Meal object
    meal = Meal(items, calories)

    if db.add_meal(meal_date, meal):
        print("* Entry added in.")
    else:
        print("Error, could not add meal.")

def add_workout():
    print("## Add Workout Information ##")
    workout_date = prompt_date("Enter date of workout(MM/DD/YYYY): ")

    day = db.get_day(workout_date)
    if day is None:
        day = db.add_day(workout_date)

    details = input("Enter workout details: ")
    burned = prompt_int("Enter calories burned: ")

    # Creating Workout object
    workout = Workout(details, burned)

    if db.add_workout(workout_date, workout):
        print("* Workout added in.")
    else:
        print("Error, could not add workout.")

def search_date():
    print("## Search for Entry ##")
    search_date = prompt_date("Enter date to search(MM/DD/YYYY): ")

    day = db.get_day(search_date)

    if day is None:
        print("\nSorry, no date information found.")
    else:
        print()
        print(day)

# Main Loop
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

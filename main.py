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

def add_meal():
    print("## Add Meal Entry ##")
    date = input("Enter date of meal (MM/DD/YYYY): ")
    details = input("Enter item details: ")
    calories = int(input("Enter calories: "))

    mealTracker[date] = {"items": details, "calories": calories}


def add_workout():
    print("## Add Workout Information ##")
    date = input("Enter date of workout(MM/DD/YYYY): ")
    details = input("Enter workout details: ")
    burned = int(input("Enter calories burned: "))

    # store in workoutTracker
    workoutTracker[date] = {"details": details, "burned": burned}


def search_date():
    print("## Search for Entry ##")
    searchDate = input("Enter date to search(MM/DD/YYYY): ")

    print("\nMeals:")

    if searchDate in mealTracker:
        print("Meal Items:", mealTracker[searchDate]["items"])
        print("Meal Calories:", mealTracker[searchDate]["calories"])
        meal_cal = mealTracker[searchDate]["calories"]
    else:
        print("None")
        meal_cal = 0

    print("\nWorkout:")

    if searchDate in workoutTracker:
        print("Details:", workoutTracker[searchDate]["details"])
        print("Calories Burned:", workoutTracker[searchDate]["burned"])
        workout_cal = workoutTracker[searchDate]["burned"]
    else:
        print("None")
        workout_cal = 0

    difference = meal_cal - workout_cal

    print(f"\nCalorie Difference: {difference:+}")


def main():
    while True:
        print("\n### Health and Wellness App ###")
        print("1. Add Meal")
        print("2. Add Workout")
        print("3. Search Date")
        print("4. Exit")

        choice = int(input("Choose operation: "))

        while choice < 1 or choice > 4:
            print("Invalid selection. Please choose a number between 1 and 4.")
            choice = int(input("Choose operation: "))

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

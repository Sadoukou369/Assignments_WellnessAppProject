from models.DateEntity import Day
from models.CalorieEntity import Meal, Workout
from datetime import date
from models.EntryType import MealType, WorkoutType

# Dictionary to store Day objects
health_data = {}


# Adding Day
def add_day(day_date: date):
    if day_date in health_data:
        return None
    new_day = Day(day_date)
    health_data[day_date] = new_day
    return new_day


# Adding Entries
def add_meal(meal_date: date, meal: Meal):
    if meal_date in health_data:
        day = health_data[meal_date]
        day.add_meal(meal)
        return True
    return False


def add_workout(workout_date: date, workout: Workout):
    if workout_date in health_data:
        day = health_data[workout_date]
        day.add_workout(workout)
        return True
    return False


# Searching Entries
def get_day(entry_date: date):
    if entry_date in health_data:
        return health_data[entry_date]
    return None


# Delete functions
def delete_meal(entry_date: date, meal_index: int):
    day = get_day(entry_date)
    if day and 0 <= meal_index < len(day.meals):
        day.meals.pop(meal_index)
        return True
    return False


def delete_workout(entry_date: date, workout_index: int):
    day = get_day(entry_date)
    if day and 0 <= workout_index < len(day.workouts):
        day.workouts.pop(workout_index)
        return True
    return False


# Filter functions by comprehensions
def filter_by_year(year: int):
    """Return all days in the given year using comprehension."""
    # Using list comprehension to filter days by year
    return [day for day in health_data.values() if day.date.year == year]


def filter_by_month(month: int, year: int = None):
    """Return all days in the given month using comprehension."""
    if year is None:
        year = date.today().year
    # Use of list comprehension to Filter days by month and year
    return [day for day in health_data.values()
            if day.date.year == year and day.date.month == month]


def filter_by_date_range(start_date: date, end_date: date):
    """Return all days between start_date and end_date using comprehension."""
    # Use of  list comprehension to filter days within date range
    return [day for day in health_data.values()
            if start_date <= day.date <= end_date]


def get_all_days():
    """Get all days for testing."""
    return list(health_data.values())


def clear_data():
    """Clear all data (for testing)."""
    health_data.clear()


def generate_test_data():
    """Generate test data for the application."""
    # Clear existing data first
    clear_data()

    # Testing data for 2025 (November and December)
    test_data_2025 = [
        # November 2025
        (date(2025, 11, 3), [
            Meal("Oatmeal + berries", 320, MealType.BREAKFAST),
            Meal("Turkey sandwich", 540, MealType.LUNCH),
            Meal("Chicken stir-fry", 720, MealType.DINNER)
        ], [
             Workout("Walking - 20 min", 90, WorkoutType.CARDIO),
             Workout("Light strength training - 25 min", 320, WorkoutType.STRENGTH)
         ]),

        (date(2025, 11, 5), [
            Meal("Chicken caesar salad", 480, MealType.LUNCH),
            Meal("Salmon + rice", 760, MealType.DINNER)
        ], [
             Workout("Walking - 30 min", 130, WorkoutType.CARDIO)
         ]),

        (date(2025, 11, 7), [
            Meal("Burrito bowl", 650, MealType.LUNCH),
            Meal("Greek yogurt", 180, MealType.SNACK),
            Meal("Spaghetti + meat sauce", 820, MealType.DINNER)
        ], [
             Workout("Walking - 40 min", 170, WorkoutType.CARDIO),
             Workout("Bike cardio - 30 min", 335, WorkoutType.CARDIO)
         ]),

        (date(2025, 11, 9), [
            Meal("Eggs + toast", 410, MealType.BREAKFAST),
            Meal("Soup + bread", 520, MealType.LUNCH),
            Meal("Protein bar", 220, MealType.SNACK),
            Meal("Tacos", 780, MealType.DINNER)
        ], [
             Workout("Walking - 50 min", 210, WorkoutType.CARDIO)
         ]),

        (date(2025, 11, 12), [
            Meal("Smoothie (banana + peanut butter)", 450, MealType.BREAKFAST),
            Meal("Chicken wrap", 560, MealType.LUNCH),
            Meal("Steak + potatoes", 900, MealType.DINNER)
        ], [
             Workout("Walking - 60 min", 250, WorkoutType.CARDIO),
             Workout("Group fitness class - 45 min", 435, WorkoutType.GROUP_FITNESS)
         ]),

        (date(2025, 11, 14), [
            Meal("Oatmeal + berries", 320, MealType.BREAKFAST),
            Meal("Turkey sandwich", 540, MealType.LUNCH),
            Meal("Chicken stir-fry", 720, MealType.DINNER)
        ], [
             Workout("Walking - 20 min", 90, WorkoutType.CARDIO)
         ]),

        (date(2025, 11, 16), [
            Meal("Chicken caesar salad", 480, MealType.LUNCH),
            Meal("Salmon + rice", 760, MealType.DINNER)
        ], [
             Workout("Walking - 30 min", 130, WorkoutType.CARDIO),
             Workout("Yoga / stretching - 30 min", 400, WorkoutType.FLEXIBILITY)
         ]),

        (date(2025, 11, 18), [
            Meal("Burrito bowl", 650, MealType.LUNCH),
            Meal("Greek yogurt", 180, MealType.SNACK),
            Meal("Spaghetti + meat sauce", 820, MealType.DINNER)
        ], [
             Workout("Walking - 40 min", 170, WorkoutType.CARDIO)
         ]),

        (date(2025, 11, 21), [
            Meal("Eggs + toast", 410, MealType.BREAKFAST),
            Meal("Soup + bread", 520, MealType.LUNCH),
            Meal("Protein bar", 220, MealType.SNACK),
            Meal("Tacos", 780, MealType.DINNER)
        ], [
             Workout("Walking - 50 min", 210, WorkoutType.CARDIO),
             Workout("HIIT intervals - 20 min", 680, WorkoutType.HIGH_INTENSITY)
         ]),

        (date(2025, 11, 24), [
            Meal("Smoothie (banana + peanut butter)", 450, MealType.BREAKFAST),
            Meal("Chicken wrap", 560, MealType.LUNCH),
            Meal("Steak + potatoes", 900, MealType.DINNER)
        ], [
             Workout("Walking - 60 min", 250, WorkoutType.CARDIO)
         ]),

        # December 2025
        (date(2025, 12, 1), [
            Meal("Oatmeal + berries", 320, MealType.BREAKFAST),
            Meal("Turkey sandwich", 540, MealType.LUNCH),
            Meal("Chicken stir-fry", 720, MealType.DINNER)
        ], [
             Workout("Walking - 20 min", 90, WorkoutType.CARDIO),
             Workout("Light strength training - 25 min", 320, WorkoutType.STRENGTH)
         ]),

        (date(2025, 12, 3), [
            Meal("Chicken caesar salad", 480, MealType.LUNCH),
            Meal("Salmon + rice", 760, MealType.DINNER)
        ], [
             Workout("Walking - 30 min", 130, WorkoutType.CARDIO)
         ]),

        (date(2025, 12, 5), [
            Meal("Burrito bowl", 650, MealType.LUNCH),
            Meal("Greek yogurt", 180, MealType.SNACK),
            Meal("Spaghetti + meat sauce", 820, MealType.DINNER)
        ], [
             Workout("Walking - 40 min", 170, WorkoutType.CARDIO),
             Workout("Bike cardio - 30 min", 335, WorkoutType.CARDIO)
         ]),

        (date(2025, 12, 8), [
            Meal("Eggs + toast", 410, MealType.BREAKFAST),
            Meal("Soup + bread", 520, MealType.LUNCH),
            Meal("Protein bar", 220, MealType.SNACK),
            Meal("Tacos", 780, MealType.DINNER)
        ], [
             Workout("Walking - 50 min", 210, WorkoutType.CARDIO)
         ]),

        (date(2025, 12, 10), [
            Meal("Smoothie (banana + peanut butter)", 450, MealType.BREAKFAST),
            Meal("Chicken wrap", 560, MealType.LUNCH),
            Meal("Steak + potatoes", 900, MealType.DINNER)
        ], [
             Workout("Walking - 60 min", 250, WorkoutType.CARDIO),
             Workout("Group fitness class - 45 min", 435, WorkoutType.GROUP_FITNESS)
         ]),

        (date(2025, 12, 13), [
            Meal("Oatmeal + berries", 320, MealType.BREAKFAST),
            Meal("Turkey sandwich", 540, MealType.LUNCH),
            Meal("Chicken stir-fry", 720, MealType.DINNER)
        ], [
             Workout("Walking - 20 min", 90, WorkoutType.CARDIO)
         ]),
    ]

    # Add 2026 data for testing year filter
    test_data_2026 = [
        (date(2026, 1, 2), [
            Meal("Oatmeal + berries", 320, MealType.BREAKFAST),
            Meal("Turkey sandwich", 540, MealType.LUNCH),
            Meal("Chicken stir-fry", 720, MealType.DINNER)
        ], [
             Workout("Walking - 20 min", 90, WorkoutType.CARDIO),
             Workout("Light strength training - 25 min", 320, WorkoutType.STRENGTH)
         ]),

        (date(2026, 1, 3), [
            Meal("Chicken caesar salad", 480, MealType.LUNCH),
            Meal("Salmon + rice", 760, MealType.DINNER)
        ], [
             Workout("Walking - 30 min", 130, WorkoutType.CARDIO)
         ]),

        (date(2026, 1, 5), [
            Meal("Burrito bowl", 650, MealType.LUNCH),
            Meal("Greek yogurt", 180, MealType.SNACK),
            Meal("Spaghetti + meat sauce", 820, MealType.DINNER)
        ], [
             Workout("Walking - 40 min", 170, WorkoutType.CARDIO),
             Workout("Bike cardio - 30 min", 335, WorkoutType.CARDIO)
         ]),

        (date(2026, 1, 7), [
            Meal("Eggs + toast", 410, MealType.BREAKFAST),
            Meal("Soup + bread", 520, MealType.LUNCH),
            Meal("Protein bar", 220, MealType.SNACK),
            Meal("Tacos", 780, MealType.DINNER)
        ], [
             Workout("Walking - 50 min", 210, WorkoutType.CARDIO)
         ]),

        (date(2026, 1, 9), [
            Meal("Smoothie (banana + peanut butter)", 450, MealType.BREAKFAST),
            Meal("Chicken wrap", 560, MealType.LUNCH),
            Meal("Steak + potatoes", 900, MealType.DINNER)
        ], [
             Workout("Walking - 60 min", 250, WorkoutType.CARDIO),
             Workout("Group fitness class - 45 min", 435, WorkoutType.GROUP_FITNESS)
         ]),

        (date(2026, 1, 12), [
            Meal("Oatmeal + berries", 320, MealType.BREAKFAST),
            Meal("Turkey sandwich", 540, MealType.LUNCH),
            Meal("Chicken stir-fry", 720, MealType.DINNER)
        ], [
             Workout("Walking - 20 min", 90, WorkoutType.CARDIO)
         ]),

        (date(2026, 1, 14), [
            Meal("Chicken caesar salad", 480, MealType.LUNCH),
            Meal("Salmon + rice", 760, MealType.DINNER)
        ], [
             Workout("Walking - 30 min", 130, WorkoutType.CARDIO),
             Workout("Yoga / stretching - 30 min", 400, WorkoutType.FLEXIBILITY)
         ]),

        (date(2026, 1, 18), [
            Meal("Burrito bowl", 650, MealType.LUNCH),
            Meal("Greek yogurt", 180, MealType.SNACK),
            Meal("Spaghetti + meat sauce", 820, MealType.DINNER)
        ], [
             Workout("Walking - 40 min", 170, WorkoutType.CARDIO)
         ]),

        (date(2026, 1, 21), [
            Meal("Eggs + toast", 410, MealType.BREAKFAST),
            Meal("Soup + bread", 520, MealType.LUNCH),
            Meal("Protein bar", 220, MealType.SNACK),
            Meal("Tacos", 780, MealType.DINNER)
        ], [
             Workout("Walking - 50 min", 210, WorkoutType.CARDIO),
             Workout("HIIT intervals - 20 min", 680, WorkoutType.HIGH_INTENSITY)
         ]),

        (date(2026, 1, 27), [
            Meal("Smoothie (banana + peanut butter)", 450, MealType.BREAKFAST),
            Meal("Chicken wrap", 560, MealType.LUNCH),
            Meal("Steak + potatoes", 900, MealType.DINNER)
        ], [
             Workout("Walking - 60 min", 250, WorkoutType.CARDIO)
         ]),
    ]

    # Add all test data
    for day_date, meals, workouts in test_data_2025 + test_data_2026:
        day = add_day(day_date)
        for meal in meals:
            day.add_meal(meal)
        for workout in workouts:
            day.add_workout(workout)
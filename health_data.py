from models.DateEntity import Day
from models.CalorieEntity import Meal, Workout
from datetime import date

# Dictionary for storing Day objects
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
# dictionaries moved here
meal_tracker = {}
workout_tracker = {}

# ADDING ENTRIES

def add_meal(meal_date, meal):
    if meal_date in meal_tracker:
        return False

    meal_tracker[meal_date] = meal
    return True


def add_workout(workout_date, workout):
    if workout_date in workout_tracker:
        return False

    workout_tracker[workout_date] = workout
    return True


# SEARCHING ENTRIES

def get_meal(meal_date):
    if meal_date in meal_tracker:
        return meal_tracker[meal_date]
    return None


def get_workout(workout_date):
    if workout_date in workout_tracker:
        return workout_tracker[workout_date]
    return None


# optional helper
def get_entry(entry_date):
    return get_meal(entry_date), get_workout(entry_date)

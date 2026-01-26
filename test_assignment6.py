from unittest import TestCase
from datetime import date
import health_data as db
from models.DateEntity import Day
from models.CalorieEntity import Meal, Workout
from models.EntryType import MealType, WorkoutType


class TestAssignment6(TestCase):
    """Testing cases for Assignment 6 new functionality."""

    def setUp(self):
        """Set up fresh test data for each test."""
        # Clear any existing data
        db.clear_data()

        # Create test day
        self.test_date = date(2024, 1, 15)
        self.day = Day(self.test_date)

        # Add test meals
        self.meal1 = Meal("Breakfast", 500, MealType.BREAKFAST)
        self.meal2 = Meal("Lunch", 300, MealType.LUNCH)
        self.day.add_meal(self.meal1)
        self.day.add_meal(self.meal2)

        # Add test workouts
        self.workout1 = Workout("Morning Run", 400, WorkoutType.CARDIO)
        self.workout2 = Workout("Strength Training", 200, WorkoutType.STRENGTH)
        self.day.add_workout(self.workout1)
        self.day.add_workout(self.workout2)

        # Add to health data
        db.health_data[self.test_date] = self.day

    def test_filter_by_year(self):
        """Test filtering by year using comprehension."""
        # Add another day in different year
        diff_year_date = date(2025, 1, 15)
        diff_year_day = Day(diff_year_date)
        db.health_data[diff_year_date] = diff_year_day

        # Filter 2024 - using comprehension in health_data.filter_by_year()
        filtered = db.filter_by_year(2024)
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].date.year, 2024)

        # Filter 2025
        filtered = db.filter_by_year(2025)
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].date.year, 2025)

        # Filter non-existent year
        filtered = db.filter_by_year(2023)
        self.assertEqual(len(filtered), 0)

    def test_filter_by_month(self):
        """Test filtering by month using comprehension."""
        # Add days in different months
        for month in [2, 3, 4]:
            test_date = date(2024, month, 15)
            db.health_data[test_date] = Day(test_date)

        # Filter January - using comprehension in health_data.filter_by_month()
        filtered = db.filter_by_month(1, 2024)
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].date.month, 1)

        # Filter February
        filtered = db.filter_by_month(2, 2024)
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].date.month, 2)

        # Filter non-existent month
        filtered = db.filter_by_month(12, 2024)
        self.assertEqual(len(filtered), 0)

    def test_filter_by_date_range(self):
        """Test filtering by date range using comprehension."""
        # Add multiple days
        dates = [
            date(2024, 1, 10),
            date(2024, 1, 20),
            date(2024, 1, 30),
            date(2024, 2, 10)
        ]

        for d in dates:
            db.health_data[d] = Day(d)

        # Filter range within January - using comprehension
        start = date(2024, 1, 15)
        end = date(2024, 1, 25)
        filtered = db.filter_by_date_range(start, end)
        self.assertEqual(len(filtered), 1)  # Only Jan 20

        # Filter range spanning months
        start = date(2024, 1, 25)
        end = date(2024, 2, 15)
        filtered = db.filter_by_date_range(start, end)
        self.assertEqual(len(filtered), 2)  # Jan 30 and Feb 10

        # Filter range with no matches
        start = date(2024, 3, 1)
        end = date(2024, 3, 31)
        filtered = db.filter_by_date_range(start, end)
        self.assertEqual(len(filtered), 0)

    def test_delete_meal(self):
        """Test deleting a meal."""
        self.assertEqual(len(self.day.meals), 2)

        # Delete first meal
        result = db.delete_meal(self.test_date, 0)
        self.assertTrue(result)
        self.assertEqual(len(self.day.meals), 1)
        self.assertEqual(self.day.meals[0].description, "Lunch")

        # Try to delete invalid index
        result = db.delete_meal(self.test_date, 5)
        self.assertFalse(result)
        self.assertEqual(len(self.day.meals), 1)

    def test_delete_workout(self):
        """Test deleting a workout."""
        self.assertEqual(len(self.day.workouts), 2)

        # Delete first workout
        result = db.delete_workout(self.test_date, 0)
        self.assertTrue(result)
        self.assertEqual(len(self.day.workouts), 1)
        self.assertEqual(self.day.workouts[0].description, "Strength Training")

        # Try to delete invalid index
        result = db.delete_workout(self.test_date, 5)
        self.assertFalse(result)
        self.assertEqual(len(self.day.workouts), 1)

    def test_meal_calories_comprehension(self):
        """Test meal calories calculation using comprehension."""
        # Day class uses: sum(meal.calories for meal in self.__meals)
        self.assertEqual(self.day.meal_calories(), 800)

        # Add another meal
        meal3 = Meal("Dinner", 400, MealType.DINNER)
        self.day.add_meal(meal3)
        self.assertEqual(self.day.meal_calories(), 1200)

    def test_workout_calories_comprehension(self):
        """Test workout calories calculation using comprehension."""
        # Day class uses: sum(workout.calories for workout in self.__workouts)
        self.assertEqual(self.day.workout_calories(), 600)

        # Add another workout
        workout3 = Workout("Evening Walk", 150, WorkoutType.CARDIO)
        self.day.add_workout(workout3)
        self.assertEqual(self.day.workout_calories(), 750)

    def test_total_net_calories_comprehension(self):
        """Test calculating total net calories from filtered list."""
        # Add more days for testing
        day2 = Day(date(2024, 1, 16))
        day2.add_meal(Meal("Meal1", 200, MealType.BREAKFAST))
        day2.add_workout(Workout("Workout1", 100, WorkoutType.CARDIO))
        db.health_data[date(2024, 1, 16)] = day2

        day3 = Day(date(2024, 1, 17))
        day3.add_meal(Meal("Meal1", 300, MealType.LUNCH))
        day3.add_workout(Workout("Workout1", 150, WorkoutType.STRENGTH))
        db.health_data[date(2024, 1, 17)] = day3

        # Filter days in January 2024
        filtered = db.filter_by_year(2024)

        # Calculate total net calories using comprehension
        total_net_calories = sum(day.net_calories for day in filtered)

        # Day1: 800 - 600 = 200
        # Day2: 200 - 100 = 100
        # Day3: 300 - 150 = 150
        # Total: 200 + 100 + 150 = 450
        self.assertEqual(total_net_calories, 450)


if __name__ == '__main__':
    import unittest

    unittest.main()
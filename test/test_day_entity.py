from unittest import TestCase
from datetime import date
from models.DateEntity import Day
from models.CalorieEntity import Meal, Workout
from models.EntryType import MealType, WorkoutType


class TestDayEntity(TestCase):
    """Testing cases for Day class."""

    @classmethod
    def setUpClass(cls):
        """Set up test data that will be used in multiple tests."""
        # Creating a test date
        cls.test_date = date(2024, 1, 15)

        # Creating a Day object with meals and workouts
        cls.test_day = Day(cls.test_date)

        # Adding test meals
        cls.test_meal1 = Meal("Breakfast", 500, MealType.BREAKFAST)
        cls.test_meal2 = Meal("Lunch", 300, MealType.LUNCH)
        cls.test_day.add_meal(cls.test_meal1)
        cls.test_day.add_meal(cls.test_meal2)

        # Adding test workouts
        cls.test_workout1 = Workout("Morning Run", 400, WorkoutType.CARDIO)
        cls.test_workout2 = Workout("Strength Training", 200, WorkoutType.STRENGTH)
        cls.test_day.add_workout(cls.test_workout1)
        cls.test_day.add_workout(cls.test_workout2)

    def test_net_calories_calculation(self):
        """Testing net_calories property calculation."""
        # Total meals: 500 + 300 = 800
        # Total workouts: 400 + 200 = 600
        # Net calories: 800 - 600 = 200
        self.assertEqual(self.test_day.meal_calories(), 800)
        self.assertEqual(self.test_day.workout_calories(), 600)
        self.assertEqual(self.test_day.net_calories, 200)

    def test_equals_method_same_object(self):
        """Testing __eq__ method with same object."""
        self.assertEqual(self.test_day, self.test_day)

    def test_equals_method_different_date(self):
        """Testing __eq__ method with different date."""
        different_day = Day(date(2024, 1, 16))  # Different date
        self.assertNotEqual(self.test_day, different_day)

    def test_equals_method_same_date(self):
        """Testing __eq__ method with same date."""
        same_date_day = Day(date(2024, 1, 15))  # Same date
        self.assertNotEqual(self.test_day, same_date_day)

    def test_empty_day_calories(self):
        """Testing a day with no meals or workouts."""
        empty_day = Day(date(2024, 1, 1))

        self.assertEqual(empty_day.meal_calories(), 0)
        self.assertEqual(empty_day.workout_calories(), 0)
        self.assertEqual(empty_day.net_calories, 0)

    def test_string_representation(self):
        """Testing __str__ method contains expected labels."""
        day_str = str(self.test_day)

        # Checking for expected labels in the string
        self.assertIn("Date:", day_str)
        self.assertIn("Meals:", day_str)
        self.assertIn("Workouts:", day_str)
        self.assertIn("Net Calories:", day_str)

        # Checking that meals are included
        self.assertIn("Breakfast", day_str)
        self.assertIn("Lunch", day_str)

        # Checking that workouts are included
        self.assertIn("Morning Run", day_str)
        self.assertIn("Strength Training", day_str)

    def test_add_meal(self):
        """Testing adding a meal to day."""
        new_day = Day(date(2024, 1, 2))
        new_meal = Meal("Dinner", 400, MealType.DINNER)

        self.assertEqual(len(new_day.meals), 0)  # Initially empty
        new_day.add_meal(new_meal)
        self.assertEqual(len(new_day.meals), 1)  # Should have 1 meal
        self.assertEqual(new_day.meal_calories(), 400)

    def test_add_workout(self):
        """Testing adding a workout to day."""
        new_day = Day(date(2024, 1, 2))
        new_workout = Workout("Evening Walk", 150, WorkoutType.CARDIO)

        self.assertEqual(len(new_day.workouts), 0)  # Initially empty
        new_day.add_workout(new_workout)
        self.assertEqual(len(new_day.workouts), 1)  # Should have 1 workout
        self.assertEqual(new_day.workout_calories(), 150)

    def test_meal_and_workout_lists(self):
        """Testing that meals and workouts are stored correctly."""
        # Checking meal list
        self.assertEqual(len(self.test_day.meals), 2)
        self.assertIsInstance(self.test_day.meals[0], Meal)
        self.assertIsInstance(self.test_day.meals[1], Meal)

        # Checking workout list
        self.assertEqual(len(self.test_day.workouts), 2)
        self.assertIsInstance(self.test_day.workouts[0], Workout)
        self.assertIsInstance(self.test_day.workouts[1], Workout)

    def test_date_property(self):
        """Testing date getter and setter."""
        # Testing getter
        self.assertEqual(self.test_day.date, self.test_date)

        # Testing setter
        new_date = date(2024, 2, 1)
        self.test_day.date = new_date
        self.assertEqual(self.test_day.date, new_date)

        # Reset to original
        self.test_day.date = self.test_date

    def test_net_calories_property_negative(self):
        """Testing net_calories when workouts exceed meals."""
        day = Day(date(2024, 1, 3))
        day.add_meal(Meal("Small Meal", 100, MealType.BREAKFAST))
        day.add_workout(Workout("Intense Workout", 300, WorkoutType.CARDIO))

        # 100 - 300 = -200
        self.assertEqual(day.net_calories, -200)

    def test_meal_calories_empty(self):
        """Testing meal_calories with empty meals list."""
        day = Day(date(2024, 1, 4))
        self.assertEqual(day.meal_calories(), 0)

    def test_workout_calories_empty(self):
        """Testing workout_calories with empty workouts list."""
        day = Day(date(2024, 1, 4))
        self.assertEqual(day.workout_calories(), 0)

    def test_meal_calories_comprehension(self):
        """Test that meal_calories uses comprehension."""
        day = Day(date(2024, 1, 5))
        day.add_meal(Meal("Breakfast", 100, MealType.BREAKFAST))
        day.add_meal(Meal("Lunch", 200, MealType.LUNCH))
        day.add_meal(Meal("Dinner", 300, MealType.DINNER))

        # Using comprehension: sum(meal.calories for meal in self.__meals)
        self.assertEqual(day.meal_calories(), 600)

    def test_workout_calories_comprehension(self):
        """Test that workout_calories uses comprehension."""
        day = Day(date(2024, 1, 5))
        day.add_workout(Workout("Workout1", 50, WorkoutType.CARDIO))
        day.add_workout(Workout("Workout2", 75, WorkoutType.STRENGTH))
        day.add_workout(Workout("Workout3", 100, WorkoutType.FLEXIBILITY))

        # Using comprehension: sum(workout.calories for workout in self.__workouts)
        self.assertEqual(day.workout_calories(), 225)
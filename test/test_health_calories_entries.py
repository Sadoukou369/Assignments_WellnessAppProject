from unittest import TestCase
from models.HealthEntry import HealthEntry
from models.CalorieEntity import Meal, Workout
from models.EntryType import MealType, WorkoutType


class TestHealthCalorieEntries(TestCase):
    """Testing cases for HealthEntry, Meal, and Workout classes."""

    @classmethod
    def setUpClass(cls):
        """Seting up test data to be used in multiple tests."""
        cls.test_meal = Meal("Test Meal", 500, MealType.BREAKFAST)
        cls.test_workout = Workout("Test Workout", 400, WorkoutType.CARDIO)

    # Testing Meal class
    def test_meal_setter_positive_calories(self):
        """Test Meal calorie setter with positive values."""
        meal = Meal("Test", 100, MealType.BREAKFAST)
        meal.calories = 300
        self.assertEqual(meal.calories, 300)

    def test_meal_setter_negative_calories(self):
        """Testing Meal calorie setter with negative values."""
        meal = Meal("Test", 100, MealType.BREAKFAST)
        meal.calories = -50
        self.assertEqual(meal.calories, 0)  # Should default to 0

    def test_workout_setter_positive_calories(self):
        """Testing Workout calorie setter with positive values."""
        workout = Workout("Test", 100, WorkoutType.CARDIO)
        workout.calories = 300
        self.assertEqual(workout.calories, 300)

    def test_workout_setter_negative_calories(self):
        """Testing Workout calorie setter with negative values."""
        workout = Workout("Test", 100, WorkoutType.CARDIO)
        workout.calories = -50
        self.assertEqual(workout.calories, 0)  # Should default to 0

    def test_meal_constructor_negative_calories(self):
        """Testing Meal constructor with negative calories."""
        meal = Meal("Negative Meal", -100, MealType.BREAKFAST)
        self.assertEqual(meal.calories, 0)  # Should default to 0

    def test_workout_constructor_negative_calories(self):
        """Testing Workout constructor with negative calories."""
        workout = Workout("Negative Workout", -100, WorkoutType.CARDIO)
        self.assertEqual(workout.calories, 0)  # Should default to 0

    def test_meal_type_getter_setter(self):
        """Testing Meal type getter and setter."""
        # Test getter
        self.assertEqual(self.test_meal.meal_type, MealType.BREAKFAST)

        # Testing setter with valid type
        self.test_meal.meal_type = MealType.LUNCH
        self.assertEqual(self.test_meal.meal_type, MealType.LUNCH)

        # Reset to original
        self.test_meal.meal_type = MealType.BREAKFAST

    def test_workout_type_getter_setter(self):
        """Testing Workout type getter and setter."""
        # Testing getter
        self.assertEqual(self.test_workout.workout_type, WorkoutType.CARDIO)

        # Testing setter with valid type
        self.test_workout.workout_type = WorkoutType.STRENGTH
        self.assertEqual(self.test_workout.workout_type, WorkoutType.STRENGTH)

        # Reset to original
        self.test_workout.workout_type = WorkoutType.CARDIO

    def test_invalid_meal_type(self):
        """Testing Meal with invalid type."""
        meal = Meal("Invalid Type Meal", 300, "INVALID_TYPE")
        # Should default to SNACK
        self.assertEqual(meal.meal_type, MealType.SNACK)

        # Testing setting invalid type
        meal.meal_type = 123  # Not a MealType
        self.assertEqual(meal.meal_type, MealType.SNACK)  # Should stay as default

    def test_invalid_workout_type(self):
        """Testing Workout with invalid type."""
        workout = Workout("Invalid Type Workout", 300, "INVALID_TYPE")

        self.assertEqual(workout.workout_type, WorkoutType.OTHER)

        # Testing setting invalid type
        workout.workout_type = 123  # Not a WorkoutType
        self.assertEqual(workout.workout_type, WorkoutType.OTHER)  # Should stay as default

    def test_meal_string_representation(self):
        """Testing Meal __str__ method."""
        meal = Meal("Test Meal", 250, MealType.BREAKFAST)
        expected = "Entry: Test Meal, Calories: 250, Type: Breakfast"
        self.assertEqual(str(meal), expected)

    def test_workout_string_representation(self):
        """Testing Workout __str__ method."""
        workout = Workout("Morning Run", 300, WorkoutType.CARDIO)
        expected = "Entry: Morning Run, Calories: 300, Type: Cardio"
        self.assertEqual(str(workout), expected)

    def test_health_entry_inheritance(self):
        """Testing that Meal and Workout inherit from HealthEntry."""
        meal = Meal("Test", 100, MealType.BREAKFAST)
        workout = Workout("Test", 100, WorkoutType.CARDIO)

        self.assertTrue(isinstance(meal, HealthEntry))
        self.assertTrue(isinstance(workout, HealthEntry))

        # Testing inherited properties
        meal.description = "Updated Meal"
        self.assertEqual(meal.description, "Updated Meal")

        workout.description = "Updated Workout"
        self.assertEqual(workout.description, "Updated Workout")
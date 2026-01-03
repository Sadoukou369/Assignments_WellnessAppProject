from abc import ABC, abstractmethod
from enum import Enum

class HealthEntry(ABC):
    """Base class for all health-related entries (Meal and Workout)."""

    def __init__(self, description: str, calories: int):
        """Initialize with description and calories."""
        self._description = description
        self.calories = calories  # Uses setter for validation

    @property
    def description(self) -> str:
        """Get the entry description."""
        return self._description

    @description.setter
    def description(self, value: str):
        """Set the entry description."""
        self._description = value

    @property
    def calories(self) -> int:
        """Get the calories."""
        return self._calories

    @calories.setter
    def calories(self, value: int):
        """Set calories with validation (must be > 0)."""
        if value > 0:
            self._calories = value
        else:
            raise ValueError("Calories must be greater than 0")

    @abstractmethod
    def __str__(self) -> str:
        """Abstract method to be implemented by subclasses."""
        pass

    def base_string(self) -> str:
        """Helper method for common string formatting."""
        return f"Entry: {self._description}, Calories: {self._calories}"
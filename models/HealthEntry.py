class HealthEntry:
    """Base class for all health-related entries (Meal and Workout)."""

    def __init__(self, description: str, calories: int):
        """Initialize with description and calories."""
        self._description = description
        # Use property setter for validation
        self.calories = calories

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

    def __str__(self) -> str:
        """String representation - to be overridden by subclasses."""
        return f"Entry: {self._description}, Calories: {self._calories}"
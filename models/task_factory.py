"""Centralized creation of Task objects."""
from typing import Optional

from models.task import Task


class TaskFactory:
    """Simple Factory for task objects."""

    @staticmethod
    def create(
        description: str,
        priority: str = "Medium",
        category: str = "General",
        due_date: Optional[str] = None,
    ) -> Task:
        """Create a normalized, validated task."""
        return Task(
            description=description.strip(),
            priority=priority,
            category=category.strip() if category else "General",
            due_date=due_date or None,
        )

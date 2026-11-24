"""Observer types for task lifecycle events."""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class TaskEvent:
    kind: str
    task_id: int
    task_description: Optional[str] = None


class TaskObserver(ABC):
    """Interface for components interested in task events."""

    @abstractmethod
    def on_task_event(self, event: TaskEvent) -> None:
        """Handle a task event."""
        raise NotImplementedError

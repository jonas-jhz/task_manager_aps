"""Application facade coordinating task operations and observers."""
from typing import Iterable, Protocol

from models.task import Task
from models.task_factory import TaskFactory
from application.task_observer import TaskEvent, TaskObserver


class TaskRepository(Protocol):
    def insert_task(self, task: Task) -> int: ...
    def update_task(self, task: Task) -> None: ...
    def delete_task(self, task_id: int) -> None: ...
    def mark_task_complete(self, task_id: int) -> None: ...
    def mark_task_incomplete(self, task_id: int) -> None: ...
    def get_task_by_id(self, task_id: int) -> Task | None: ...


class TaskFacade:
    """Single application entry point for use cases involving tasks."""

    def __init__(self, repository: TaskRepository):
        self.repository = repository
        self._observers: list[TaskObserver] = []

    def subscribe(self, observer: TaskObserver) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def unsubscribe(self, observer: TaskObserver) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def create_task(self, description: str, priority: str, category: str, due_date: str | None = None) -> int:
        task = TaskFactory.create(description, priority, category, due_date)
        task_id = self.repository.insert_task(task)
        self._notify(TaskEvent("task_created", task_id, task.description))
        return task_id

    def update_task(self, task: Task) -> None:
        self.repository.update_task(task)
        self._notify(TaskEvent("task_updated", task.id or 0, task.description))

    def delete_task(self, task_id: int) -> None:
        task = self.repository.get_task_by_id(task_id)
        self.repository.delete_task(task_id)
        self._notify(TaskEvent("task_deleted", task_id, task.description if task else None))

    def complete_task(self, task_id: int) -> None:
        task = self.repository.get_task_by_id(task_id)
        self.repository.mark_task_complete(task_id)
        self._notify(TaskEvent("task_completed", task_id, task.description if task else None))

    def incomplete_task(self, task_id: int) -> None:
        task = self.repository.get_task_by_id(task_id)
        self.repository.mark_task_incomplete(task_id)
        self._notify(TaskEvent("task_incompleted", task_id, task.description if task else None))

    def _notify(self, event: TaskEvent) -> None:
        for observer in tuple(self._observers):
            observer.on_task_event(event)

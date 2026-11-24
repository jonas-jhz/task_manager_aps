"""Tests for the new task application patterns."""
import tempfile
import unittest

from database import TaskDatabase
from models.task_factory import TaskFactory
from application.task_facade import TaskFacade
from application.task_observer import TaskObserver


class RecordingObserver(TaskObserver):
    def __init__(self):
        self.events = []

    def on_task_event(self, event):
        self.events.append(event)


class TestApplicationPatterns(unittest.TestCase):
    def setUp(self):
        self.temp_db = tempfile.NamedTemporaryFile(delete=False, suffix=".db")
        self.temp_db.close()
        self.db = TaskDatabase(self.temp_db.name)
        self.facade = TaskFacade(self.db)

    def tearDown(self):
        self.db.close()
        import os
        os.unlink(self.temp_db.name)

    def test_factory_creates_normalized_task(self):
        task = TaskFactory.create(
            description="  Study patterns  ",
            priority="High",
            category="Study",
            due_date="2026-12-31",
        )

        self.assertEqual(task.description, "Study patterns")
        self.assertEqual(task.priority, "High")

    def test_complete_task_notifies_registered_observer(self):
        task_id = self.db.insert_task(
            TaskFactory.create(description="Observer test", category="General")
        )
        observer = RecordingObserver()
        self.facade.subscribe(observer)

        self.facade.complete_task(task_id)

        self.assertEqual(len(observer.events), 1)
        event = observer.events[0]
        self.assertEqual(event.kind, "task_completed")
        self.assertEqual(event.task_id, task_id)


if __name__ == "__main__":
    unittest.main()

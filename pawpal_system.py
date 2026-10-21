from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    description: str
    time: str
    frequency: str
    completed: bool = False

    def mark_complete(self):
        """Mark the task as completed."""
        self.completed = True

    def mark_incomplete(self):
        """Mark the task as incomplete."""
        self.completed = False


@dataclass
class Pet:
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to the pet's task list."""
        self.tasks.append(task)

    def get_tasks(self) -> List[Task]:
        """Return the pet's task list."""
        return self.tasks


@dataclass
class Owner:
    name: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        """Add a pet to the owner's pet list."""
        self.pets.append(pet)

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks belonging to the owner's pets."""
        all_tasks = []

        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())

        return all_tasks


class Scheduler:
    def __init__(self, owner: Owner):
        """Initialize the scheduler with an owner."""
        self.owner = owner

    def get_tasks(self) -> List[Task]:
        """Return all tasks belonging to the owner."""
        return self.owner.get_all_tasks()

    def get_pending_tasks(self) -> List[Task]:
        """Return tasks that have not been completed."""
        pending_tasks = []

        for task in self.get_tasks():
            if not task.completed:
                pending_tasks.append(task)

        return pending_tasks

    def get_tasks_for_frequency(self, frequency: str) -> List[Task]:
        """Return tasks matching the specified frequency."""
        matching_tasks = []

        for task in self.get_tasks():
            if task.frequency == frequency:
                matching_tasks.append(task)

        return matching_tasks

    def mark_task_complete(self, task: Task):
        """Mark the specified task as completed."""
        task.mark_complete()

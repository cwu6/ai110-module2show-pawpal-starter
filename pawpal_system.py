from dataclasses import dataclass, field
from typing import List
from datetime import date, datetime, timedelta


@dataclass
class Task:
    description: str
    time: str
    frequency: str
    completed: bool = False
    due_date: date = field(default_factory=date.today)

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
        """Mark a task complete and create its next recurring occurrence."""
        if task.completed:
            return

        task.mark_complete()

        if task.frequency == "daily":
            next_date = task.due_date + timedelta(days=1)
        elif task.frequency == "weekly":
            next_date = task.due_date + timedelta(days=7)
        else:
            return
        
        for pet in self.owner.pets:
            if task in pet.tasks:
                next_task = Task(
                    task.description,
                    task.time,
                    task.frequency,
                    due_date=next_date
                )
                pet.add_task(next_task)
                return

    def sort_by_time(self) -> List[Task]:
        """Return all tasks sorted by their scheduled time."""
        from datetime import datetime

        return sorted(
            self.get_tasks(),
            key=lambda task: datetime.strptime(task.time, "%I:%M %p")
        )
    
    def filter_by_status(self, completed: bool) -> List[Task]:
        """Return tasks matching the requested completion status."""
        matching_tasks = []

        for task in self.get_tasks():
            if task.completed == completed:
                matching_tasks.append(task)

        return matching_tasks
    
    def filter_by_pet(self, pet_name: str) -> List[Task]:
        """Return tasks belonging to the pet with the given name."""
        matching_tasks = []

        for pet in self.owner.pets:
            if pet.name.lower() == pet_name.lower():
                matching_tasks.extend(pet.get_tasks())

        return matching_tasks

    def find_conflicts(self) -> List[str]:
        """Return warnings for tasks scheduled at the same time."""
        conflicts = []
        tasks = []

        for pet in self.owner.pets:
            for task in pet.tasks:
                tasks.append((pet.name, task))

        for i in range(len(tasks)):
            pet_name, task = tasks[i]

            for j in range(i + 1, len(tasks)):
                other_pet, other_task = tasks[j]

                if (task.time == other_task.time
                        and task.due_date == other_task.due_date):
                    warning = (
                        f"Conflict: {pet_name}'s '{task.description}' and "
                        f"{other_pet}'s '{other_task.description}' are both "
                        f"scheduled at {task.time} on {task.due_date}."
                    )
                    conflicts.append(warning)

        return conflicts



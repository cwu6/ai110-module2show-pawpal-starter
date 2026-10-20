
from dataclasses import dataclass, field
from typing import List


class Owner:
    def __init__(
        self,
        name: str,
        available_minutes: int,
        preferences: str
    ):
        self.name = name
        self.available_minutes = available_minutes
        self.preferences = preferences
        self.pets = []

    def add_pet(self, pet):
        pass

    def update_availability(self, minutes: int):
        pass


@dataclass
class Pet:
    name: str
    species: str
    age: int
    care_needs: str
    tasks: List["Task"] = field(default_factory=list)

    def add_task(self, task: "Task"):
        pass


@dataclass
class Task:
    name: str
    duration: int
    priority: str
    preferred_time: str = ""

    def is_feasible(self, available_minutes: int) -> bool:
        pass


class Schedule:
    def __init__(self, date: str, tasks: List[Task] = None):
        self.date = date
        self.tasks = tasks if tasks is not None else []
        self.total_duration = 0

    def generate_plan(self):
        pass

    def explain_plan(self):
        pass

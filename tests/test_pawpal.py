
from pawpal_system import Pet, Task


def test_task_completion():
    task = Task("Morning walk", "8:00 AM", "daily")

    task.mark_complete()

    assert task.completed is True


def test_task_addition():
    pet = Pet("Biscuit", "Dog", 3)

    task = Task("Morning walk", "8:00 AM", "daily")
    pet.add_task(task)

    assert len(pet.tasks) == 1

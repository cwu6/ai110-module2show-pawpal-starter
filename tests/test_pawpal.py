
from datetime import timedelta

from pawpal_system import Owner, Pet, Task, Scheduler

def test_task_completion():
    task = Task("Morning walk", "8:00 AM", "daily")

    task.mark_complete()

    assert task.completed is True

def test_task_addition():
    pet = Pet("Biscuit", "Dog", 3)

    task = Task("Morning walk", "8:00 AM", "daily")
    pet.add_task(task)

    assert len(pet.tasks) == 1

def test_sort_by_time():
    owner = Owner("Alex")
    dog = Pet("Biscuit", "Dog", 3)

    dog.add_task(Task("Dinner", "6:00 PM", "daily"))
    dog.add_task(Task("Walk", "8:00 AM", "daily"))
    owner.add_pet(dog)

    scheduler = Scheduler(owner)
    sorted_tasks = scheduler.sort_by_time()

    assert [task.description for task in sorted_tasks] == [
        "Walk", "Dinner"
    ]

def test_daily_task_recurrence():
    owner = Owner("Alex")
    dog = Pet("Biscuit", "Dog", 3)

    task = Task("Morning walk", "8:00 AM", "daily")
    dog.add_task(task)
    owner.add_pet(dog)

    scheduler = Scheduler(owner)
    original_date = task.due_date

    scheduler.mark_task_complete(task)

    assert task.completed is True
    assert len(dog.tasks) == 2
    assert dog.tasks[1].completed is False
    assert dog.tasks[1].due_date == original_date + timedelta(days=1)

def test_conflict_detection():
    owner = Owner("Alex")
    dog = Pet("Biscuit", "Dog", 3)
    cat = Pet("Mochi", "Cat", 2)

    dog.add_task(Task("Morning walk", "8:00 AM", "daily"))
    cat.add_task(Task("Breakfast", "8:00 AM", "daily"))

    owner.add_pet(dog)
    owner.add_pet(cat)

    scheduler = Scheduler(owner)
    conflicts = scheduler.find_conflicts()

    assert len(conflicts) == 1
    assert "Conflict" in conflicts[0]

def test_empty_pet_has_no_tasks():
    owner = Owner("Alex")
    dog = Pet("Biscuit", "Dog", 3)
    owner.add_pet(dog)

    scheduler = Scheduler(owner)

    assert scheduler.filter_by_pet("Biscuit") == []
    assert scheduler.sort_by_time() == []
    assert scheduler.find_conflicts() == []

def test_filter_by_status():
    owner = Owner("Alex")
    dog = Pet("Biscuit", "Dog", 3)

    completed_task = Task("Breakfast", "8:00 AM", "daily")
    completed_task.mark_complete()
    pending_task = Task("Walk", "9:00 AM", "daily")

    dog.add_task(completed_task)
    dog.add_task(pending_task)
    owner.add_pet(dog)

    scheduler = Scheduler(owner)

    assert scheduler.filter_by_status(True) == [completed_task]
    assert scheduler.filter_by_status(False) == [pending_task]

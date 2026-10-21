from pawpal_system import Owner, Pet, Task, Scheduler


owner = Owner("Alex")

dog = Pet("Biscuit", "Dog", 3)
cat = Pet("Mochi", "Cat", 2)

dog.add_task(Task("Morning walk", "8:00 AM", "daily"))
dog.add_task(Task("Breakfast", "8:30 AM", "daily"))

cat.add_task(Task("Breakfast", "9:00 AM", "daily"))

owner.add_pet(dog)
owner.add_pet(cat)

scheduler = Scheduler(owner)

print("Today's Schedule")
print("----------------")

for task in scheduler.get_tasks():
    status = "Completed" if task.completed else "Pending"
    print(
        f"{task.time} - {task.description} "
        f"({task.frequency}) - {status}"
    )

scheduler = Scheduler(owner)

print("\n--- Tasks Sorted by Time ---")
for task in scheduler.sort_by_time():
    print(f"{task.time} - {task.description}")

print("\n--- Pending Tasks ---")
for task in scheduler.filter_by_status(False):
    print(f"{task.time} - {task.description}")

print("\n--- Biscuit's Tasks ---")
for task in scheduler.filter_by_pet("Biscuit"):
    print(f"{task.time} - {task.description}")

morning_walk = dog.tasks[0]
scheduler.mark_task_complete(morning_walk)

print("\n--- Test Recurring Tasks ---")
for task in dog.tasks:
    print(
        f"{task.due_date} - {task.time} - {task.description} - "
        f"{'Completed' if task.completed else 'Pending'}"
    )

cat.add_task(Task("Vet appointment", "8:00 AM", "once"))

print("\n--- Test Conflict Detection ---")
conflicts = scheduler.find_conflicts()

if conflicts:
    for warning in conflicts:
        print(warning)
else:
    print("No scheduling conflicts found.")
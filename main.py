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

import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

if "owner" not in st.session_state:
    st.session_state.owner = Owner("Chloe")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )


st.divider()

st.subheader("Owner Information")
owner_name = st.text_input(
    "Owner name",
    value=st.session_state.owner.name
)

if owner_name.strip():
    st.session_state.owner.name = owner_name.strip()

st.subheader("Add a Pet")
pet_name = st.text_input("Pet name")
species = st.selectbox("Species", ["dog", "cat", "other"])
pet_age = st.number_input("Pet age", min_value=0, value=1, step=1)

if st.button("Add Pet"):
    if pet_name.strip():
        pet = Pet(pet_name.strip(), species, int(pet_age))
        st.session_state.owner.add_pet(pet)
        st.success(f"Added {pet.name}!")
    else:
        st.warning("Please enter a pet name.")

st.subheader("Your Pets")
pets = st.session_state.owner.pets

if pets:
    for pet in pets:
        st.write(f"**{pet.name}** — {pet.species}, age {pet.age}")
else:
    st.info("No pets added yet.")

st.divider()

st.subheader("Add a Care Task")

if pets:
    pet_names = [pet.name for pet in pets]
    selected_pet = st.selectbox("Choose a pet", pet_names)

    task_title = st.text_input("Task title", value="Morning walk")
    task_time = st.text_input("Task time", value="8:00 AM")
    frequency = st.selectbox(
        "Frequency", ["daily", "weekly", "monthly"]
    )

    if st.button("Add Task"):
        if task_title.strip() and task_time.strip():
            for pet in pets:
                if pet.name == selected_pet:
                    task = Task(
                        task_title.strip(),
                        task_time.strip(),
                        frequency
                    )
                    pet.add_task(task)
                    st.success(f"Added task for {pet.name}!")
                    break
        else:
            st.warning("Please enter a task title and time.")
else:
    st.info("Add a pet before creating a task.")

st.subheader("Current Tasks")
has_tasks = False

for pet in pets:
    if pet.tasks:
        has_tasks = True
        st.write(f"**{pet.name}'s tasks**")

        for task in pet.tasks:
            status = "Completed" if task.completed else "Pending"
            st.write(
                f"- {task.description} | {task.time} | "
                f"{task.frequency} | {status}"
            )

if not has_tasks:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")

if st.button("Generate Schedule"):
    scheduler = Scheduler(st.session_state.owner)
    tasks = scheduler.get_tasks()

    if tasks:
        st.success("Here is your schedule!")

        for task in tasks:
            status = "Completed" if task.completed else "Pending"
            st.write(
                f"**{task.time}** — {task.description} "
                f"({task.frequency}) — {status}"
            )
    else:
        st.info("No tasks yet. Add a task first.")

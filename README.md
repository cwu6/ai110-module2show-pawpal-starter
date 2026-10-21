# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
# e.g.:
# Daily plan for Biscuit (Golden Retriever):
#   08:00 — Morning walk (30 min) [priority: high]
#   09:00 — Feeding (10 min) [priority: high]
#   ...
```
My Sample:

Today's Schedule
----------------
8:00 AM - Morning walk (daily) - Pending
8:30 AM - Breakfast (daily) - Pending
9:00 AM - Breakfast (daily) - Pending

Implementation Summary:

I built a pet care tasks scheduling system. The Task class stores each task's description, time, frequency, and status of completion. The Pet class stores pet information and manage its tasks. The Owner class manages multiple pets and collects tasks from all of the pets by using get_all_tasks(). The Scheduler class gets the tasks through the Owner class and manages the schedule.

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
python -m pytest

# Run with coverage:
python -m pytest --cov
```

What the tests cover:
- Task completion and task addition
- Sorts tasks by scheduling time
- Daily recurring task creation
- Detecting conflicts for tasks scheduled at the same time
- Filtering tasks by completion status
- Handling pets with no tasks

Sample test output:

```
# Paste your pytest output here
```
====================================== test session starts ======================================
platform darwin -- Python 3.14.7, pytest-9.1.1, pluggy-1.7.0
rootdir: /Users/chlxe/ai110-module2show-pawpal-starter
plugins: anyio-4.15.1
collected 7 items                                                                               

tests/test_pawpal.py .......                                                              [100%]

======================================= 7 passed in 0.02s =======================================

Confidence Level: 
4/5 stars

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | Scheduler.sort_by_time() | Sorts tasks in chronological order by scheduled time |
| Filtering | Scheduler.filter_by_status(), Scheduler.filter_by_pet() | Filters tasks by pet name or completion status |
| Conflict handling | Scheduler.find_conflicts | Returns warning messages when two tasks have the same scheduled time on the same date |
| Recurring tasks | Scheduler.mark_task_complete() | Creates the next occurence one day later for daily tasks or seven days later for weekly tasks |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. Enter Owner Information: The user enters their name in the Owner information section
2. Enter Pets: The user enters a pet's name, select its species, and enters its age. Click Add Pet to save the pet
3. Verify Your Pets: Check the Your Pets section to enusre the pet has been added
4. Add A Care Task: Select a pet, enter the task and task time, choose a frequency, and click Add Task
5. Verify Current Tasks: Review each pet's care tasks, including scheduled time, frequency, and status of completion
6. Generate A Schedule: Click Generate Schedule to display tasks that are sorted by scheduled time
7. Check for Scheduling Conflicts: Review any warnings about tasks scheduled at the same time on the same date

Example output: python main.py

Today's Schedule
----------------
8:00 AM - Morning walk (daily) - Pending
8:30 AM - Breakfast (daily) - Pending
9:00 AM - Breakfast (daily) - Pending

--- Tasks Sorted by Time ---
8:00 AM - Morning walk
8:30 AM - Breakfast
9:00 AM - Breakfast

--- Pending Tasks ---
8:00 AM - Morning walk
8:30 AM - Breakfast
9:00 AM - Breakfast

--- Rachel's Tasks ---
8:00 AM - Morning walk
8:30 AM - Breakfast

--- Test Recurring Tasks ---
2026-10-21 - 8:00 AM - Morning walk - Completed
2026-10-21 - 8:30 AM - Breakfast - Pending
2026-10-22 - 8:00 AM - Morning walk - Pending

--- Test Conflict Detection ---
Conflict: Rachel's 'Morning walk' and Jules's 'Vet appointment' are both scheduled at 8:00 AM on 2026-10-21.


**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->

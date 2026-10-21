# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

Three core actions:
    1. Enter the owner and pet's information: The user can enter basic information about themselves and their pet. Such information can include owner's name and avaliability, pet's name, breed, and special care needs, and any care preferences the owner may have
    2. Add and Manage care tasks: The user can add and edit tasks such as walking, feeding, grooming, medication. They also provide specific details about the duration of these tasks or their priority
    3. Generate a daily schedule: The user can generate a daily schedule based on their needs, avaliability, and preferences

Initial UML Design:
Classes:
    - Owner: Stores the owner's name, preferences, and available time for pet. It also manages the owner's pet and allows for their availibility to be updated
    - Pet: Stores information about the pet, including its name, breed, age, and specific care needs. It also assists in tracking the pet's care tasks
    - Task: Defines a pet care activity, including walking, grooming, or feeding
    - Schedule: Organizes the pet care tasks into a daily schedule. It generates a schedule based on the tasks needs and priorities, availibility, and explains why each task was assigned


**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

Based on AI feedback and reviewing my initial skeleton, I noticied some missing relationships and methods that could use improvement. For instance, the Owner class needs a way to manage multiple pets. To fix this, I added a type hint to the pets lists so that it could contain Pet objects and added an add_pet() method. The Pet Class needed a way to store and manage the tasks so I kept the tasks list but added an add_task() method. Additionally, the Schedule class needed a more direct way to get the tasks across all of the owner's pets, so I added an Owner.get_all_tasks() method. I also updated the Schedule class to accept an Owner object to allow the scheduling logic to connect to the owner's pets. 

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

One tradeoff my scheduler makes is that it checks whether tasks have the exact same scheduled time instead of checking whether their durations overlap. With this, it may miss conflicts between tasks that start at different times but overlap in duration. For example, a task from 8:00 AM to 8:30 AM could overlap with another task starting at 8:15 AM. A future improvement would be to add task durations and check whether their time intervals overlap. This tradeoff is reasonable because PawPal+ is a simple pet task scheduler, so checking for the exact time matches is easy to implement. It can warn owners when two tasks are scheduled at the same time without requiring extra information about task durations. Although it may miss tasks that overlap in duration, exact time matching is enough for the project's instructions and keeps the scheduler more simple.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

I used AI to help implement the methods in pawpal_system.py and to understand the relationships between the Task, Pet, Owner, and Scheduler classes. I also used AI to help write the demo script for main.py and draft two basic tests for task completion and task addition. Additionally, it assisted to adding one-line docstrings to my methods. AI also assisted in debugging and clafification for certain concepts I didn;t undersatnd such as type hints or improving code readability. The most helpful prompts were specific questions about how a method should work and how to verify that my implemenations work. For instance, I asked "How should the Scheduler get all the tasks from the Owner's Pets?" This allows me to understand how classes interact and their relationships.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

One moment where I did not accept an AI suggestion as-is is when making sure that the Scheduler class recieved tasks from multiple pets. Initially, the AI suggested an implementation where it only recieved tasks from one pet. But after reviewing the instructions, I realized that it needed to target multiple pets simulatenously. So I made sure Scheduler.get_tasks() called Owner.get_all_tasks() which helps collects the tasks from every pet. To verify what AI suggested I ran main.py and made sure the schedule displayed all the tasks from all pets. 
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

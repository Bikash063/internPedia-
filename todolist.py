import os

# File to store tasks
TASKS_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from the file."""
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            for line in file:
                task, status = line.strip().split("||")
                tasks.append({"task": task, "done": status == "1"})
    return tasks

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            status = "1" if task["done"] else "0"
            file.write(f"{task['task']}||{status}\n")

def display_tasks(tasks):
    """Display all tasks with their completion status."""
    if not tasks:
        print("\nNo tasks to show.")
    else:
        print("\nTo-Do List:")
        for index, task in enumerate(tasks, start=1):
            status = "[Done]" if task["done"] else "[Not Done]"
            print(f"{index}. {task['task']} {status}")

def add_task(tasks):
    """Add a new task to the list."""
    task = input("\nEnter the new task: ").strip()
    if task:
        tasks.append({"task": task, "done": False})
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")

def mark_task(tasks, done=True):
    """Mark a task as done or undone."""
    display_tasks(tasks)
    if tasks:
        try:
            task_index = int(input("\nEnter the task number to mark: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = done
                status = "done" if done else "undone"
                print(f"Task marked as {status}.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def remove_task(tasks):
    """Remove a task from the list."""
    display_tasks(tasks)
    if tasks:
        try:
            task_index = int(input("\nEnter the task number to remove: ")) - 1
            if 0 <= task_index < len(tasks):
                removed_task = tasks.pop(task_index)
                print(f"Removed task: {removed_task['task']}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main_menu():
    """Display the main menu and handle user choices."""
    print("\nTo-Do List Application")
    print("======================")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Mark Task as Undone")
    print("5. Remove Task")
    print("6. Save and Exit")
    
def main():
    tasks = load_tasks()

    while True:
        main_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task(tasks, done=True)
        elif choice == '4':
            mark_task(tasks, done=False)
        elif choice == '5':
            remove_task(tasks)
        elif choice == '6':
            save_tasks(tasks)
            print("\nTasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

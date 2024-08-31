# Define an empty list to store tasks
task_list = []

# Function to display the to-do list
def show_tasks():
    """Displays the current to-do list with task status."""
    if not task_list:
        print("Your task list is empty.")
    else:
        print("Task List:")
        for index, item in enumerate(task_list, start=1):
            status = "Completed" if item["done"] else "Pending"
            print(f"{index}. {item['name']} ({status})")

# Function to add a task to the to-do list
def create_task(task_name):
    """Adds a new task to the task list."""
    task = {"name": task_name, "done": False}
    task_list.append(task)
    print(f"Task '{task_name}' added to your task list.")

# Function to mark a task as completed
def complete_task(task_number):
    """Marks a specific task as completed by its number."""
    if 1 <= task_number <= len(task_list):
        task_list[task_number - 1]["done"] = True
        print(f"Task {task_number} marked as completed.")
    else:
        print("Invalid task number. Please enter a valid task number.")

# Function to remove a task from the to-do list
def delete_task(task_number):
    """Removes a task from the task list by its number."""
    if 1 <= task_number <= len(task_list):
        removed_item = task_list.pop(task_number - 1)
        print(f"Task '{removed_item['name']}' removed from your task list.")
    else:
        print("Invalid task number. Please enter a valid task number.")

# Main program loop
while True:
    print("\nMenu:")
    print("1. Show task list")
    print("2. Create a task")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")
    choice = input("Enter your selection: ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        task_name = input("Enter the task description: ")
        create_task(task_name)
    elif choice == '3':
        show_tasks()
        try:
            task_number = int(input("Enter the task number to mark as completed: "))
            complete_task(task_number)
        except ValueError:
            print("Invalid input. Please enter a valid task number.")
    elif choice == '4':
        show_tasks()
        try:
            task_number = int(input("Enter the task number to delete: "))
            delete_task(task_number)
        except ValueError:
            print("Invalid input. Please enter a valid task number.")
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid selection. Please choose a valid option.")
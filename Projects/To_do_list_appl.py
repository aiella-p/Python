# To-Do List Application:

# Build a basic to-do list application where users can add, edit, and delete tasks.

# Input values:
# User interacts with the application through commands to add, edit, or delete tasks.

# Output value:

# Updated the to-do list based on user actions.

# Example:

# Input values:
# 1. Add Task
# 2. Edit Task
# 3. Delete Task
# 4. Exit
# Select an option: 1
# Enter task: Buy groceries
# Output value:
# Task added successfully.
# Input values:
# 1. Add Task
# 2. Edit Task
# 3. Delete Task
# 4. Exit
# Select an option: 2
# Enter task index to edit: 1
# Enter new task: Buy weekly groceries
# Output value:
# Task edited successfully.
# Input values:
# 1. Add Task
# 2. Edit Task
# 3. Delete Task
# 4. Exit
# Select an option: 3
# Enter task index to delete: 1
# Output value:
# Task deleted successfully.
# Input values:
# 1. Add Task
# 2. Edit Task
# 3. Delete Task
# 4. Exit
# Select an option: 4
# Here are two different solutions for a basic to-do list application in Python. This application will allow users to add, edit, and delete tasks using a command-line interface.

# Solution 1: Basic Approach Using a While Loop and List Operations

# Solution 1: Basic Approach Using a While Loop and List Operations

# Initialize an empty list to store tasks
tasks = []

# Function to display the available options
def display_menu():
    print("\n1. Add Task")
    print("2. Edit Task")
    print("3. Delete Task")
    print("4. Exit")

# Start an infinite loop to continuously interact with the user
while True:
    # Display the menu options
    display_menu()
    
    # Get the user's choice
    choice = input("Select an option: ")

    # Option 1: Add Task
    if choice == '1':
        # Prompt the user to enter a task
        task = input("Enter task: ")
        # Add the task to the list
        tasks.append(task)
        print("Task added successfully.")

    # Option 2: Edit Task
    elif choice == '2':
        # Check if there are tasks available to edit
        if tasks:
            # Display the current tasks with their indices
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task}") # this will tell u to start the 
                # the index from 1 not from index 0
            # Prompt the user to enter the index of the task to edit
            try:
                task_index = int(input("Enter task index to edit: ")) - 1
                # Check if the entered index is valid
                if 0 <= task_index < len(tasks):
                    # Prompt the user to enter a new task
                    new_task = input("Enter new task: ")
                    # Update the task at the specified index
                    tasks[task_index] = new_task
                    print("Task edited successfully.")
                else:
                    print("Invalid index.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No tasks available to edit.")

    # Option 3: Delete Task
    elif choice == '3':
        # Check if there are tasks available to delete
        if tasks:
            # Display the current tasks with their indices
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task}")
            # Prompt the user to enter the index of the task to delete
            try:
                task_index = int(input("Enter task index to delete: ")) - 1
                # Check if the entered index is valid
                if 0 <= task_index < len(tasks):
                    # Remove the task at the specified index
                    tasks.pop(task_index)
                    print("Task deleted successfully.")
                else:
                    print("Invalid index.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No tasks available to delete.")

    # Option 4: Exit
    elif choice == '4':
        # Exit the application
        print("Exiting the application. Goodbye!")
        break

    # Handle invalid menu choices
    else:
        print("Invalid choice. Please select a valid option.")

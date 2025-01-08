from typing import List

def show_menu():
    print("\n=== To Do List Manager ===")
    print("1. Add Task")
    print("2. View Task")
    print("3. Remove Task")
    print("4. Quit")

def add_task(tasks):
    task = input("Enter your task: ")
    if task != "": 
        tasks.append(task)
        print("Tasks added Successfully")
    else:
        print("Task cannot be left empty")

def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks in your list!")
    elif len(tasks) > 0:
        enumerate(tasks, starts=1)

def remove_task(tasks: list[str]) -> None:
    # First let's check if the list is empty
    if len(tasks) == 0:  # Note: we have to check length, not comparing string to string
        print("No tasks to remove!")
        return
    #
    view_tasks(tasks) 

try:
    choice = int(input("Which task would you like to remove?"))
    if 1 <= choice <= len(tasks): # checking if choice is valid
        removed_task = tasks.pop(choice - 1) # -1 is because list starts at 0
    else:
        print("Invalid task number!")

except ValueError: 
    print("Please enter a valid number!")

def main():
    # Initializes empty list to store out tasks
    
    tasks = []

    while True:
        show_menu() 
        choice = input("Enter your choice (1-4): ")
    # Handle each menu option with clear separation of concerns
    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        remove_task(tasks)
    elif choice == "4":
        # Exit the program (Quit)
        print("Thank you for using To-Do_list Manager. Goodbye!")
    
    else: 
        # Handle invalid inputs 
        print("\nInvalid choice! Please enter a number between 1 and 4.")
    
if __name__ == "__main__":
    main()





    
    


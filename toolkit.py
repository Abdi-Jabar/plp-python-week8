import random


# Tool 1: To-Do List
def todo_list():
    tasks = []

    while True:
        print("\n--- To-Do List ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a task: ")
            tasks.append(task)
            print(f"Task added: {task}")

        elif choice == "2":
            if len(tasks) == 0:
                print("Your to-do list is empty.")
            else:
                print("\nYour tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if len(tasks) == 0:
                print("There are no tasks to remove.")
            else:
                print("\nYour tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                try:
                    task_number = int(input("Enter the task number to remove: "))

                    if 1 <= task_number <= len(tasks):
                        removed_task = tasks.pop(task_number - 1)
                        print(f"Removed task: {removed_task}")
                    else:
                        print("That task number does not exist.")

                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            print("Returning to the main menu.")
            break

        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.")


# Tool 2: Simple Calculator
def calculator():
    print("\n--- Simple Calculator ---")

    try:
        first_number = float(input("Enter the first number: "))
        operator = input("Enter an operation (+, -, *, /): ")
        second_number = float(input("Enter the second number: "))

        if operator == "+":
            result = first_number + second_number
            print(f"Result: {result}")

        elif operator == "-":
            result = first_number - second_number
            print(f"Result: {result}")

        elif operator == "*":
            result = first_number * second_number
            print(f"Result: {result}")

        elif operator == "/":
            if second_number == 0:
                print("You cannot divide by zero.")
            else:
                result = first_number / second_number
                print(f"Result: {result}")

        else:
            print(f"Sorry, {operator} is not a valid operation.")

    except ValueError:
        print("Please enter valid numbers.")


# Tool 3: Number Guessing Game
def guessing_game():
    print("\n--- Number Guessing Game ---")
    print("I have chosen a number between 1 and 10.")

    secret_number = random.randint(1, 10)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess the number: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")

            elif guess > secret_number:
                print("Too high! Try again.")

            else:
                print(
                    f"Congratulations! You guessed the number "
                    f"in {attempts} attempts."
                )
                break

        except ValueError:
            print("Please enter a whole number.")


# Main menu
print("\n===================================")
print(" Welcome to My Personal Mini-Toolkit")
print("===================================")

while True:
    print("\nPlease choose a tool:")
    print("1. To-Do List")
    print("2. Simple Calculator")
    print("3. Number Guessing Game")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        todo_list()

    elif choice == "2":
        calculator()

    elif choice == "3":
        guessing_game()

    elif choice == "4":
        print("\nThank you for using My Personal Mini-Toolkit!")
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")
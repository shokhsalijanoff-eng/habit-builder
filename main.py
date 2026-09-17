import json

FILE_NAME = "habits.json"
habits = []
try:
    with open(FILE_NAME, "r") as file:
        habits = json.load(file)
except FileNotFoundError:
    habits = []
while True:
    print("===== HABIT BUILDER =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. Delete Habit")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        habit = input("Enter habit name: ")
        habits.append({"name": habit, "completed": False})
        with open(FILE_NAME, "w") as file:
            json.dump(habits, file, indent=4)
        print("Habit added!")
    elif choice == "2":
        if len(habits) == 0:
            print("No habits yet.")
        else:
             print("Your Habits:")
             for i, habit in enumerate(habits, 1):
                status = "✓" if habit["completed"] else "✗"
                print(i, habit["name"], status)
    elif choice == "3":
        if len(habits) == 0:
            print("No habits yet.")
        else:
            for i, habit in enumerate(habits, 1):
                print(i, habit["name"])

            number = int(input("Which habit did you complete? "))
            habits[number - 1]["completed"] = True
            with open(FILE_NAME, "w") as file:
                json.dump(habits, file, indent=4)
            print("Habit completed!")
    elif choice == "4":
            if len(habits) == 0:
                print("No habits yet.")
            else:
                for i, habit in enumerate(habits, 1):
                    print(i, habit["name"])

                number = int(input("Which habit do you want to delete? "))
                deleted = habits.pop(number - 1)
                with open(FILE_NAME, "w") as file:
                    json.dump(habits, file, indent=4)
                print(deleted["name"], "deleted!")
    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option")

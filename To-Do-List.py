import json
import os
import time

tasks=[]
def addtask():
    os.system('cls')
    id = input("Enter the ID: ")
    task = input("Enter your Task: ")
    status = input("Enter Status(Pending/Done): ")

    try:
        with open("task.txt", "r") as f:
            tasks = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []

    new_task = {
        "ID": id.lower(),
        "Task": task.lower(),
        "Status": status.lower()
    }

    tasks.append(new_task)

    with open("task.txt", "w") as f:
        json.dump(tasks, f, indent=4)

    print("Task Added Successfully!")
    print("Do you want to add more?\n1. Yes\n2. No")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        os.system('cls')
        addtask()
    elif choice == 2:
        os.system('cls')
        main()
    else:
        print("Invalid Input")


def viewtask():
    print("=======================================")
    print(">>>>>>>>>>Showing Tasks<<<<<<<<<<<<<<<<")
    print("=======================================")

    with open("task.txt") as f:
        tasks=json.load(f)
        for item in tasks:
            print(f"ID: {item['ID']} Task: {item['Task']} Status: {item['Status']}")
    input("Press Enter to go back....")
    os.system('cls')
    main()

def deletetask():
    try:
        with open("task.txt", "r") as f:
            tasks = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No tasks found to delete.")
        return

    delete_id = input("Enter the ID of the task to delete: ").lower()
    updated_tasks = [task for task in tasks if task["ID"] != delete_id]

    if len(updated_tasks) == len(tasks):
        print("Task with given ID not found.")
    else:
        with open("task.txt", "w") as f:
            json.dump(updated_tasks, f, indent=4)
        print("Task deleted successfully.")

    print("\nDo you want to delete more?\n1. Yes\n2. No")
    choice = input("Enter your choice: ")
    if choice == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        deletetask()
    elif choice == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        main()  
    else:
        print("Invalid input.")


def updatestatus():
    try:
        with open("task.txt", "r") as f:
            tasks = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No tasks available to update.")
        return

    status_id = input("Enter the ID of the task to update: ").lower()
    new_status = input("Enter new status (pending/done): ").lower()

    task_found = False
    for task in tasks:
        if task["ID"] == status_id:
            task["Status"] = new_status
            task_found = True
            break

    if not task_found:
        print("Task with given ID not found.")
        return

    with open("task.txt", "w") as f:
        json.dump(tasks, f, indent=4)

    print("Status updated successfully.")

def main():
    while True:
        print("========================================")
        print(">>>>>>>>>>>>>TO DO LIST<<<<<<<<<<<<<<<<<")
        print("========================================")
        print("          1. Add a Task                 ")
        print("          2. View All Tasks             ")
        print("          3. Delete Tasks               ")
        print("          4. Update Status              ")
        print("          5. Exit                       ")
        print("========================================")
        choice=int(input("Enter Your choice: "))

        if choice==1:
            addtask()
            os.system('cls')
        elif choice==2:
            viewtask()
            os.system('cls')
        elif choice==3:
            deletetask()
            os.system('cls')
        elif choice==4:
            updatestatus()
            os.system('cls')
        elif choice==5:
            print("Good Bye!")
            break
        else:
            print("Press a valid key")
            os.system('cls')
            main()

main()
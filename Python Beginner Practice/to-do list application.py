# Simple todo list application
import os
todo_path = "todo"
app = True


def show_task():
    with open(todo_path, "r") as file:
        file_content = file.read()
        print(file_content)


def create_task():
    with open(todo_path, "a") as file:
        create_todo = input("What is the task: ")
        file_content = file.write(create_todo + "\n")
        print(f"Added {create_todo} to the list.")


def edit_task():
    with open(todo_path, "r") as file:
        file_content = file.read()
        print(file_content)
    with open(todo_path, "w") as file:
        old_content = input("Write the part that need to be edited: ")
        new_content = input("Now write the modified version: ")
        modified_content = file_content.replace(old_content, new_content)
        file_content = file.write(modified_content)
        print("Updated successfully!")
    with open(todo_path, "r") as file:
        file_content = file.read()
        print(file_content)


def delete_task():
    with open(todo_path, "r") as file:
        file_content = file.read()
        print(file_content)
    with open(todo_path, "w") as file:
        delete = input("Which part need to be deleted: ")
        deleted = file_content.replace(delete, "")
        print("Deleted Successfully.")
    with open(todo_path, "r") as file:
        file_content = file.read()
        print(file_content)


def application():
    app = True
    while app:
        try:
            user_choice = float(input("Welcome to todo list\nChoose an option from below\n 1. Show task\n 2. Create task\n 3. Edit Task\n 4. Delete task\n 5. Exit\nPlease choose an option between (1-5): "))
            if user_choice == 1:
                show_task()
            elif user_choice == 2:
                create_task()
            elif user_choice == 3:
                edit_task()
            elif user_choice == 4:
                delete_task()
            elif user_choice ==5:
                print("Exiting Program.")
                app = False
            else:
                print("Invalid option. Choose again")
        except:
            print("Choose number from (1-5)")



if __name__ == '__main__':
    application()
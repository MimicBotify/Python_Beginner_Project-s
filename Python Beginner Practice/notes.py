#python simple note application
import os


def create_note():
    new_note = input("Enter note title: ")
    new_note = open(new_note, "w")
    new_note.write(input("Start writing you're note: "))


def read_note():
    r_note = input("Enter note title to read: ")
    r_note = open(r_note, "r")
    print(r_note.read())


def edit_note():
    try:
        e_note = input("Enter title name: ")
        with open(e_note, "r") as file:
            file_content = file.read()
            print(file_content)
            old_content = input("Which part need to be edited: ")
            new_content = input("Write the modified version: ")
            modified_version = file_content.replace(old_content, new_content)
        with open(e_note, "w") as file:
            file.write(modified_version)
    except FileNotFoundError:
        print("No note found with that title")


def delete_note():
    d_note = input("Enter the title: ")
    if os.path.exists(d_note):
        os.remove(d_note)
        print(f"Deleted {d_note} note successfully.")
    else:
        print("Note doesn't exist.")


def search_note():
    s_note = input("Search note by title: ")
    if os.path.exists(s_note):
        print(f"Founded {s_note}")
    else:
        print(f"{s_note} is not available.")


def main():
    running = True
    while running:
        print("Choose an option to access the function:\n1. Create new Note\n2. Read Note\n3. Edit Note\n4. Delete Note\n5. Search Note\n6. Exit")
        choice = float(input("Enter option (1-5): "))
        if choice == 1:
            create_note()
        elif choice == 2:
            read_note()
        elif choice == 3:
            edit_note()
        elif choice == 4:
            delete_note()
        elif choice == 5:
            search_note()
        elif choice == 6:
            running = False
            print("Simple note application. Made by Tanvir")
        else:
            print("Invalid Option")


if __name__ == '__main__':
    main()

from tracker import (
    add_study_session,
    view_study_sessions,
    search_by_subject,
    edit_study_session,
    delete_study_session
)

from analysis import weekly_report


def display_menu():
    print("\n===== Student Study Tracker =====")
    print("1. Add Study Session")
    print("2. View Study Sessions")
    print("3. Search by Subject")
    print("4. Weekly Report")
    print("5. Edit Study Session")
    print("6. Delete Study Session")
    print("7. Exit")


def get_user_choice():
    return input("Enter your choice (1-7): ")


def process_choice(choice):

    if choice == "1":
        add_study_session()

    elif choice == "2":
        view_study_sessions()

    elif choice == "3":
        search_by_subject()

    elif choice == "4":
        weekly_report()

    elif choice == "5":
        edit_study_session()

    elif choice == "6":
        delete_study_session()

    elif choice == "7":
        print("\nThank you for using Student Study Tracker!")
        return True

    else:
        print("\nInvalid choice! Please try again.")

    return False


def main():
    while True:
        display_menu()
        choice = get_user_choice()

        if process_choice(choice):
            break


if __name__ == "__main__":
    main()
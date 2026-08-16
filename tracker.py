from storage import load_data, save_data
from datetime import datetime


def add_study_session():

    print("\n===== Add Study Session =====")

    subject = input("Enter Subject: ").strip()

    if not subject:
        print("\nSubject cannot be empty.")
        return

    topic = input("Enter Topic: ").strip()

    if not topic:
        print("\nTopic cannot be empty.")
        return

    try:
        duration = int(input("Enter Duration (minutes): "))

        if duration <= 0:
            print("\nDuration must be greater than 0.")
            return

    except ValueError:
        print("\nInvalid duration! Please enter a number.")
        return

    date = input("Enter Date (YYYY-MM-DD): ").strip()

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("\nInvalid date! Use YYYY-MM-DD format.")
        return

    completed = input("Completed (Y/N): ").strip().upper()

    if completed not in ["Y", "N"]:
        print("\nInvalid status! Use Y or N.")
        return

    session = {
        "subject": subject,
        "topic": topic,
        "duration": duration,
        "date": date,
        "completed": completed
    }

    sessions = load_data()
    sessions.append(session)
    save_data(sessions)

    print("\nStudy session added successfully!")


def view_study_sessions():

    sessions = load_data()

    if len(sessions) == 0:
        print("\nNo study sessions found.")
        return

    print("\n===== Study Sessions =====")

    for index, session in enumerate(sessions, start=1):

        subject = session.get("subject", "Unknown")
        topic = session.get("topic", "Unknown")
        duration = session.get("duration", 0)
        date = session.get("date", "Unknown")
        completed = session.get("completed", "N")

        print(f"\nSession {index}")
        print("-" * 30)
        print(f"Subject   : {subject}")
        print(f"Topic     : {topic}")
        print(f"Duration  : {duration} mins")
        print(f"Date      : {date}")
        print(f"Completed : {completed}")


def search_by_subject():

    print("\n===== Search by Subject =====")

    search_subject = input("Enter Subject: ").strip().lower()

    if not search_subject:
        print("\nSubject cannot be empty.")
        return

    sessions = load_data()

    if len(sessions) == 0:
        print("\nNo study sessions found.")
        return

    found_count = 0

    for index, session in enumerate(sessions, start=1):

        subject = session.get("subject", "Unknown")

        if subject.strip().lower() == search_subject:

            found_count += 1

            topic = session.get("topic", "Unknown")
            duration = session.get("duration", 0)
            date = session.get("date", "Unknown")
            completed = session.get("completed", "N")

            print(f"\nSession {index}")
            print("-" * 30)
            print(f"Subject   : {subject}")
            print(f"Topic     : {topic}")
            print(f"Duration  : {duration} mins")
            print(f"Date      : {date}")
            print(f"Completed : {completed}")

    if found_count == 0:
        print(
            f"\nNo study sessions found for "
            f"'{search_subject}'."
        )
    else:
        print(f"\nFound {found_count} session(s).")


def edit_study_session():

    print("\n===== Edit Study Session =====")

    sessions = load_data()

    if len(sessions) == 0:
        print("\nNo study sessions found.")
        return

    for index, session in enumerate(sessions, start=1):

        subject = session.get("subject", "Unknown")
        topic = session.get("topic", "Unknown")
        duration = session.get("duration", 0)

        print(
            f"{index}. "
            f"{subject} - "
            f"{topic} - "
            f"{duration} mins"
        )

    try:
        choice = int(input("\nEnter session number to edit: "))
    except ValueError:
        print("\nInvalid input! Please enter a number.")
        return

    if choice < 1 or choice > len(sessions):
        print("\nInvalid session number.")
        return

    index = choice - 1
    session = sessions[index]

    current_subject = session.get("subject", "Unknown")
    current_topic = session.get("topic", "Unknown")
    current_duration = session.get("duration", 0)
    current_date = session.get("date", "Unknown")
    current_completed = session.get("completed", "N")

    print("\nPress Enter to keep the existing value.")

    new_subject = input(
        f"New Subject [{current_subject}]: "
    ).strip()

    if new_subject:
        session["subject"] = new_subject

    new_topic = input(
        f"New Topic [{current_topic}]: "
    ).strip()

    if new_topic:
        session["topic"] = new_topic

    new_duration = input(
        f"New Duration [{current_duration}]: "
    ).strip()

    if new_duration:

        try:
            duration = int(new_duration)

            if duration <= 0:
                print(
                    "\nDuration must be greater than 0. "
                    "Keeping old duration."
                )
            else:
                session["duration"] = duration

        except ValueError:
            print(
                "\nInvalid duration. "
                "Keeping old duration."
            )

    new_date = input(
        f"New Date [{current_date}]: "
    ).strip()

    if new_date:

        try:
            datetime.strptime(new_date, "%Y-%m-%d")
            session["date"] = new_date

        except ValueError:
            print(
                "\nInvalid date. "
                "Keeping old date."
            )

    new_completed = input(
        f"Completed (Y/N) [{current_completed}]: "
    ).strip().upper()

    if new_completed in ["Y", "N"]:
        session["completed"] = new_completed

    elif new_completed:
        print(
            "\nInvalid completion status. "
            "Keeping old status."
        )

    save_data(sessions)

    print("\nStudy session updated successfully!")


def delete_study_session():

    print("\n===== Delete Study Session =====")

    sessions = load_data()

    if len(sessions) == 0:
        print("\nNo study sessions found.")
        return

    for index, session in enumerate(sessions, start=1):

        subject = session.get("subject", "Unknown")
        topic = session.get("topic", "Unknown")
        duration = session.get("duration", 0)

        print(
            f"{index}. "
            f"{subject} - "
            f"{topic} - "
            f"{duration} mins"
        )

    try:
        choice = int(
            input("\nEnter session number to delete: ")
        )
    except ValueError:
        print(
            "\nInvalid input! "
            "Please enter a number."
        )
        return

    if choice < 1 or choice > len(sessions):
        print("\nInvalid session number.")
        return

    index = choice - 1
    selected_session = sessions[index]

    subject = selected_session.get("subject", "Unknown")
    topic = selected_session.get("topic", "Unknown")
    duration = selected_session.get("duration", 0)
    date = selected_session.get("date", "Unknown")

    print("\nSelected Session:")
    print(f"Subject   : {subject}")
    print(f"Topic     : {topic}")
    print(f"Duration  : {duration} mins")
    print(f"Date      : {date}")

    confirmation = input(
        "\nAre you sure you want to delete? (Y/N): "
    ).strip().upper()

    if confirmation == "Y":

        del sessions[index]
        save_data(sessions)

        print("\nStudy session deleted successfully!")

    else:
        print("\nDelete cancelled.")
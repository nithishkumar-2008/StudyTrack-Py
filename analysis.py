from storage import load_data
from datetime import datetime, timedelta


def get_last_7_days_sessions():
    sessions = load_data()

    today = datetime.today().date()
    seven_days_ago = today - timedelta(days=6)

    recent_sessions = []

    for session in sessions:
        try:
            session_date = datetime.strptime(
                session.get("date", ""),
                "%Y-%m-%d"
            ).date()

        except ValueError:
            print(
                f"\nSkipping invalid session date: "
                f"{session.get('date', 'Unknown')}"
            )
            continue

        if seven_days_ago <= session_date <= today:
            recent_sessions.append(session)

    return recent_sessions


def weekly_report():
    sessions = get_last_7_days_sessions()

    if not sessions:
        print("\nNo study sessions found in the last 7 days.")
        return

    total_sessions = len(sessions)
    total_duration = 0
    completed_count = 0
    subject_time = {}

    for session in sessions:
        duration = session.get("duration", 0)
        subject = session.get("subject", "Unknown")
        completed = session.get("completed", "N")

        total_duration += duration

        if completed.strip().upper() == "Y":
            completed_count += 1

        if subject in subject_time:
            subject_time[subject] += duration
        else:
            subject_time[subject] = duration

    if not subject_time:
        print("\nNo subject data available.")
        return

    pending_count = total_sessions - completed_count

    completion_rate = (
        completed_count / total_sessions
    ) * 100

    average_time = (
        total_duration / total_sessions
    )

    most_studied_subject = max(
        subject_time,
        key=subject_time.get
    )

    today = datetime.today().date()
    seven_days_ago = today - timedelta(days=6)

    print("\n===== WEEKLY PERFORMANCE REPORT =====")

    print(
        f"\nPeriod: "
        f"{seven_days_ago} to {today}"
    )

    print(
        f"\nTotal Sessions     : "
        f"{total_sessions}"
    )

    print(
        f"Total Study Time   : "
        f"{total_duration} minutes"
    )

    print(
        f"Completed Sessions : "
        f"{completed_count}"
    )

    print(
        f"Pending Sessions   : "
        f"{pending_count}"
    )

    print(
        f"Completion Rate    : "
        f"{completion_rate:.2f}%"
    )

    print(
        f"Average Study Time : "
        f"{average_time:.2f} minutes"
    )

    print("\n===== SUBJECT ANALYSIS =====")

    for subject, duration in subject_time.items():
        print(
            f"{subject:<25} : "
            f"{duration} minutes"
        )

    print("\n===== MOST STUDIED SUBJECT =====")

    print(
        f"{most_studied_subject} - "
        f"{subject_time[most_studied_subject]} minutes"
    )
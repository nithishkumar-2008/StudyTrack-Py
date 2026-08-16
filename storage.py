import json


def save_data(study_sessions):

    try:

        with open("data.json", "w") as file:
            json.dump(
                study_sessions,
                file,
                indent=4
            )

    except OSError as error:

        print(f"\nError saving data: {error}")


def load_data():

    try:

        with open("data.json", "r") as file:
            data = json.load(file)

        if not isinstance(data, list):
            print("\nError: data.json must contain a list.")
            return []

        return data

    except FileNotFoundError:

        return []

    except json.JSONDecodeError as error:

        print(
            f"\nError: data.json contains invalid JSON: {error}"
        )

        return []

    except OSError as error:

        print(f"\nError reading data: {error}")
        return []
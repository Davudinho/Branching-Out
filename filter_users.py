import json
import os


# Basisverzeichnis des Skripts ermitteln
script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, "users.json")

with open(json_path, "r", encoding="utf-8") as f:
    content = f.read()
    print("RAW JSON:", repr(content))  # Zeigt dir, was Python wirklich liest

print("JSON Path:", json_path)

def filter_users_by_name(name):
    """Filter users by exact name match (case-insensitive)."""
    with open(json_path, "r", encoding="utf-8") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    if filtered_users:
        for user in filtered_users:
            print(user)
    else:
        print(f"No users found with name '{name}'.")


def filter_users_by_age(min_age=None, max_age=None):
    """Filter users by minimum and/or maximum age."""
    with open(json_path, "r", encoding="utf-8") as file:
        users = json.load(file)

    filtered_users = users

    if min_age is not None:
        filtered_users = [user for user in filtered_users if user["age"] >= min_age]
    if max_age is not None:
        filtered_users = [user for user in filtered_users if user["age"] <= max_age]

    if filtered_users:
        for user in filtered_users:
            print(user)
    else:
        print("No users found in the specified age range.")


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (name / age): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)

    elif filter_option == "age":
        min_age_input = input("Enter minimum age (or leave empty): ").strip()
        max_age_input = input("Enter maximum age (or leave empty): ").strip()

        min_age = int(min_age_input) if min_age_input else None
        max_age = int(max_age_input) if max_age_input else None

        filter_users_by_age(min_age, max_age)

    else:
        print("Filtering by that option is not yet supported.")

# System platform and version
import platform
print(platform.platform())

# Colors
from colorama import Fore, Style

# dotenv - library that allows to store data (ex passwords, API keys, file paths) in .env file for Python project
from dotenv import load_dotenv
import os
load_dotenv("data/.env")

HOTEL_NAME = os.getenv("HOTEL_NAME")            # os.getenv() - function of Python to get a value from .env
ADMIN_NAME = os.getenv("ADMIN_NAME")
MAX_ROOMS = int(os.getenv("MAX_ROOMS"))

# Decorator
import webbrowser                               # module for opening website links

def decorator(func):
    def wrapper(url):
        if url.startswith("https://www.booking.com/"):
            print("✅ Link opened")
            return func(url)
        else:
            print("❌ Incorrect URL")
    return wrapper

# JSON
import json

file = open("data/all_rooms.json", "r")
all_rooms = json.load(file)                         # Load rooms
file.close()

file = open("data/guest_profiles.json", "r")
guest_profiles = json.load(file)                    # Load guests
file.close()



# =====================
# OOP - Simple Room class example
# =====================

# class Room:
#     def __init__(self, number, room_type, floor, status):              # A class constructor in OOP using __init__
#         self.number = number
#         self.room_type = room_type
#         self.floor = floor
#         self.status = status
#
#     def show_info(self):
#         print(f"Room: {self.number}")
#         print(f"Type: {self.room_type}")
#         print(f"Floor: {self.floor}")
#         print(f"Status: {self.status}")
#
# room = Room("#1", "Standard", 1, "Occupied")
# room.show_info()

# =====================
# OOP - End of example
# =====================



def save_rooms():
    file = open("data/all_rooms.json", "w")
    json.dump(all_rooms, file, indent=4)            # Save rooms
    file.close()

def save_guest_profiles():
    file = open("data/guest_profiles.json", "w")
    json.dump(guest_profiles, file, indent=4)   # Save guests
    file.close()

# Activity logs
from datetime import datetime
def create_log(message):
    file = open("data/activity_log.txt", "a")

    time = datetime.now()
    file.write(f"{time} - {message}\n")
    file.close()



# Main menu
def main_menu():
    while True:
        print("\n" + "="*35)
        print(f"🏨 {HOTEL_NAME}")
        print("="*35)
        print("1. 🔍 Find guest profile")
        print("2. 🏠 Find room")
        print("3. 🙋 See all guests")
        print("4. 💤️ See all rooms")
        print("5. 🌐 Open hotel profile on Booking.com")
        print("6. ❌ Exit")
        print("-"*35)
        choice = "".join(input("Choose option (1-5): ").lower().split())
        
        if choice == "1":
            find_guest_profile()
        elif choice == "2":
            find_room()
        elif choice == "3":
            all_guests()
        elif choice == "4":
            see_all_rooms()
        elif choice == "5":
            @decorator
            def open_url(url):
                webbrowser.open(url)
            open_url("https://www.booking.com/")

        elif choice == "6" or choice.lower() == "e":
            print(Fore.CYAN + "\nThank you! Goodbye! 👋" + Style.RESET_ALL)
            break
        else:
            print("\n❌ Invalid option. Try again.")



# Search of guest profiles
def find_guest_profile():
    while True:
            search_name = " ".join(input("\nType guest name to search profile: \n"
                                         "\n"
                                         "or \n"
                                         "\n"
                                         "Type 'a' to add a comment: \n"
                                         "Type 'r' to read all comments: \n"
                                         "Type 'e' to go back: ").split()).lower().replace(" ", "_")
            print("\n")
            if search_name == "a":
                add_comment()
                continue
            elif search_name == "r":
                read_comments()
                continue
            elif search_name == "e":
                print("Returning to main menu..." )
                return

            elif search_name in guest_profiles:
                print("\n".join(guest_profiles[search_name].values()))

            else:
                print("❌ Value does not exist. Please try again. ")



# See all inhouse guests
def all_guests():
        print()
        all_guests = ["James Smith", "Oliver Brown", "Jack Wilson", "Harry Taylor",
                              "Noah Davis",
                              "Liam Miller",
                              "Ethan Moore", "Lucas White", "Henry Clark", "Leo Harris", "Emily Johnson",
                              "Sophia Walker",
                              "Olivia Hall",
                              "Emma Young", "Mia Allen", "Grace King", "Chloe Scott", "Lily Green", "Ella Baker",
                              "Ava Adams", "Michael Smith", "Emma Wilson"]
        print("\n".join(all_guests))
        print()
        find_guest_profile()

# Adding notes to comments.txt
def comments_menu():
        while True:
            choice = " ".join(input("Type 'a' to add a comment: \n"
                                    "Type 'r' to read all comments: \n"
                                    "Type 'e' to go back: ").split()).lower()
            if choice == "a":
                add_comment()
            elif choice == "r":
                read_comments()
            elif choice.lower() == "e":
                print("Returning...\n")
                return
            else:
                print("❌ Value does not exist. Please try again. \n")

def add_comment():
            comment_name = " ".join(input("Type guest name: ").split()).lower()
            if comment_name == "e":
                print("Returning...\n")
                return

            room_input = " ".join(input("Type room number with # (ex. #1, #2 etc): ").split())
            if room_input == "e":
                print("Returning...\n")
                return
            if "#" not in room_input:
                print("❌ Please enter room number with # (example: #1)\n")
                return add_comment()
            elif not room_input[1:].isdigit():
                print("❌ Room number must contain digits only with # (example: #1)\n")
                return add_comment()
            if room_input not in all_rooms:
                print("❌ Room does not exist. \n")
                return(add_comment())

            comment_comment = " ".join(input("Type comment: ").split()).lower()
            if comment_comment == "e":
                print("Returning...\n")
                return
            print("Comment has been recorded✅ \n")

            file = open("/AI Hotel Assistant/comments.txt", "a")
            from datetime import datetime
            time = datetime.now()
            file.write(f"{time} - \n")

            file.write(f"Guest: {comment_name}\n")
            file.write(f"Room: {room_input}\n")
            file.write(f"Comment: {comment_comment}\n")
            file.write("---------------------------\n")
            file.close()

            create_log(f"Note added for {comment_name}, room number: {room_input}, comment: {comment_comment}")          #log for activity_log.txt
            print()

def read_comments():
            try:
                with open("/Hotel Management System/data/comments.txt", "r") as file:
                    comments = file.read()

                    if comments:
                        print()
                        print(comments)
                    else:
                        print()
                        print("❌ No comments yet.")
                        print()
            except FileNotFoundError:
                print("❌ No file with comments found.")



# change status
def change_status():                                                                          #function to change room status in console
   while True:
        room_number = " ".join(input("Type room number with # (#1, #2 etc): ").split()).lower()

        if room_number == "e":
            print("Returning to main menu...")
            return(main_menu())
        elif "#" not in room_number:
            print("❌ Please enter room number with # (example: #1)")
            return(change_status())
        elif room_number not in all_rooms:
            print("❌ Room number does not exist")
            return(change_status())
        while True:
            print("1 - Available")
            print("2 - Occupied")
            print("3 - Maintenance")
            new_status = " ".join(input("Choose new status (ex. '1'): ").split()).lower()

            statuses = {"1": "Available",
                        "2": "Occupied",
                        "3": "Maintenance"}
            if new_status == "e":
                print("Returning...")
                return(change_status())
            if new_status in statuses:
                break
            print("\n ❌ Please choose status from the list (example: '1') \n")

        old_status = all_rooms[room_number]["status"]                                                     # old_status is needed for activity_log.txt
        new_status = statuses[new_status]
        all_rooms[room_number]["status"] = new_status

        create_log(f"Room {room_number} status changed from {old_status} to {new_status}")                # log for activity_log.txt
        save_rooms()                                                                                      # Save rooms in JSON

        print()
        print("Status updated!")
        return(change_status())



def find_room():
    print("\n=== ROOM SEARCH ===")
    print("1. Standard")
    print("2. Deluxe")
    print("3. Suite")
    print("4. See all rooms")
    print("5. Update room status")

    choice = " ".join(input("Select room type (or 'e' to go back): ").split()).lower()
    print()

    if choice.lower() == "e":
        print("Returning to main menu...")
        return

    if choice == "1":
        selected_room_type = "Standard"
    elif choice == "2":
        selected_room_type = "Deluxe"
    elif choice == "3":
        selected_room_type = "Suite"
    elif choice == "4":
        print("See all rooms:")
        print()
        see_all_rooms()
        return (find_room())
    elif choice == "5":
        print("Update room status:")
        print()
        change_status()
    else:
        print("❌ Invalid choice.")
        return (find_room())

    available = []
    for room, info in all_rooms.items():
        if info["room_type"] == selected_room_type and info["status"] == "Available":
            available.append(room)
    if len(available) > 0:
        print(f"✅Available {selected_room_type} rooms:")
        print(" ".join(available))
    else:
        print(f"❌ All {selected_room_type} rooms are occupied.")

    while True:
        next_value = " ".join(input("Type 'e' to go back): ").split()).lower()
        if next_value.lower() == "e":
            print("Returning to main menu...")
            return (find_room())



# See all rooms
def see_all_rooms():
        for room, info in all_rooms.items():
            print("Room: " + room)
            print("Type: " + (info["room_type"]))
            print("Floor: " + str(info["floor"]))
            if info["status"] == "Available":
                print("Status: " +(info["status"] + "✅"))
            elif info["status"] == "Maintenance":
                print("Status: " +(info["status"] + "🟡"))
            else:
                print("Status: " + (info["status"] + "❌"))
            print()

        while True:
            choice = " ".join(input("Type '1' to update room status: \n"
                                    "Type 'e' to go back): ").split()).lower()
            if choice == "1":
                print()
                change_status()
                return (find_room())
            elif choice.lower() == "e":
                print("Returning to main menu...")
                return
            else:
                print("❌ Value does not exist. Please try again.")



# Launch the program
main_menu()

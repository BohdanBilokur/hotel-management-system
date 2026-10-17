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

from datetime import datetime
def create_log(message):
    file = open("data/activity_log.txt", "a")

    time = datetime.now()
    file.write(f"{time} - {message}\n")
    file.close()



# Guests menu section
def guests_menu():
    while True:
        print("\n=== GUESTS ===")
        print("1. Find guest profile")
        print("2. See all guests")
        print("3. Comments")
        print("e. Go back")

        choice = " ".join(input("Choose option: ").split()).lower()

        if choice == "1":
            find_guest_profile()
        elif choice == "2":
            all_guests()
        elif choice == "3":
            comments_menu()
        elif choice == "e":
            print("Returning...")
            return
        else:
            print("❌ Invalid option. Try again.")

# Rooms menu section
def rooms_menu():
    while True:
        print("\n=== ROOMS ===")
        print("1. Find room")
        print("2. See all rooms")
        print("3. Update room status")
        print("e. Go back")

        choice = " ".join(input("Choose option: ").split()).lower()

        if choice == "1":
            find_room()
        elif choice == "2":
            see_all_rooms()
        elif choice == "3":
            change_status()
        elif choice == "e":
            print("Returning...")
            return
        else:
            print("❌ Invalid option. Try again.")

# Check-in / Check out menu section
def check_in_out_menu():
    while True:
        print("\n=== CHECK-IN / CHECK-OUT ===")
        print("1. Check-in")
        print("2. Check-out")
        print("e. Go back")

        choice = " ".join(input("Choose option: ").split()).lower()

        if choice == "1":
            check_in()
        elif choice == "2":
            check_out()
        elif choice == "e":
            print("Returning...")
            return
        else:
            print("❌ Invalid option. Try again.")

# Activity Log Viewer section (reads and shows all activity Logs)
def read_activity_log():
    try:
        file = open("data/activity_log.txt", "r")
        logs = file.read()
        file.close()

        if logs:
            print()
            print(logs)

            while True:
                choice = input("Type 'e' to go back: ").strip().lower()

                if choice == "e":
                    print("Returning...")
                    return
                else:
                    print("❌ Please type 'e' to go back.")
        else:
            print()
            print("❌ No activity logs yet.")

    except FileNotFoundError:
        print("❌ Activity log file not found.")



# Main menu
def main_menu():
    while True:
        print("\n" + "="*35)
        print(f"🏨 {HOTEL_NAME}")
        print("="*35)
        print("1. 👤 Guests")
        print("2. 🏠 Rooms")
        print("3. 🛎️ Check-in /️ Сheck-out")
        print("4. 📋 Activity log")
        print("5. 🌐 Open Booking.com")
        print("6. ❌ Exit")
        print("-"*35)
        choice = "".join(input("Choose option (1-6): ").lower().split())
        
        if choice == "1":
            guests_menu()
        elif choice == "2":
            rooms_menu()
        elif choice == "3":
            check_in_out_menu()
        elif choice == "4":
            read_activity_log()
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
                                         "Type 'e' to go back: ").split()).lower()
            print("\n")

            if search_name == "":
                print("❌ Please enter a guest name.")
                continue
            if search_name == "a":
                add_comment()
                continue
            elif search_name == "r":
                read_comments()
                continue
            elif search_name == "e":
                print("Returning to main menu..." )
                return

            found = False

            for guest in guest_profiles:
                if search_name.replace(" ", "_") in guest:
                    print("\n".join(guest_profiles[guest].values()))
                    print()
                    found = True
            if found == False:
                print ("❌ Value does not exist. Please try again.")



# See all inhouse guests
def all_guests():
        print()
        all_guests = []
        guest_count = 0

        for guest in guest_profiles:
            room = guest_profiles[guest]["room number"]
            name = guest_profiles[guest]["name"]
            name = name.replace("Full name: ", "")

            if room != "Room number: ":
                guest_count += 1

                room = room.replace("Room number: ", "#")
                room_type = all_rooms[room]["room_type"]
                status = all_rooms[room]["status"]
                check_in_date = guest_profiles[guest]["check-in date"]
                booking_source = guest_profiles[guest]["booking source"]
                check_out_date = guest_profiles[guest]["check-out date"]

                all_guests.append(
                    f"{name}\n"
                    f"Room: {room}\n"
                    f"Room type: {room_type}\n"
                    f"Room status: {status}\n"
                    f"{check_in_date}\n"
                    f"{check_out_date}\n"
                    f"{booking_source}\n")

        print(f"Total in-house guests: {guest_count}")
        print()
        print("\n".join(all_guests))
        if guest_count == 0:
            print("❌ No guests are currently checked in.")

        while True:
            print()
            choice = " ".join(input("Type 'e' to go back: ").split()).lower()

            if choice == "e":
                print("Returning...\n")
                return
            else:
                print("❌ Please type 'e' to go back")



# Adding notes to comments.txt
def comments_menu():
        while True:
            print()
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

            file = open("data/comments.txt", "a")
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
                with open("data/comments.txt", "r") as file:
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
def change_status():                                                                          # function to change room status in console
   while True:
        room_number = " ".join(input("Type room number with # (ex. #1, #2 etc): \n"
                                     "Type 'e' to go back: ").split()).lower()
        if room_number == "e":
            print("Returning to main menu...")
            return(main_menu())
        elif "#" not in room_number:
            print("❌ Please enter room number with # (example: #1)")
            return(change_status())
        elif room_number not in all_rooms:
            print("❌ Room number does not exist")
            return(change_status())

        room_number_for_guest = room_number.replace("#", "")                          # removes "#" from the room number for guest search

        guest_found = False

        for guest in guest_profiles:
            room = guest_profiles[guest]["room number"]
            if room == "Room number: " + room_number_for_guest:                                 # this checks if there is a guest in a chosen room
                print()
                print(guest_profiles[guest]["name"])
                guest_found = True

        while True:
            print()
            current_status = all_rooms[room_number]["status"]                                   # Shows current status of the room

            if guest_found == True and current_status == "Available":
                print("⚠️ Guest exists, but room is marked as Available.")
            if guest_found == False and current_status == "Occupied":
                print("⚠️ Room is Occupied, but no guest was found.")
            if guest_found == True and current_status == "Maintenance":
                print("⚠️ Guest exists, but room is under maintenance.")

            print(f"Current status: {current_status}")
            print()

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
                if statuses[new_status] == current_status:
                    print()
                    print(f"❌ Room {room_number} is already {current_status}.")
                    continue

                if guest_found == True and statuses[new_status] == "Available":
                    print("⚠️ There is a guest in this room.")

                    confirm = input("Continue? (y/n): ").lower()

                    if confirm == "n":
                        continue
                    if confirm != "y":
                        print("❌ Please type 'y' or 'n'.")
                        continue

                if guest_found == False and statuses[new_status] == "Occupied":
                    print()
                    print("⚠️ No guest was found in this room.")
                break

            else:
                print("\n ❌ Please choose status from the list (example: '1') \n")

        old_status = current_status                                                                       # old_status is needed for activity_log.txt
        new_status = statuses[new_status]
        all_rooms[room_number]["status"] = new_status

        create_log(f"Room {room_number} status changed from {old_status} to {new_status}")                # log for activity_log.txt
        save_rooms()                                                                                      # Save rooms in JSON

        print(f"✅ Done! Room {room_number} status changed from {old_status} to {new_status}.")

        print()
        return(change_status())



def check_in():
    while True:
        guest_name = " ".join(input("Type guest name (or 'e' to go back): ").split()).lower()

        if guest_name == "e":
            print("Returning to main menu...")
            return

        found_guests = []
        for guest in guest_profiles:
            if guest_name.replace(" ", "_") in guest:
                found_guests.append(guest)

        if len(found_guests) == 0:
            print()
            print("❌ Guest not found.")
            continue

        if len(found_guests) == 1:
            selected_guest = found_guests[0]

        else:
            print()
            print("Multiple guests found:")

            for number in range(len(found_guests)):
                guest = found_guests[number]
                print(f"{number + 1}. {guest_profiles[guest]['name']}")

        while True:
            choice = input("Choose guest number: ").strip()

            if not choice.isdigit():
                print("❌ Please choose a number from the list.")
                continue

            choice = int(choice)

            if choice < 1 or choice > len(found_guests):
                print("❌ Please choose a number from the list.")
                continue

            selected_guest = found_guests[choice - 1]
            break

            selected_guest = found_guests[choice - 1]

        current_room = guest_profiles[selected_guest]["room number"]
        if current_room != "Room number: ":
            current_room = current_room.replace("Room number: ", "#")
            print(f"❌ Guest is already assigned to room {current_room}.")
            return

        standard_rooms = []
        deluxe_rooms = []
        suite_rooms =    []

        for room, info in all_rooms.items():
            if info["status"] == "Available":
                if info["room_type"] == "Standard":
                    standard_rooms.append(room)
                elif info["room_type"] == "Deluxe":
                    deluxe_rooms.append(room)
                elif info["room_type"] == "Suite":
                    suite_rooms.append(room)

        room_type = " ".join(input("Choose room type:\n"
                                   "1. Standard\n"
                                   "2. Deluxe\n"
                                   "3. Suite\n"
                                   "Choose option: ").split()).lower()
        if room_type == "e":
            print("Returning...")
            return
        if room_type == "1":
            room_type = "Standard"
        elif room_type == "2":
            room_type = "Deluxe"
        elif room_type == "3":
            room_type = "Suite"
        else:
            print("❌ Please choose 1, 2 or 3.")
            continue

        if room_type == "Standard":
            available_rooms = standard_rooms
        elif room_type == "Deluxe":
            available_rooms = deluxe_rooms
        elif room_type == "Suite":
            available_rooms = suite_rooms

        if len(available_rooms) == 0:
            print()
            print(f"❌ No available {room_type} rooms.")
            continue

        print()
        print(f"Available {room_type} rooms:")
        print(" ".join(available_rooms))
        print(f"Total available {room_type} rooms: {len(available_rooms)}")

        room_number = " ".join(input("Choose room number (or 'e' to go back): ").split()).lower()
        if room_number == "e":
            print("Returning...")
            return
        if room_number not in available_rooms:
            print("❌ Please choose a room from the available list.")
            continue

        all_rooms[room_number]["status"] = "Occupied"
        guest_profiles[selected_guest]["room number"] = "Room number: " + room_number.replace("#", "")

        check_in_date = datetime.now().strftime("%Y-%m-%d")                                                                 # records date and time of the check in
        guest_profiles[selected_guest]["check-in date"] = "Check-in date: " + check_in_date
        guest_profiles[selected_guest]["check-out date"] = "Check-out date: "

        create_log(f"Guest {guest_profiles[selected_guest]['name']} checked in to room {room_number}")

        save_rooms()
        save_guest_profiles()

        print()
        print("✅ Check-in completed.")
        print(f"Guest: {guest_profiles[selected_guest]['name']}")
        print(f"Room: {room_number}")
        print(f"Room type: {room_type}")
        print(f"Check-in date: {check_in_date}")
        return ()



def check_out():
    while True:
        print()
        search_type = " ".join(input("Choose option (1 or 2) \n"
                                    "1. Search by guest name: \n"
                                    "2. Search by room number: " ).split()).lower()

        if search_type == "e":
            print("Returning to main menu...")
            return
        if search_type == "1":
            guest_name = " ".join(input("Type guest name: ").split()).lower()
            if guest_name == "e":
                print("Returning to main menu...")
                return

        elif search_type == "2":
            room_number = " ".join(input("Type room number with # (ex. #8) or 'e' to go back: ").split()).lower()
            if room_number == "e":
                print("Returning to main menu...")
                return
            if "#" not in room_number:
                print("❌ Please enter room number with # (example: #8)")
                return
            if room_number not in all_rooms:
                print("❌ Room number does not exist.")
                return
        else:
            print("❌ Please choose '1' or '2'.")
            continue

        found = False

        for guest in guest_profiles:
            if search_type == "1" and guest_name.replace(" ", "_") in guest:
                print()
                print(guest_profiles[guest]["name"])
                found = True
                selected_guest = guest

            elif search_type == "2":
                guest_room = guest_profiles[guest]["room number"]
                guest_room = guest_room.replace("Room number: ", "#")

                if guest_room == room_number:
                    print(guest_profiles[guest]["name"])
                    found = True
                    selected_guest = guest

        if found == False:
            print()

            if search_type == "2":
                print(f"❌ No guest found in room {room_number}.")
            else:
                print("❌ Guest not found.")
            return

        if search_type == "1":
            room_number = guest_profiles[selected_guest]["room number"]
            room_number = room_number.replace("Room number: ", "#")

        if room_number == "#":
            print()
            print("❌ Guest is not assigned to a room.")
            return
        if room_number not in all_rooms:
            print("❌ Room number does not exist.")
            return

        current_status = all_rooms[room_number]["status"]

        if current_status != "Occupied":
            print()
            print(f"❌ Room {room_number} is not marked as Occupied.")
            return

        print()
        print(f"Guest: {guest_profiles[selected_guest]['name']}")
        print(f"Room: {room_number}")

        while True:
            confirm = input("Confirm check-out? (y/n): ").lower()

            if confirm == "y":
                break
            if confirm == "n":
                print("Check-out cancelled.")
                return

            print("❌ Please type 'y' or 'n'.")

        all_rooms[room_number]["status"] = "Available"
        guest_profiles[selected_guest]["room number"] = "Room number: "                             # it clears the guest’s assigned room number after check-out

        check_out_date = datetime.now().strftime("%Y-%m-%d")                                        # time and date of the check-out
        guest_profiles[selected_guest]["check-out date"] = "Check-out date: " + check_out_date

        create_log(f"Guest {guest_profiles[selected_guest]['name']} checked out from room {room_number}")

        save_rooms()
        save_guest_profiles()

        print()
        print("✅ Check-out completed.")
        print(f"Guest: {guest_profiles[selected_guest]['name']}")
        print(f"Room: {room_number}")
        print(f"Check-out date: {check_out_date}")
        print("Room is now available.")
        return ()



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
        return
    else:
        print("❌ Invalid choice.")
        return (find_room())

    available = []
    for room, info in all_rooms.items():
        if info["room_type"] == selected_room_type and info["status"] == "Available":
            available.append(room)
    if len(available) > 0:
        print(f"✅ Available {selected_room_type} rooms:")
        print(" ".join(available))
        print()
        print(f"Total available {selected_room_type} rooms: {len(available)}")
    else:
        print(f"❌ No available {selected_room_type} rooms.")

    while True:
        next_value = " ".join(input("Type 'e' to go back): ").split()).lower()
        if next_value.lower() == "e":
            print("Returning to main menu...")
            return (find_room())
        else:
            print("❌ Please type 'e' to go back.")



# See all rooms
def see_all_rooms():
        print()
        print(f"{'Room':<8}{'Type':<12}{'Floor':<8}{'Status'}")
        print("-" * 48)

        for room, info in all_rooms.items():
            if info["status"] == "Available":
                status = info["status"] + "✅"
            elif info["status"] == "Maintenance":
                status = info["status"] + "🟡"
            else:
                status = info["status"] + "❌"

            print(f"{room:<8}{info['room_type']:<12}{info['floor']:<8}{status}")
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

# Class: CSE 1321L
# Section: W04
# Term: Spring 2025
# Instructor: Nalamati
# Name: Zenzele Broomfield
# Lab: 08

def main():
    mailing_list = []

    while True:
        print("\n[Mailing List]")
        print("1 - Add email")
        print("2 - Delete email")
        print("3 - List all emails")
        print("4 - Quit")

        choice = input("Make your selection: ")

        if choice == "1":
            email = input("Enter the email to be added: ")
            mailing_list.append(email)
            print("Email added to mailing list.")

        elif choice == "2":
            email = input("Enter the email to be removed: ")
            if email in mailing_list:
                mailing_list.remove(email)
                print(f"{email} has been removed from the mailing list.")
            else:
                print(f"No such email in mailing list: {email}")

        elif choice == "3":
            if mailing_list:
                for email in mailing_list:
                    print(email)
            else:
                print("Mailing list is empty.")

        elif choice == "4":
            print("Shutting down...")
            break

        else:
            print("Invalid selection. Please choose a number between 1 and 4.")

if __name__ == "__main__":
    main()

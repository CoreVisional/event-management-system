"""Main module for the event management system."""

# ALEX CHIEW (TP056952)
# ACHREEN KAUR (TP063334)

import admin
import client
import sys
from datetime import datetime


def display_main_menu() -> list:
    """
    Display the main menu screen.

    :return: list[str]
    """
    menu_list = [
        "View as Guest",
        "Login as Existing User",
        "Exit",
    ]
    print("\n" + ("=" * 50))
    print("Welcome to Asian Event Management Services (AEMS)!")
    print("=" * 50)
    print("\nSelect one of the options below to access the system:")
    return menu_list


def display_login_menu() -> list:
    """
    Display the register/login menu.

    :return: list[str]
    """
    menu_list = [
        "Login as Existing Member",
        "Login as Administrator (Admin Only)",
        "Back to Main Menu",
    ]
    return menu_list


def display_guest_menu() -> list:
    """
    Display the guest menu for users who wish to view and register as member.

    :return: list[str]
    """
    menu_list = [
        "Register as New Member",
        "View Events",
        "Back to Main Menu",
        "Exit",
    ]
    return menu_list


def ask_user_yes_no(yes_no_question: str) -> bool:
    """
    Simplify if/else to determine the correct answers from the user input.

    :param yes_no_question: str
    :return: bool
    """
    choice_yes = ["yes", "y"]
    choice_no = ["no", "n"]

    while True:
        user_choice = input(yes_no_question).lower()

        if user_choice in choice_yes:
            return True
        elif user_choice in choice_no:
            return False
        else:
            print("\nInvalid Input. Try again.\n")


def validate_name_input(prompt: str) -> str:
    """
    Validate the given name during registration.

    :param prompt: str
    :return: str
    """
    while True:
        name = input(prompt).strip()

        if not name:
            print("\nName must not be blank.\n")
            continue
        break
    return name


def validate_int_input(user_input: int) -> int:
    """
    Check the user input for a ValueError.

    :param user_input: int
    :return: int
    """
    while True:
        try:
            return int(input(user_input))
        except ValueError:
            print("\n\nValue must be an integer. \n\nTry again.\n")


def validate_age(age_prompt: str) -> int:
    """
    Validate the user's age.

    :param age_prompt: str
    :return: int
    """
    current_year = datetime.now().year

    while True:
        input_year = validate_int_input(age_prompt)
        age = current_year - input_year
        if input_year <= 0:
            print("\nInvalid year. Try again.\n")
        elif input_year > current_year:
            print("\nAre you from the Future? No, I don't think so. Retrying...\n")
        elif age < 16:
            print("\nAge must be 16 or older to register.\n")
            print("\nReturning to main menu...\n")
            main()
        else:
            return age


def validate_gender(prompt: str) -> str:
    """
    Verify the gender input of the user provided by the prompt.

    :param prompt: str
    :return: str
    """
    gender = ["male", "female", "m", "f"]
    while True:
        user_gender = input(prompt).lower()
        if not user_gender:
            print("\nField must not be blank.\n")
        elif user_gender not in gender:
            print("\nOnly Male or Female.")
        else:
            return user_gender


def validate_date_format(date_prompt: str, length: int, date_format: str) -> str:
    """
    Validate the date format.

    :param date: str
    :param length: int
    :return: str
    """
    while True:
        try:
            user_input = input(date_prompt)
            if len(user_input) == length:
                str(
                    datetime.strptime(user_input, date_format).date()
                )  # Convert user input date format into a specified date format
                return user_input
            elif not user_input:
                print("\nField must not be blank.\n")
            else:
                print("\nInvalid date format.\n")
        except ValueError:
            print("\nInvalid date.\n")


def validate_password(password_prompt: str) -> str:
    """
    Validate user password.

    :param password_prompt: str
    :return: str
    """
    special_symbols = [
        "!",
        "@",
        "#",
        "$",
        "%",
        "^",
        "&",
        "*",
        "(",
        ")",
        "-",
        "_",
        "+",
        "=",
        "~",
        "`",
        ";",
        ":",
        "'",
        '"',
        ",",
        ".",
        "<",
        ">",
        "/",
        "?",
    ]
    while True:
        user_password = input(password_prompt)
        if (
            len(user_password) < 8
        ):  # Check if the length of the password is less than eight
            print("\nPassword must be at least 8 characters long.\n")
        elif not any(
            char.isdigit for char in user_password
        ):  # Check if the password contains at least one digit
            print("\nPassword must contain at least one digit.\n")
        elif not any(
            char.isupper() for char in user_password
        ):  # Check if the password contains at least one uppercase letter
            print("\nPassword must contain at least one uppercase letter.\n")
        elif not any(
            char in special_symbols for char in user_password
        ):  # Check if the password contains at least one special symbol
            print("\nPassword must contain at least one special symbol.\n")
        else:
            return user_password


def validate_email(email_prompt: str) -> str:
    """
    Validate user email format.

    :param email_prompt: str
    :return: str
    """
    error_email_message = "Invalid email address.\n"

    while True:
        user_email = (
            input(email_prompt).strip().lower()
        )  # strip whitespace and make lowercase
        if "@" not in user_email:  # Check if the email contains @ symbol
            print(f"\n{error_email_message}")
        elif user_email[-4:] not in [
            ".com",
            ".net",
            ".org",
        ]:  # Check if the email contains .com, .net or .org top level domain names
            print(f"\n{error_email_message}")
        else:
            return user_email


def format_datetime(data: str, initial_format: str, new_format: str) -> str:
    """
    Format datetime to specified format.

    :param data: The value to be formatted.
    :param initial_format: The original format of the data.
    :param new_format: The new datetime format for the value.
    :return: str
    """
    temp = datetime.strptime(data, initial_format)
    return str(datetime.strftime(temp, new_format))


def authenticate_login_credentials(filename: str) -> bool:
    """
    Authenticate the login credentials of the user.

    :param account_details: list
    :return: bool
    """
    print("\n\n--- Type in username and password to login. ---")
    while True:
        username = input("\nUsername: ")
        password = input("Password: ")
        with open(filename, "r") as file_reader:
            content = file_reader.readlines()[1:]
            for line in content:
                login_info = line.strip().split(";")[1:]
                if (
                    not username or not password
                ):  # Check if the username or password is empty
                    print("\n**Username or Password field must not be blank.**")
                    break
                elif username == login_info[0] and password == login_info[1]:
                    print("\nLOGIN SUCCESSFUL!\n")
                    return login_info
            else:
                print("\nIncorrect Credentials Entered. Try again.")


def create_menu(choices: list[str], prompt: str = "\nChoose an option: ") -> int:
    """
    Prompt the user to choose from a list of choices.

    Returns either the choice that was chosen, or False.

    :param choices: list[str]
    :param prompt: str
    :returns: int
    """
    print("\n", end="")
    while True:
        for counter, choice in enumerate(
            choices, start=1
        ):  # Generate a numbered list of choices
            print(f"\t{counter}. {choice}")

        choice = validate_int_input(prompt)

        if 0 < choice <= len(choices):
            return choice
        else:
            print("\n** Please enter a number within the listed options. **\n")


def create_header(filename: str, column_name: list[str]) -> None:
    """
    Create headers for data files.

    :param filename: str
    :param column_name: list[str]
    :return: None
    """
    try:
        # Try to read the first line of the file
        with open(filename, "r", encoding="utf-8") as file_writer:
            old_column_name = file_writer.readline()
    except FileNotFoundError:
        old_column_name = ""
    if not old_column_name:
        with open(filename, "w", encoding="utf-8") as file_writer:
            file_writer.write(f"{';'.join(column_name)}\n")
    elif (
        old_column_name.split("\n")[0].split(";") != column_name
    ):  # Split by newline first and then by semicolon
        raise AssertionError(
            "Incorrect file headers detected."
        )  # Detect incorrect column names
    elif not old_column_name.endswith("\n"):
        # Append a newline if the column names are not terminated by a newline
        with open(filename, "a", encoding="utf-8") as file_writer:
            file_writer.write("\n")


def add_file_headers(filename: str, headers: list[str]) -> None:
    """
    Check whether the headers has been added to the file for the calling functions.

    :param filename: str
    :param headers: list[str]
    :return: None
    """
    is_headers_added = False
    if not is_headers_added:
        create_header(filename, headers)
        is_headers_added = True


def append_data_to_file(filename: str, record_details: list[list[str]]) -> None:
    """
    Generate a new line of data to be appended to the file.

    :param filename: str
    :param record_details: list[list[str]]
    :return: None
    """
    with open(filename, "a+") as file_handler:
        file_handler.seek(0)
        total_lines = len(file_handler.readlines())
        for data_id, records in enumerate(record_details):
            file_handler.write(f"{total_lines + data_id};{';'.join(records)}\n")


def add_admin_file_headers() -> None:
    """
    Create headers for the admin file.

    :return: None
    """
    admin_headers = ["admin_id", "username", "password", "email_address"]
    filename = "event_management_system/data/admin.txt"
    add_file_headers(filename, admin_headers)


def create_default_admin_account() -> list:
    """
    Create a default admin account if one does not exist.

    :return: list
    """
    add_admin_file_headers()
    master_list = []
    filename = "event_management_system/data/admin.txt"
    admin_username = "admin"
    admin_password = "superuser"
    admin_email = "su@aems.apu.edu.my"
    account_info = [admin_username, admin_password, admin_email]
    master_list.append(account_info)

    with open(filename, "r") as file_writer:
        record_exist = file_writer.readlines()[1:]
        if not record_exist:
            append_data_to_file(filename, master_list)
    return master_list


def create_customer_file_headers() -> None:
    """
    Create headers for the client file.

    :return: None
    """
    customer_headers = [
        "customer_id",
        "username",
        "password",
        "name",
        "age",
        "gender",
        "birthdate",
        "nationality",
        "contact_number",
        "email_address",
    ]
    filename = "event_management_system/data/client.txt"
    add_file_headers(filename, customer_headers)


def check_duplicate_username(username_prompt: str) -> str:
    """
    Check if a username already exists in the client file.

    :param username: str
    :return: bool
    """
    while True:
        logon_name = input(username_prompt)
        with open("event_management_system/data/client.txt", "r") as file_reader:
            content = file_reader.readlines()[1:]
            data_list = [item.strip().split(";") for item in content]
            for record in data_list:
                if logon_name == record[1]:
                    print("\n**Username already exists. Try again**")
                    break
            else:
                return logon_name


def create_new_member_account() -> list:
    """
    Create a new member account.

    :return: list
    """
    create_customer_file_headers()
    print("\n\n" + ("*" * 45))
    print("\tMember Registration Panel")
    print("\nKindly input your details to register as a new member. Thank you.")

    while True:
        username = check_duplicate_username("\nEnter a username: ")
        password = validate_password("Enter your password: ")
        member_name = validate_name_input("Enter your name: ")
        member_age = str(validate_age("Enter your year of birth: "))
        member_gender = validate_gender("Enter your gender (Male/Female): ")
        member_birthdate = validate_date_format(
            "Enter your birthdate in format YYYY-MM-DD: ", 10, "%Y-%m-%d"
        )
        member_nationality = input("Enter your nationality: ")
        member_contact = input("Enter your contact number: ")
        member_email = validate_email("Enter your email address: ")

        account_info = [
            username,
            password,
            member_name,
            member_age,
            member_gender,
            member_birthdate,
            member_nationality,
            member_contact,
            member_email,
        ]
        break

    print("\n**ACCOUNT CREATED**")
    return account_info


def split_multi_delimiters(filename: str) -> list:
    """
    Split the first and last delimiters in the category file into a list.

    :param filename: str
    :return: str
    """
    records = []
    data_list = []

    with open(filename, "r") as file_reader:
        contents = file_reader.readlines()[1:]
        for value in contents:
            data_value = ". ".join(value.strip().split(";", 1))
            records.append(data_value)

    for data in records:
        id_split = data.split(".", 1)
        current_total_events_value = [
            last_delimiter.rsplit(";", 1) for last_delimiter in id_split
        ]
        list_flatten = [
            item for sublist in current_total_events_value for item in sublist
        ]
        data_list.append(list_flatten)

    return data_list


def check_category_selection(prompt: str) -> int:
    """
    Check the user's choice of category.

    :param prompt: str
    :return: int
    """
    category_file_path = "event_management_system/data/category.txt"
    data_list = split_multi_delimiters(category_file_path)

    while True:
        print("\n", end="")
        for data in data_list:
            print(". ".join(data[:-1]).strip())

        choice = validate_int_input(prompt)

        if not choice > len(data_list):
            record: str = data_list[choice - 1]
            category = "".join(record[1]).strip()
            return category
        print("\n\nCategory does not exist. Try again.\n")


def display_all_records(filename: str) -> None:
    """
    Display all records of the specified file.

    :param filename: str
    :return: None
    """
    try:
        with open(filename, "r") as file_reader:
            content_list = file_reader.readlines()
            if len(content_list) == 0:
                print("\nFile is empty.")
            elif len(content_list) == 1:
                print("\nNo Records Found.")
            else:
                print("\n", end="")
                for data in content_list:
                    print(f"\n{', '.join(data.strip().split(';'))}")
    except FileNotFoundError:
        print(f"Sorry, '{filename}' does not exist.")


def update_record(filename: str, data_difference: list) -> None:
    """
    Update changed values of a record in the file.

    :param filename: str
    :param data_difference: list
    :return: None
    """
    with open(filename, "r") as file_reader:
        filedata = file_reader.read()
        for data in data_difference:
            old_data = ";".join(data[0])
            new_data = ";".join(data[1])
            new_content = filedata.replace(old_data, new_data)

    with open(filename, "w") as file_writer:
        file_writer.write(new_content)


def find_record(filename: str, data: str, value_index: int) -> list:
    """
    Get the record of the specified file.

    :param filename: str
    :param data: str
    :return: list
    """
    with open(filename, "r") as infile:
        contents = infile.readlines()[1:]
        data_list = [item.strip().split(";") for item in contents]
        for record in data_list:
            if data == record[value_index]:
                return record
        else:
            print("\n\n --- No Such Record Found. ---\n")


def find_customer_record_by_username(username: str) -> list:
    """
    Wrapper function to get the customer record by username.

    :param username: str
    :return: list
    """
    client_file_path = "event_management_system/data/client.txt"
    username_index = 1
    return find_record(client_file_path, username, username_index)


def find_event_record_by_prompt(prompt: str) -> list:
    """
    Wrapper function to get the event record by prompting the user.

    :param prompt: str
    :return: list
    """
    event_file_path = "event_management_system/data/events.txt"
    event_code = input(prompt)
    event_code_index = 3
    return find_record(event_file_path, event_code, event_code_index)


def get_event_summary() -> list:
    """
    Get the summary of the event based on selected category.

    :return: None
    """
    event_file_path = "event_management_system/data/events.txt"
    prompt_message = "\nSelect a category to view event details: "
    category = check_category_selection(prompt_message)
    record_found = False
    record_list = []

    with open(event_file_path, "r") as file_reader:
        event_content = file_reader.readlines()[1:]  # Skip the header
        # Get the record of the selected category
        event_details = [item.strip().split(";")[1:] for item in event_content]
        for data in event_details:
            if category in data:
                formatted_date = format_datetime(
                    data[5], "%Y-%m-%d", "%A, %b %d, %Y"
                )  # Format the date
                formatted_time = format_datetime(
                    data[6], "%H:%M", "%-H:%M %p"
                )  # Format the time (replace dash with hashtag on Windows)
                print(f"\n\n\033[1mEvent Name:\033[0m {data[0]}")
                print(f"\033[1mEvent Category:\033[0m {data[1]}")
                print(f"\033[1mOrganizer:\033[0m {data[4]}")
                print(
                    f"\033[1mDate and Time:\033[0m {formatted_date}, {formatted_time} GMT"
                )
                print(f"\033[1mLocation:\033[0m {data[9]}")
                print(f"\033[1mTicket Price:\033[0m RM {float(data[3]):.2f}")
                print(f"\033[1mSeats Available:\033[0m {data[-2]}")
                print(f"\033[1mStatus:\033[0m {data[-1]}")
                print(f"\n\033[1mEVENT CODE:\033[0m {data[2]}")
                record_list.append(data)
                record_found = True

    if not record_found:
        print("\n --- No Records Found ---\n")
    else:
        return record_list


def should_logout() -> bool:
    """
    Prompt the user whether they want to logout or not.

    :return: bool
    """
    logout_prompt = "\nAre you sure you want to logout? (y/n): "
    return ask_user_yes_no(logout_prompt)


def check_guest_menu_selection() -> None:
    """
    Check the guest's selection.

    :return: int
    """
    guest_menu = display_guest_menu()
    while True:
        choice = create_menu(guest_menu)
        if choice == 1:
            member_account = create_new_member_account()
            append_data_to_file(
                "event_management_system/data/client.txt", member_account
            )
            break
        elif choice == 2:
            get_event_summary()
        elif choice == 3:
            print("\n\n" + ("=" * 35))
            print("\tBack to main menu")
            print("=" * 35)
            break
        elif choice == 4:
            print("\n\n" + ("=" * 80))
            print("\tThank you for using Event Management System. Have a good day!")
            print("=" * 80)
            sys.exit(0)


def check_login_selection() -> None:
    """
    Prompt the user to choose an option.

    :return: None
    """
    login_menu = display_login_menu()
    while True:
        choice = create_menu(login_menu)
        if choice == 1:
            client.client_main()
        elif choice == 2:
            admin_file_path = "event_management_system/data/admin.txt"
            create_default_admin_account()
            authenticate_login_credentials(admin_file_path)
            admin.admin_main()
        elif choice == 3:
            print("\n\n" + ("=" * 35))
            print("\tBack to Main Menu")
            print("=" * 35)
            break


def main() -> None:
    """
    Initialize the program.

    :return: None
    """
    main_menu = display_main_menu()
    while True:
        user_choice = create_menu(main_menu)
        if user_choice == 1:
            check_guest_menu_selection()
        elif user_choice == 2:
            check_login_selection()
        elif user_choice == 3:
            print("\n\n" + ("=" * 80))
            print("\tThank you for using Event Management System. Have a good day!")
            print("=" * 80)
            sys.exit(0)


if __name__ == "__main__":
    main()

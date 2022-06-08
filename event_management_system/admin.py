"""Handles all functionalities related to the admin."""

# ALEX CHIEW (TP056952)

import ems


def display_admin_main_menu() -> list:
    """
    Display the main menu of the administrator panel.

    :return: list of menu options
    """
    menu_list = [
        "Add A New Event Category",
        "Add A New Event Record",
        "Modify Event Records",
        "Display Records",
        "Search Specific Event Record",
        "Logout",
    ]
    return menu_list


def display_view_all_records_menu() -> list:
    """
    Display a list of options for the admin to select from to view records.

    :return: int
    """
    menu_list = [
        "All Event Categories",
        "All Events Based on Category",
        "All Registered Customers",
        "All Customer Payments",
        "Back to Admin Menu",
    ]
    return menu_list


def display_search_records_menu() -> int:
    """
    Display a list of options for the admin to select from to search records.

    :return: int
    """
    menu_list = [
        "Customer Records",
        "Customer Payment",
        "Back to Admin Menu",
    ]
    return menu_list


def display_event_modification_menu() -> None:
    """
    Display a list of options for the admin to select from to modify event records.

    :return: None
    """
    menu_list = [
        "Event Title",
        "Event Category",
        "Event Price",
        "Start Date",
        "Venue",
        "Seats Available",
        "Event Status",
        "Back to Admin Menu",
    ]
    return menu_list


def display_search_customer_menu() -> list:
    """
    Display a list of options for the admin to select from to search customer records.

    :return: list of options
    """
    menu_list = [
        "Search by Username or Customer Name",
        "Search by Nationality",
        "Search by Birth Year",
        "Back to Admin Menu",
    ]
    return menu_list


def display_search_payment_menu() -> list:
    """
    Display a list of options for the admin to select from to search payment records.

    :return: list of options
    """
    menu_list = [
        "Search by Username",
        "Search by Amount",
        "Search by Date",
        "Back to Admin Menu",
    ]
    return menu_list


def add_category_headers() -> None:
    """
    Create a header for the category file.

    :return: None
    """
    category_headers = [
        "category_id",
        "category_name",
        "total_events",
    ]
    filename = "event_management_system/data/category.txt"
    ems.add_file_headers(filename, category_headers)


def create_event_category() -> list:
    """
    Accept user inputs to create a list of event category details.

    :return: list of event category details
    """
    add_category_headers()
    master_list = []

    while True:
        category_name = input("\nEnter a category name: ")
        current_events = 0
        master_list.append([category_name, str(current_events)])

        if not ems.ask_user_yes_no("\nWould you like to add another category? (y/n): "):
            break
    return master_list


def add_event_headers() -> None:
    """
    Create a header for the event file.

    :return: None
    """
    event_headers = [
        "event_id",
        "event_name",
        "event_category",
        "event_code",
        "event_price",
        "organizer",
        "start_date",
        "start_time",
        "end_date",
        "end_time",
        "venue",
        "total_seats_available",
        "event_status",
    ]
    filename = "event_management_system/data/events.txt"
    ems.add_file_headers(filename, event_headers)


def update_category_total_events(category: str) -> None:
    """
    Increment the total number of events in a category based on selected category.

    :param category: str
    :return: None
    """
    filename = "event_management_system/data/category.txt"
    records = ems.split_multi_delimiters(filename)
    for data in records:
        category_name = "".join(data[1]).strip()  # Get only the category name
        old_record = [
            item.strip() for item in data
        ]  # Strip newlines from data and get the values
        new_record = old_record.copy()  # Copy the values to a new variable
        if category == category_name:
            current_value = int(new_record[-1])  # Get last value from the list
            new_value = current_value + 1  # Add 1 to the value
            new_record[2] = str(
                new_value
            )  # Update the value of total_events in the list
        # Read the old content of the file
        with open(filename, "r") as infile:
            filedata = infile.read()
            old_data = ";".join(old_record)
            new_data = ";".join(new_record)
            new_content = filedata.replace(old_data, new_data)
        # Overwrite the old content with the new content
        with open(filename, "w") as outfile:
            outfile.write(new_content)


def create_event() -> list:
    """
    Accept user inputs to create a list of event details.

    :return: list of event details
    """
    add_event_headers()
    master_list = []

    while True:
        event_title = input("\n\nEnter the title of the event: ")
        event_category = ems.check_category_selection(
            "\nSelect a category for this event: "
        )
        event_code = input("\nEnter the event code: ")
        ticket_price = input("Enter the price of the event: ")
        organizer_name = input("Enter the name of the event organizer: ")
        start_date = ems.validate_date_format(
            "Enter start date of event in format YYYY-MM-DD: ", 10, "%Y-%m-%d"
        )
        start_time = input("Enter the start time of the event: ")
        end_date = ems.validate_date_format(
            "Enter end date of event in format YYYY-MM-DD: ", 10, "%Y-%m-%d"
        )
        end_time = input("Enter the end time of the event: ")
        venue = input("Enter the venue of the event: ")
        total_seats_available = str(
            ems.validate_int_input("Enter the total available seats for the event: ")
        )

        event_info = [
            event_title,
            event_category,
            event_code,
            ticket_price,
            organizer_name,
            start_date,
            start_time,
            end_date,
            end_time,
            venue,
            total_seats_available,
        ]

        master_list.append(event_info)

        update_category_total_events(event_category)

        if not ems.ask_user_yes_no("\nWould you like to add another event? (y/n): "):
            break
    return master_list


def get_event_status() -> str:
    """
    Get the status of the event from the admin.

    :return: str
    """
    status = [
        "Active",
        "Completed",
        "Cancelled",
    ]
    user_choice = ems.create_menu(status, "\nSelect the status of the event: ")
    return status[user_choice - 1]


def modify_event_record() -> None:
    """
    Modify and update the event record based on selected column.

    :return: None
    """
    event_file = "event_management_system/data/events.txt"
    event_code_prompt = "\nEnter the event code to modify record: "
    old_event_record = ems.find_event_record_by_prompt(event_code_prompt)
    record_difference = []

    if not old_event_record:
        return None

    menu_prompt = "\nSelect the column you wish to modify: "
    new_event_record = old_event_record.copy()
    submenu = display_event_modification_menu()

    while True:
        choice = ems.create_menu(submenu, menu_prompt)
        if choice == 1:
            new_event_record[1] = input("\nEnter the new title of the event: ")
            record_difference.append([old_event_record, new_event_record])
            print("\n\n** EVENT TITLE UPDATED SUCCESSFULLY **")
        elif choice == 2:
            new_event_record[2] = ems.check_category_selection(
                "\nSelect a category as new category for this event: "
            )
            record_difference.append([old_event_record, new_event_record])
            print("\n\n** EVENT CATEGORY UPDATED SUCCESSFULLY **")
        elif choice == 3:
            new_event_record[4] = input("\nEnter new ticket price for the event: ")
            record_difference.append([old_event_record, new_event_record])
            print("\n\n** TICKET PRICE UPDATED SUCCESSFULLY **")
        elif choice == 4:
            new_event_record[6] = ems.validate_date_format(
                "\nEnter new start date of the event: ", 10, "%Y-%m-%d"
            )
            record_difference.append([old_event_record, new_event_record])
            print("\n\n** EVENT DATE UPDATED SUCCESSFULLY **")
        elif choice == 5:
            new_event_record[-3] = input("\nEnter new venue of the event: ")
            record_difference.append([old_event_record, new_event_record])
            print("\n\n** EVENT VENUE UPDATED SUCCESSFULLY **")
        elif choice == 6:
            new_event_record[-2] = str(
                ems.validate_int_input(
                    "\nEnter new total seats available for this event: "
                )
            )
            record_difference.append([old_event_record, new_event_record])
            print("\n\n** EVENT CAPACITY UPDATED SUCCESSFULLY **")
        elif choice == 7:
            new_event_record[-1] = get_event_status()
            record_difference.append([old_event_record, new_event_record])
            print("\n\n** EVENT STATUS UPDATED SUCCESSFULLY **")
        elif choice == 8:
            break
        else:
            print("\nInvalid choice. Try again.")
        if not ems.ask_user_yes_no("\nWould you like to modify another value? (y/n): "):
            break

    ems.update_record(event_file, record_difference)

    print("\n\n** EVENT RECORD UPDATED SUCCESSFULLY **\n")
    print("-- BACK TO MENU --\n")


def view_records(filename: str) -> None:
    """
    Display all records of the specified file.

    :param filename: str
    :return: None
    """
    with open(filename, "r") as file_reader:
        content = file_reader.readlines()
        record_list = [item.strip().split(";") for item in content]
        for data in record_list:
            print(f"\n{', '.join(data)}")


def find_all_registered_member_records() -> None:
    """
    Wrapper function to get all registered members.

    :return: None
    """
    client_file = "event_management_system/data/client.txt"
    view_records(client_file)


def find_all_payment_records() -> None:
    """
    Wrapper function to get all transaction records.

    :return: None
    """
    transaction_file = "event_management_system/data/transactions.txt"
    view_records(transaction_file)


def save_file_headers(filename: str) -> None:
    """
    Save the headers of the file to be used for other admin functions.

    :param filename: str
    :return: None
    """
    with open(filename, "r") as file_reader:
        content = file_reader.readline()
        headers = content.strip().split(";")
    return headers


def search_specific_record_by_string(
    prompt: str, filename: str, value_index: int
) -> None:
    """
    Search for a specific record in a file based on search term.

    :param prompt: A message that prompts the user to enter the search term.
    :param filename: The filename for the record to be searched.
    :return: None
    """
    headers = save_file_headers(filename)
    record_found = False

    while True:
        search_term = input(prompt)
        print(f"\n\n{', '.join(headers)}")
        with open(filename, "r") as file_reader:
            content = file_reader.readlines()[1:]
            record_list = [item.strip().split(";") for item in content]
            result_list = [
                data for data in record_list if search_term == data[value_index]
            ]
            for data in result_list:
                print(f"\n{', '.join(data)}")
                record_found = True

        if not record_found:
            print("\n\n--- No Record Found. ---\n")
        else:
            print(f"\n\n\033[1mTOTAL RECORDS FOUND:\033[0m {len(result_list)}")
        break


def search_specific_record_by_date(
    prompt: str, filename: str, date_length: int, date_format: str, dt_index: int
) -> None:
    """
    Search for a specific record in a file based on date.

    :param filename: The filename for the record to be searched.
    :param kwargs: The keyword arguments for the date and index of date from record.
    :return: None
    """
    headers = save_file_headers(filename)
    record_found = False

    while True:
        search_term = ems.validate_date_format(prompt, date_length, date_format)

        print(f"\n\n{', '.join(headers)}")

        with open(filename, "r") as file_reader:
            content = file_reader.readlines()[1:]
            record_list = [item.strip().split(";") for item in content]
            for data in record_list:
                formatted_date = ems.format_datetime(
                    data[dt_index], "%Y-%m-%d", "%Y-%m"
                )
                if search_term == formatted_date:
                    print(f"\n{', '.join(data)}")
                    record_found = True

        if not record_found:
            print("\n--- No Record Found. ---")
        break


def search_specific_payment_record_by_amount(
    prompt: str, filename: str, dt_index: int
) -> None:
    """
    Search payment record by transaction amount.

    :return: None
    """
    headers = save_file_headers(filename)
    record_found = False
    result_counter = 0

    while True:
        transaction_amount = ems.validate_int_input(prompt)
        if transaction_amount < 0:
            print("\n--- INVALID INPUT! --- Try again.")
            continue

        print(f"\n\n{', '.join(headers)}")

        with open(filename, "r") as file_reader:
            content = file_reader.readlines()[1:]
            record_list = [item.strip().split(";") for item in content]
            for data in record_list:
                if 0 <= int(float(data[dt_index])) >= transaction_amount:
                    print(f"\n{', '.join(data)}")
                    record_found = True
                    result_counter += 1

        if not record_found:
            print("\n--- No Record Found. ---")
        else:
            print(f"\n\n\033[1mTOTAL RECORDS FOUND:\033[0m {result_counter}")
        break


# -------------------- WRAPPER FUNCTIONS TO GET CUSTOMER PAYMENT RECORDS --------------------
def retrieve_member_record_by_username() -> None:
    """
    Wrapper function to get customer record by username.

    :return: None
    """
    client_file = "event_management_system/data/client.txt"
    logon_name = "\nEnter a username to view their record: "
    data_index = 1
    search_specific_record_by_string(logon_name, client_file, data_index)


def retrieve_member_record_by_nationality() -> None:
    """
    Wrapper function to get customer record by their nationality.

    :return: None
    """
    client_file = "event_management_system/data/client.txt"
    nationality = "\nEnter a nationality to begin filtering records: "
    data_index = 7
    search_specific_record_by_string(nationality, client_file, data_index)


def retrieve_member_record_by_birthyear() -> None:
    """
    Wrapper function to get customer record by their nationality.

    :return: None
    """
    client_file = "event_management_system/data/client.txt"
    year_prompt = "\nEnter a year to begin searching customer records: "
    date_format = "%Y"  # Format of datetime to be year-only.
    year_string_length = 4  # Length of string that is to be validated.
    column_index = 6  # The index of the column that contains the birthdate
    search_specific_record_by_date(
        year_prompt, client_file, year_string_length, date_format, column_index
    )


# -------------------- WRAPPER FUNCTIONS TO GET CUSTOMER PAYMENT RECORDS --------------------
def retrieve_payment_record_by_username() -> None:
    """
    Wrapper function to get the payment record by username.

    :return: None
    """
    transaction_file = "event_management_system/data/transactions.txt"
    login_name = "\n\nEnter the username to search for their payment record: "
    data_index = 1
    search_specific_record_by_string(login_name, transaction_file, data_index)


def retrieve_payment_record_by_amount() -> None:
    """
    Wrapper function to get the payment record by transaction amount.

    :return: None
    """
    input_message = "\n\nEnter amount to start searching: > RM "
    transaction_file = "event_management_system/data/transactions.txt"
    column_index = -2
    search_specific_payment_record_by_amount(
        input_message, transaction_file, column_index
    )


def retrieve_payment_record_by_date() -> None:
    """
    Wrapper function to get the payment record by date.

    :return: None
    """
    transaction_file = "event_management_system/data/transactions.txt"
    input_message = "\nEnter date in format YYYY-MM (e.g. 2020-01) to search Record: "
    date_format = "%Y-%m"
    date_length = 7  # The length of the date string - YYYY-MM
    value_index = 4  # The index of the date in the transaction record

    search_specific_record_by_date(
        input_message,
        transaction_file,
        date_length,
        date_format,
        value_index,
    )


# ----------------------- FUNCTIONS TO CHECK ADMIN MENU SELECTIONS  -----------------------
def check_search_customer_record_submenu() -> None:
    """
    Search for a specific customer record based on selected search options.

    :return: None
    """
    submenu = display_search_customer_menu()
    prompt_message = "\nSelect an option to search for a customer's record: "

    while True:
        choice = ems.create_menu(submenu, prompt_message)
        if choice == 1:
            retrieve_member_record_by_username()
        elif choice == 2:
            retrieve_member_record_by_nationality()
        elif choice == 3:
            retrieve_member_record_by_birthyear()
        elif choice == 4:
            break

        if not ems.ask_user_yes_no("\n\nWould you like to search again? (y/n): "):
            break


def check_search_payment_record_submenu() -> None:
    """
    Search for a specific payment record based on selected search options.

    :return: None
    """
    submenu = display_search_payment_menu()
    prompt_message = "\nSelect an option to search for a payment record: "

    while True:
        choice = ems.create_menu(submenu, prompt_message)
        if choice == 1:
            retrieve_payment_record_by_username()
        elif choice == 2:
            retrieve_payment_record_by_amount()
        elif choice == 3:
            retrieve_payment_record_by_date()
        elif choice == 4:
            break

        if not ems.ask_user_yes_no("\n\nWould you like to search again? (y/n): "):
            break


def check_view_record_selection() -> None:
    """
    Check the user's choice of event to be viewed.

    :return: int
    """
    submenu = display_view_all_records_menu()
    prompt_message = "\nSelect a record to display: "
    while True:
        choice = ems.create_menu(submenu, prompt_message)
        if choice == 1:
            print("\n\n** VIEWING CATEGORY RECORDS **")
            ems.display_all_records("event_management_system/data/category.txt")
            print("\n\nBacked to Menu")
        elif choice == 2:
            print("\n\n** VIEWING EVENT RECORDS **")
            ems.get_event_summary()
        elif choice == 3:
            find_all_registered_member_records()
        elif choice == 4:
            find_all_payment_records()
        elif choice == 5:
            break


def check_search_record_selection() -> None:
    """
    Check which record to be viewed by the admin.

    :return: int
    """
    submenu = display_search_records_menu()
    prompt_message = "\nSelect a record to search: "
    while True:
        choice = ems.create_menu(submenu, prompt_message)
        if choice == 1:
            print("\n\n** YOU ARE NOW SEARCHING CUSTOMERS RECORDS **")
            check_search_customer_record_submenu()
        elif choice == 2:
            print("\n\n** YOU ARE NOW SEARCHING TRANSACTION RECORDS **")
            check_search_payment_record_submenu()
        elif choice == 3:
            break


def admin_main() -> None:
    """
    Initialize the admin panel.

    :return: None
    """
    print("\n\nYou are now logged into the Administrator Panel.")
    admin_menu = display_admin_main_menu()
    while True:
        user_choice = ems.create_menu(admin_menu)
        if user_choice == 1:
            category_details = create_event_category()
            category_filename = "event_management_system/data/category.txt"
            ems.append_data_to_file(category_filename, category_details)
            print("\n** Category Added Successfully. **\n")
        elif user_choice == 2:
            event_details = create_event()
            event_filename = "event_management_system/data/events.txt"
            ems.append_data_to_file(event_filename, event_details)
        elif user_choice == 3:
            print("\n** MODIFYING EVENT RECORDS **")
            modify_event_record()
        elif user_choice == 4:
            check_view_record_selection()
        elif user_choice == 5:
            check_search_record_selection()
        elif user_choice == 6:
            if ems.should_logout():
                break

    print("\nYou have successfully logged out.\n")
    ems.main()

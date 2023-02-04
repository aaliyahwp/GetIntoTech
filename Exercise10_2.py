import getpass

supplied_pin = getpass.getpass("Enter your PIN:  ")
# pin = 1998

if supplied_pin == '1998':
    print("Correct pin.")
else:
    print("Incorrect pin, please try again.")



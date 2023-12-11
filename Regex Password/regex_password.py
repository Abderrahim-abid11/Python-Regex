import re

def is_valid_password(password):
    password_pattern = r'^(?=.*[a-zA-Z])(?=.*[0-9])[a-zA-Z0-9]+$'

    return re.match(password_pattern, password) is not None

password = str(input("Enter Password : "))
if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is not valid.")


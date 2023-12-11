import re

def is_valid_name(name):
    name_pattern = r'^[a-zA-Z\s\'-]+$'

    return re.match(name_pattern, name) is not None

name = str(input("Enter Your Full Name : "))
if is_valid_name(name):
    print("Name is valid.")
else:
    print("Name is not valid.")


import re

email = str(input("Enter Your Email : "))
pattern = re.compile(r'\b[A-Z-a-z-0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b')
if re.match(pattern, email):
    print("Valid Email .")
else:
    print("Invalid Email .")


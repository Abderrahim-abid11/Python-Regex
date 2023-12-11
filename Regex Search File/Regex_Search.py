import re
import sys

try:
    filename = str(input("Enter File Name : "))
    pattern = str(input("Enter Some Name : "))
    with open(filename, 'r') as file:
        text = file.readlines()
    regexp = re.compile(pattern)
    for line in text:
        result = regexp.search(line)
        if result:
            print(line, end="")
except FileNotFoundError:
    print("File Not Found !")
except:
    print("Name Not Found !")

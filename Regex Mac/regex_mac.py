import re
import os

def find_macs_in_file(file_path):
    mac_pattern = r'\b(?:[0-9A-Fa-f]{2}[:-]){5}(?:[0-9A-Fa-f]{2})\b'

    with open(file_path, 'r') as file:
        content = file.read()

    macs = re.findall(mac_pattern, content)

    return macs

file_path = str(input("Enter File Name : "))  # Replace with the actual file path
found_macs = find_macs_in_file(file_path)

os.system('clear')
print("\n\n\n")

print("\nFound MAC Addresses:")
for mac in found_macs:
    print(mac)

print("\n\n\n")

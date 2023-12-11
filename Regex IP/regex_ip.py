import re
import os
def find_ips_in_file(file_path):
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'

    with open(file_path, 'r') as file:
        content = file.read()

    ips = re.findall(ip_pattern, content)

    return ips

file_path = str(input("Enter File Name : "))
found_ips = find_ips_in_file(file_path)

os.system('clear')
print("\n\n\n")

print("Found IPs:")
for ips in found_ips:
    print(ips)
print("\n\n\n")


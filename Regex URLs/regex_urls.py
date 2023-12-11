import re
import os

def find_urls_in_file(file_path):
    url_pattern = r'\b(?:https?|ftp):\/\/[-A-Za-z0-9+&@#\/%?=~_|!:,.;]*[-A-Za-z0-9+&@#\/%=~_|]'

    with open(file_path, 'r') as file:
        content = file.read()

    urls = re.findall(url_pattern, content)

    return urls

file_path = str(input("Enter File Name : "))
found_urls = find_urls_in_file(file_path)

os.system('clear')
print("\n\n\n")

print("Found URLs:")
for url in found_urls:
    print(url)
print("\n\n\n")

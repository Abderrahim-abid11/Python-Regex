import re
import requests
import os

def get_url_status(url):
    try:
        response = requests.head(url)
        status_code = response.status_code
        return f"{url} [{status_code} {response.reason}]"
    except requests.RequestException as e:
        return f"{url} [Error: {e}]"

def find_and_check_urls_in_file(file_path):
    url_pattern = r'\b(?:https?|ftp):\/\/[-A-Za-z0-9+&@#\/%?=~_|!:,.;]*[-A-Za-z0-9+&@#\/%=~_|]'
    
    with open(file_path, 'r') as file:
        content = file.read()

    urls = re.findall(url_pattern, content)

    urls_with_status = [get_url_status(url) for url in urls]

    return urls_with_status

file_path = str(input("Enter URLS File : "))
urls_with_status = find_and_check_urls_in_file(file_path)

os.system('clear')
print("\n\n\n")

print("URLs with Status:")
for url_status in urls_with_status:
    print(url_status)

print("\n\n\n")



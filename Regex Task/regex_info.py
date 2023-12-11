import re

random_info = """
my name is Mr. Abid my phone number is 0600112233. my email is abid@gmail.com
my name is Mr. abid my phone number is 0611223344. my email is abid@yahoo.com
"""
my_list = ['abid@gmail.com', 'abid@yahoo.com']

print(f"this the text we work on : \n{random_info}")
print("and this what we can do with Regex and 're' : \n")
print(re.findall('@[a-z]+', random_info)) # get the email types ["@gmail","@yahoo"]
print(re.findall('@([a-z]+)', random_info)) # ['gmail','yahoo'] .
print(re.findall('@([\w\.]+)', random_info)) # ['gmail.com', 'yahoo.com']
print(re.findall('[\w+]+@[\w\.]+', random_info)) # ['abid@gmail.com', 'abid@.yahoo.com']
print(re.findall('\d{10}', random_info)) # ['0600112233', '0611223344']
print()
for email in my_list:
    i = 0
    data = re.findall('[\w+]+@[\w\.]+', email)
    print(data[i])
    i += 1

print()

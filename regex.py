import re
string = "Please contact info@example.com for assistance. Phone: (123) 456-7890 or (111) 222-3333"

number = re.findall('[0-9]+',string)

print(string)




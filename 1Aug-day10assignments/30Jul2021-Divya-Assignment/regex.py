import re
# var = 'aab'
# regex = re.search("a?b+$",var)
# print(regex)

# name = "diya"
#regex = re.match("[a-zA-Z]{5}",name)

# regex = re.match("^[a-zA-z]",name)
# print(regex)

PER= "77%"
regex = re.match("^[0-9]+%$",PER)
print(PER)
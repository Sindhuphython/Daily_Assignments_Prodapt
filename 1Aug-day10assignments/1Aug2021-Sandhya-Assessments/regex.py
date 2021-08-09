#  "^hello"    matches any string that start with hello
#  "hello$"    matches any string that ends with hello
#  "^hello$"   matches any string that start and ends with hello
#  "hello"     matches any string that contains hello
#  "hello*"    matches any string that contains 0 or more than o's
#  "hello+"    matches any string that contains 1 or more than o's
#  "hello?"    there might be a single o(letter o) or not
#   {}         to specify a range
#   ()         for group 
# var="aaaaabbb"
# regex=re.search("ab")

import re
# var="abb"
#regex=re.match("ab{2,}",var)  #here the b should be 2 or unlimited means more than 2
#regex=re.match("ab{2,8}",var)  #starting from 2 b's and can reach to upto 8 b's
#v=re.search("hello+",var)
#v=re.search("hello*",var)
#v=re.search("hello?",var)
# regex=re.match("a(bc)*",var)
# regex=re.match("a(bc)+",var)
# regex=re.match("a(bc){2,4}",var)
# regex=re.match("hello|hii",var)
#  regex=re.match("^a(bc){2,4}$","abb")
# var="hellox"
# regex=re.match("(hello|hi)*x",var)
# regex=re.match("(hello|hi)+x",var) #atleast one hi or hello follwed by x
# regex=re.match("[a-zA-Z]*[0-9]{3}",var)
# regex=re.match("[a-zA-Z]{5}$",var)

# val=input("enter a name:")
# regex=re.match("^[a-zA-Z]",val)
# print(regex)

# var="%56"
# regex=re.match("^[0-9]{2}%$",var)

name=input("enter the name:")
regex=re.match("(\+91)?[0]?(91)?[6-9]\d{9}$",var)






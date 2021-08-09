#  "^hello"    matches any string that start with hello
#  "hello$"    matches any string that end with hello
#  "^hello$"   matches any string that starts and end with the same string
#  "hello"     matches any string that contain "hello"
#   "hello"    matches any string that contains 0 or more than O's 
#   {}         to specify range
#   ()         for group
#    | (or)    
#   []
import re

# *
variable = "hellox"
v=re.search("hello*", variable)
#print(v)

# +
a = "hellox"
v1=re.search("hellox+",a)
#print(v1)

#?
a1 = "hellox"
v2=re.search("hellox?",a1)
#print(v1)

#combination
var="aab"
regex = re.search("a?b+$",var)
#print(regex)

x="ababb"
reg = re.match("ab{2,4}",x)
#print(x)

#   {} 
y = re.match("^(ab){3,5}b$",x)
#print(y)

# .
b='b'
a = re.match("a.[1-9]",b)
print(b)

var1 ="thub"
re2=re.match("^[a-z A-Z]{5}$", var1)
print(re2)

vx= "a"
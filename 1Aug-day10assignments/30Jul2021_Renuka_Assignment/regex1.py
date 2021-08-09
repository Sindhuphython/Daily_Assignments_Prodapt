import re
var="shsgbdgs"
reg=re.search("^[a-zA-Z]",var)
print(reg)
var1="56%"
reg1=re.search("^[0-9]{2}%$",var1)
print(reg1)
# regular expression for indian number
var2="9849154692"
reg2=re.search("^(\+91)?[0]?(91)?[6-9]\d{9}$",var2)
#\d for digit,\w for variable,? is for optional
print(reg2)
#   "^hello" matches the string which starts with hello
#   "world$" matches the string which ends with world
#   "^hello$" matches the string which starts and ends with hello
#   "hello"  matches any string which contains hello
#   "hello*" matches any string that contains 0 or more than o's
#   "hello+" matches any string that contains 1 or more than o's
#   "hello?" might be contains single o or not
#   {}       used to specify range
#   ()       used for grouping
#import re
#var="helloooox"
#v=re.search("hello?",var)
#print(v)
import re
var="aabb"
var1="abcbc"
var2="abcbcbcbcbcbcbcb"
var3="hellohihi"
var4="hellohellohix"
var5="hellohix"
var6="a1"
var7="A1234"
regex=re.search("ab{2}",var)  
regex1=re.match("ab{2}",var)  #use match only for proper proper validations
regex2=re.search("ab{2,}",var) #it should contain atleast 2 b's should be there
regex3=re.search("ab{2,8}",var)#it should contain minimum 2 b's and 8 b's 
regex4=re.match("a(bc)*",var1)
regex5=re.match("a(bc){2,4}",var2)
regex6=re.search("hello|hi",var3)
regex7=re.search("(hello|hi)*x",var4)
regex8=re.search("(hello|hi)+x",var5)
regex9=re.search("a.[0-9]",var6)
regex10=re.search("[a-zA-Z]*[0-9]{3}",var7)
print(regex)
print(regex1)
print(regex2)
print(regex3)
print(regex4)
print(regex5)
print(regex6)
print(regex7)
print(regex8)
print(regex9)
print(regex10)
#reex should contain only five characters
var11="ABCDE"
regex11=re.search("^[A-Z]{5}$",var11)
print(regex11)

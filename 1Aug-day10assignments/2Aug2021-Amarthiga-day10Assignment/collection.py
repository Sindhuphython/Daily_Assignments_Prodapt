#1 Named tuple()
import collections as c 

students = c.namedtuple("students", ['name', 'stdID', 'fees'])
s1 = students("Amar","88221", "6000")
print(s1)

##can do index also
print(s1[2])

#OrderedDict() 
d1=c.OrderedDict()
d1['N'] ="Mani"
d1['rollNo']="20"
d1["admNO"] = "101"

for key,value in d1.items():
    print(key,value)

#3 Counter()

c1= c.Counter(["Hai", "Welcome", "Vanakam", "Hai", "Vanakam"])

print(c1)

#task1

Names1=[]
for i in range(10):
    names= input("Enter a name:")
    #Names1.append(names)
    Names1.append(names.lower())   #for rectify the case sensitive property 

Counter1=c.Counter(Names1)
print(Counter1)

#4. DefaultDict()

m=c.defaultdict(str)
m["name"]="Amar"
m["RollNo"]="03"

print(m)
print(["AdminNo"])

#5. Deque 
x= c.deque([12,4,3,5,7])
x.append(7)
#x.appendleft(8)
x.pop()       #remove the item from the right side
x.popleft()
print(x)

#6.ChainMap:
D1 ={"Name":"Kow","Age":23}
D2 ={"Name":"Div","age":22}
comb_dict=c.ChainMap(D1,D2)
print(comb_dict.maps)  
print(list(comb_dict.keys()))
print(list(comb_dict.values()))
print(comb_dict.values())
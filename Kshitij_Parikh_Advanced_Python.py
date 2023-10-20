#1
import re

def read_file(filename):
	try:
		with open(filename, 'r') as f:
			contents = f.read()
		return contents
	except IOError:
		print("Error: could not read file " + filename)
filename=r"C:\Users\k.park99\Desktop\text.txt"
x=read_file(filename)
dateregex=re.compile(r'([0-3][0-9])-([0-1][0-9])-([1-2][0,9][0-9][0-9])')
x=dateregex.findall(x)
for i in x:
    if int(i[1])>12 or int(i[1])==0:
        x.remove(i)
for i in x:
    if int(i[0])==0 or int(i[0])>31:
        x.remove(i)
for i in x:
    
    if (int(i[2])%400==0 and int(i[2])%100==0) or (int(i[2])%4==0 and int(i[2])%100!=0) :
        if int(i[1])==2 and int(i[0])>29:
            x.remove(i)
    if not ((int(i[2])%400==0 and int(i[2])%100==0) or (int(i[2])%4==0 and int(i[2])%100!=0)) :
        if int(i[1])==2 and int(i[0])>28:
            x.remove(i)
    if int(i[1]) in [1,3,5,7,8,10,12]:
        if int(i[0])==0 or int(i[0])>31 :
            x.remove(i)
    elif int(i[1]) in [4,6,9,11]:
        if int(i[0])==0 or int(i[0])>30 :
            x.remove(i)
    if int(i[1])>12 or int(i[1])==0:
        x.remove(i)
        
print(x)


import functools
data = ["123", "456", "789", "abc", "def", "101112"]
def func2(x):   
        try:
            if int(x) is not None:
                return True
        except:
            return False
list2=list(filter(func2,data))
list2_1=[int(i) for i in list2]
list2_2=[i**2 for i in list2_1]
y=functools.reduce(lambda a,b: a+b, list2_2)
print(y)

'''
Question 1
You are given a string that contains various dates. Write a Python regex expression to match all valid dates in the format of DD-MM-YYYY, where:
DD is a two-digit day between 01 and 31.
MM is a two-digit month between 01 and 12.
YYYY is a four-digit year between 1900 and 2099.
Remember to account for months that can't have 31 days, and also consider leap years.
Once you've written the regex, use it to extract all the valid dates from the given string.
Input: [take input from file, also use decorator] 
text = "These are the dates: 05-12-1995, 31-11-2000, 00-12-2000, 15-13-2010, 29-02-2000, 29-02-2001."

'''
import re
def handle_io(func):
    def wrapper(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except:
            print("Couldn't read the file")
    return wrapper         

def regex(func):
    def wrapper(*args,**kwargs):
        contents=func(*args,**kwargs)
        dateregex=re.compile(r'([0-3][0-9])-([0-1][0-9])-([1-2][0,9][0-9][0-9])')
        x=dateregex.findall(contents)
        dates=x
        for i in x:
            if int(i[1])>12 or int(i[1])==0:
                dates.remove(i)
        for i in x:
            if int(i[0])==0 or int(i[0])>31:
                dates.remove(i)
        for i in x:
            
            if (int(i[2])%400==0 and int(i[2])%100==0) or (int(i[2])%4==0 and int(i[2])%100!=0) :
                if int(i[1])==2 and int(i[0])>29:
                    dates.remove(i)
            if not ((int(i[2])%400==0 and int(i[2])%100==0) or (int(i[2])%4==0 and int(i[2])%100!=0)) :
                if int(i[1])==2 and int(i[0])>28:
                    dates.remove(i)
            if int(i[1]) in [1,3,5,7,8,10,12]:
                if int(i[0])==0 or int(i[0])>31 :
                    dates.remove(i)
            elif int(i[1]) in [4,6,9,11]:
                if int(i[0])==0 or int(i[0])>30 :
                    dates.remove(i)
            if int(i[1])>12 or int(i[1])==0:
                dates.remove(i)
        return dates
    return wrapper

@regex
@handle_io
def read_file(filename):
    with open(filename, 'r') as f:
        contents = f.read()
    return contents

filename=r"C:\Users\k.park99\Desktop\text.txt"
read_file(filename)








'''
Question 2

Filter out strings that are not numeric (e.g., "123" is valid, "abc" is not).
Convert the filtered strings into integers. [Use Lambda, Map, Reduce, Filter, Decorator]
Square each integer.
Finally, sum all the squared numbers.
# Sample list of strings
data = ["123", "456", "789", "abc", "def", "101112"]


'''

import functools
def decorator2(func):
    def wrapper(*args,**kwargs):
        data = ["123", "456", "789", "abc", "def", "101112"]
        
        list2=list(filter(func,data))
        list2_1=[int(i) for i in list2]
        list2_2=[i**2 for i in list2_1]
        y=functools.reduce(lambda a,b: a+b, list2_2)
        return y
    return wrapper
@decorator2
def func2(x):   
        try:
            if int(x) is not None:
                return True
        except:
            return False

data=func2()
print(data)

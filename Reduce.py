import functools
import operator

#1
list1=[1,2,3,4,5,6]
x=functools.reduce(lambda x,y:x+y,list1)
print(x)

#2
list2=[1,2,4,5]
x=functools.reduce(operator.add,list2)
print(x)

#3
list3=['a','b','c']
x=functools.reduce(lambda x,y:x+y,list3)
print(x)

#4
def func4(a,b):
    return a if a>b else b
list4=[1,2,3,4]
x=functools.reduce(func4,list4)
print(x)
 
#5
list5=[0,0,1]
x=functools.reduce(lambda x,y:x+y, list4, 1)
print(x)

#6
list6=[1,2,3,4,5,0]
x=functools.reduce(lambda x,y:bool(x and y),list6)
print(x)

#7
def reduce1(function, iterable, initializer=None): 
    it = iter(iterable) 
    if initializer is None: 
        value = next(it)
    else: 
        value = initializer
        
    for element in it: 
        value = function(value, element) 
    return value 
x=reduce1(lambda x,y:x+y,[1,1,1])
print(x)



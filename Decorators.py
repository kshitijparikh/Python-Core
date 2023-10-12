'''
Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.
'''
    
#Before using decorators, lets understand below concepts

#1 Function is an instance of object type. 
def shout(text): 
    return text.upper() 
print(shout('Hello')) 
yell = shout  #Function used as an object
print(yell('Hello'))


#2  Passing the function as an argument
def shout(text): 
    return text.upper() 
def whisper(text): 
    return text.lower() 
def greet(func): 
    # storing the function in a variable 
    greeting = func("""Hi, I am created by a function passed as an argument.""") 
    print (greeting) 
greet(shout) 
greet(whisper) 


#3 Returning functions from another function
def create_adder(x): 
    def adder(y): 
        return x+y 
    return adder 
add_15 = create_adder(15) 
print(add_15(10))


#Decorators

#1
def hello_decorator(func):
    def inner1():
        print("Hello, this is before function execution")
        func()
        print("This is after function execution")
         
    return inner1
def function_to_be_used():
    print("This is inside the function !!")
function_to_be_used = hello_decorator(function_to_be_used)
 
function_to_be_used()


#2
import time
import math

def decorator2(func):
    def inner2(*args,**kwargs):
        begin=time.time()
        func(*args,**kwargs)
        end=time.time()
        print('Name of the function:',func.__name__)
        print('Time taken',end-begin)
    return inner2
@decorator2
def func2(x):
    print(math.factorial(x))
func2(10)


#3
def decorator3(func):
    def inner3(*args,**kwargs):
        print('before execution')
        x=func(*args,**kwargs)
        print('after execution')
        return x
    return inner3
@decorator3
def func3(a,b):
    print('execution')
    return a*b 

print(func3(4,3))

#4 Chaining Decorators
def decorator4_1(func):
    def inner4():
        x=func()
        return x*x
    return inner4
def decorator4_2(func):
    def inner4():
        x=func()
        return x*2
    return inner4

@decorator4_1
@decorator4_2
def func4():
    return 10
print(func4())

@decorator4_2
@decorator4_1
def func4():
    return 10
print(func4())
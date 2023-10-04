#1 Recursion Function
def recursive_factorial(n):
  if n == 1:
      return n
  else:
      return n * recursive_factorial(n-1)
 
# user input
num = 6
 
# check if the input is valid or not
if num < 0:
  print("Invalid input !")
elif num == 0:
  print("1")
else:
  print("Factorial=",recursive_factorial(num))
  
  
#2 Inbuilt Function
list1=[1,2,6,4,5]
print(max(list1))
print(min(list1))



#3 Lambda Function
x = lambda a, b : a * b
print(x(5, 6))



#User defined Functions(We can do arithmatic functions and other operation inside a function and return the result easily)
def myFun1(*argv): 
    for arg in argv: 
        print (arg)
 
def myFun2(**kwargs): 
    for key, value in kwargs.items():
        print ("% s == % s" %(key, value))
        
print("Result of * args: ")
myFun1('Hello', 'Welcome', 'to', 'GeeksforGeeks')
 
print("\nResult of **kwargs")
myFun2(first ='Geeks', mid ='for', last ='Geeks') 
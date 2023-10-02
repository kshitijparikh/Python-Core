#While loop
# Sum of numbers until the user enters zero

total = 0

number = int(input('Enter a number: '))

# add numbers until number is zero
while number != 0:
    total += number   
    
    number = int(input('Enter a number: '))
    

print('total =', total)



#For loop
#Using zip() method

fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "green"]
for fruit, color in zip(fruits, colors):
    print(fruit, "is", color)
    
    
#Using range()

for i in range(0, 10, 2):
    print(i)
    
    
#Dictionary Iteration

print("Dictionary Iteration")
 
d = dict()
 
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("% s % d" % (i, d[i]))
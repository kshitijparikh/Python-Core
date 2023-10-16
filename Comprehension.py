'''
[ k*k for k in range(1, n+1) ] list comprehension
{ k*k for k in range(1, n+1) } set comprehension
( k*k for k in range(1, n+1) ) generator comprehension
{ k : k*k for k in range(1, n+1) } dictionary comprehension

'''


#List Comprehension : Syntax for Set, Tuple Comperehension is all similar
#1 
list1=[1,2,3,4,5,6,7,8,9]
lc1=[i for i in list1 if i%2==0]
print(lc1)

#2
lc2=[i**2 for i in range(1,10)]
print(lc2)

#3
planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']]
lc4=[planet for sublist in planets for planet in sublist if len(planet)<6]
print(lc4)

#4
lc5=[[i for i in range(5)] for j in range(5)]
print(lc5)

#Dictionary Comprehension
#1
dc1={keys:keys**2 for keys in range(1,6)}
print(dc1)

#2
dc2={keys:keys**2 for keys in range(11) if keys%2==0}
print(dc2)

#3
state = ['Gujarat', 'Maharashtra', 'Rajasthan']
capital = ['Gandhinagar', 'Mumbai', 'Jaipur']
dc3={keys:value for (keys,value) in zip(state,capital)}
print(dc3)


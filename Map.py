'''
map() function returns a map object(which is an iterator) 
of the results after applying the given function to each item of a given iterable (list, tuple etc.)

'''
#1
def func1(x):
    return x*x
list1=[1,2,3,4]
print(list(map(func1,list1)))

#2
list2=[0,5,10]
map2=map(lambda x: x+5,list2)
print(list(map2))

#3
list3_1=[1,2,3]
list3_2=[3,3,3]
map3=map(lambda x,y:x+y,list3_1,list3_2)
print(list(map3))

#4
list4=['sat','pat']
map4=map(list,list4)
print(list(map4))

#5
list5_1=[10,20,30]
list5_2=[5,10,15]
list5_3=[3,3,3]
map5=map(lambda x,y,z: x*x+2*y+z,list5_1,list5_2,list5_3)
print(list(map5))


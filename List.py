list1=[1,2,3,4,5,1,6]

#len()
print(len(list1))

#count()
print(list1.count(1))

#Other arithematic operations : .sum(), .min(), .avg(), .max()

#index() [Just remember that it returns the first occurence)
print(list1.index(3))

#sort()
list1.sort()
print(list1)

#reverse()
list1=[1,2,3,4,5,1,6]
list1.reverse()
print(list1)

#append()
list1=[1,2,3,4,5,1,6]
list1.append([7,8,9])
print(list1)

#extend()
list1=[1,2,3,4,5,1,6]
list1.extend([7,8,9])
print(list1)

#insert()
list1=[1,2,3,4,5,1,6]
list1.insert(7,7)
print(list1)

#pop() : Takes in index
x=list1.pop(7)
print(x, list1)

#remove(): Takes in item
list1.remove(6)
print(list1)

#del(): Also takes index but in a different way
del list1[5]
print(list1)

#join() : While using this list has to have string elements
list1=['abc','abc']
x=''.join(list1)
print(x)

#copy()
list2=list1.copy()



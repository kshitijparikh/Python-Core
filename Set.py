set1={1,2,4,5}

#add()
set1.add(3)
print(set1)

#discard()
set1={1,2,4}
set1.discard(4)
print(set1)

#remove()
set1={1,2,4}
set1.remove(4)
print(set1)

#pop() : Happens randomly unlike discard() where we have to give a specific element
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)

#clear()
set1.clear()
print(set1)

#copy()
set1={1,2,3}
set2=set1.copy()

#difference()
set1={'1','2','3'}
set2={'1','2'}
x=set1.difference(set2)
print(x)

#difference_update() : Updates set1 instead of creating a new set
set1.difference_update(set2)
print(set1)

#intersection()
set1={'1','2','3'}
set2={'1','2'}
print(set2.intersection(set1))

#intersection_update()
set1={'1','2','3'}
set2={'1','2'}
set1.intersection_update(set2)
print(set1)

#isdisjoint()
set1={'1','2','3'}
set2={'1','2'}
print(set1.isdisjoint(set2))

#issubset()
print(set2.issubset(set1))

#issuperset()
print(set1.issuperset(set2))

#symmetric_difference()
set1={1,2,3}
set2={3,4,5}
print(set1.symmetric_difference(set2))

#symmetric_difference_update()
set1={1,2,3}
set2={3,4,5}
set1.symmetric_difference_update(set2)
print(set1)

#union()
set1={1,2,3}
set2={4,5,6}
print(set1.union(set2))

#update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)
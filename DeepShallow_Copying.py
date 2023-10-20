#Keypoint: Only works in update and not append
#Deep_Copying
'''
A deep copy creates a new compound object before inserting copies of the items found in 
the original into it in a recursive manner. It means first constructing a new collection object and 
then recursively populating it with copies of the child objects found in the original. In the case of deep copy, 
a copy of the object is copied into another object. It means that any changes made to a copy of the object do not 
reflect in the original object. 

In layman terms: Instead of refrencing sub-objects inside a new object, deep copying creates new subobjects by recursion

'''

import copy

l1=[1,2,[3,0]]
print('Original List: ',l1)
l2=copy.deepcopy(l1)
l1[2][1]=4
print('Updated List: ', l1)
print('Created List stayed unupdated: ',l2)
print('')

#Shallow Copying
'''
A shallow copy creates a new compound object and then references the objects contained in the original within it, which means 
it constructs a new collection object and then populates it with references to the child objects found in the original. The copying 
process does not recurse and therefore won’t create copies of the child objects themselves. In the case of shallow copy, a reference 
of an object is copied into another object. It means that any changes made to a copy of an object do reflect in the original object. 
In python, this is implemented using the “copy()” function. 

In layman terms: Instead of creating new subobjects and injecting them into new object, subobjects are referenced in the new object.

'''
l1=[1,2,[3,0]]
print('Original List: ',l1)
l2=copy.copy(l1)
l1[2][1]=4
print('Updated List: ', l1)
print('Created List gets updated: ',l2)

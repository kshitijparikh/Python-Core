#Iterators : An object that include countable number of values
#Iterables: Containers from which countable values or in other words iterators are derived

#===============================================================================================#
#Method 1 Using iter() method
#Datatype 1 : Tuple
mytuple = ("Gandhinagar", "Ahmedabad", "Surat")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#Datatype 2: String
mystr = "shake"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#Datatype 3: List,Set
mylist = [2,3,3,5,6]
myit = iter(mylist)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#Datatype 4: Class Object 
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)


#================================================================================================#
#Method 2: Using a loop (Tuple,Dictionary,Set,String,etc.)

#Datatype 1: List,Tuples,Sets
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

#Datatype 2: String  
mystr='Gandhinagar'

for x in mystr:
    print(x)
    
    

#1  
class Employee:
  
    # Initializing
    def __init__(self):
        print('Employee created')
  
    # Calling destructor
    def __del__(self):
        print("Destructor called")
  
def Create_obj():
    print('Making Object...')
    obj = Employee()
    print('function end...')
    return obj
  
print('Calling Create_obj() function...')
obj = Create_obj()
print('Program End...')


#2
class Animals:  
    
    #  we will initialize the class  
    def __init__(self):  
        print('The class called Animals is CREATED.')  
    
    # now, we will Call the destructor  
    def __del__(self):  
        print('The destructor is called for deleting the Animals.')  
    
object = Animals()  
del object  


#3
class Student:
  def __init__(self, name, age):
    self.name = name
    self.age = age

s = Student("Jimmy", 25)

print(s.name)
print(s.age)
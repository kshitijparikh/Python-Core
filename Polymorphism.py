#Polymorphism in Function

class Cat:
    def speak(self):
        print('Meow')

class Dog:
    def speak(self):
        print('Bark')
        
for i in [Dog(),Cat()]:
    x=i
    x.speak()        
    
    
#Polymorphism in Class using method overriding

class Animal:
    def legs(self):
       print(4)
    
    def speak(self):
        print(None)

class Cat(Animal):
    def speak(self):
        print('Meow')

class Dog(Animal):
    def speak(self):
        print('Bark') 
    

for i in [Cat(), Dog()]:
    obj=i
    obj.legs()
    obj.speak()
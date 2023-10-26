#Public Variables
class person:
    def __init__(self,name,age,place):
        self.age=age
        self.name=name
        self.place=place
    
    def describe(self):
        print(self.name)
        print(self.age)
        print(self.place)
    
p1=person('Kshitij', 24, 'Gandhinagar')
p1.describe()

#Protected Variables
class Person:
    _day='Monday'
    def __init__(self,name,age,place):
        self._age=age
        self._name=name
        self._place=place
class Human(Person):
    def __init__(self,name,place,age):
        Person.__init__(self,name,age,place)
    def describe(self):
        print(self._name)
        print(self._place)
        print(self._age)
        print(self._day)
        

h1=Human('Kshitij',24, 'Gandhinagar')
h1.describe()


#Private Variables
class Person:
    def __init__(self,name,age,place):
         self.__name=name
         self.__age=age
         self.__place=place
class Human(Person):
    def describe(self):
        print(self.__name)
h1=Person('Kshitij',24,'Gandhinagar')
try:
    h1.describe()
except:
    print('Cannot access Private variables')
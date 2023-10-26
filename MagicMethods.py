'''
Initialization and Construction

__new__: To get called in an object’s instantiation.
__init__: To get called by the __new__ method.
__del__: It is the destructor.


Numeric magic methods

__trunc__(self): Implements behavior for math.trunc()
__ceil__(self): Implements behavior for math.ceil()
__floor__(self): Implements behavior for math.floor()
__round__(self,n): Implements behavior for the built-in round()
__invert__(self): Implements behavior for inversion using the ~ operator.
__abs__(self): Implements behavior for the built-in abs()
__neg__(self): Implements behavior for negation
__pos__(self): Implements behavior for unary positive 


Arithmetic operators

__add__(self, other): Implements behavior for math.trunc()
__sub__(self, other): Implements behavior for math.ceil()
__mul__(self, other): Implements behavior for math.floor()
__floordiv__(self, other): Implements behavior for the built-in round()
__div__(self, other): Implements behavior for inversion using the ~ operator.
__truediv__(self, other): Implements behavior for the built-in abs()
__mod__(self, other): Implements behavior for negation
__divmod__(self, other): Implements behavior for unary positive 
__pow__: Implements behavior for exponents using the ** operator.
__lshift__(self, other): Implements left bitwise shift using the << operator.
__rshift__(self, other): Implements right bitwise shift using the >> operator.
__and__(self, other): Implements bitwise and using the & operator.
__or__(self, other): Implements bitwise or using the | operator.
__xor__(self, other): Implements bitwise xor using the ^ operator.


String Magic Methods

__str__(self): Defines behavior for when str() is called on an instance of your class.
__repr__(self): To get called by built-int repr() method to return a machine readable representation of a type.
__unicode__(self): This method to return an unicode string of a type.
__format__(self, formatstr): return a new style of string.
__hash__(self): It has to return an integer, and its result is used for quick key comparison in dictionaries.
__nonzero__(self): Defines behavior for when bool() is called on an instance of your class. 
__dir__(self): This method to return a list of attributes of a class.
__sizeof__(self): It return the size of the object.


Comparison magic methods

__eq__(self, other): Defines behavior for the equality operator, ==.
__ne__(self, other): Defines behavior for the inequality operator, !=.
__lt__(self, other): Defines behavior for the less-than operator, <.
__gt__(self, other): Defines behavior for the greater-than operator, >.
__le__(self, other): Defines behavior for the less-than-or-equal-to operator, <=.
__ge__(self, other): Defines behavior for the greater-than-or-equal-to operator, >=.

'''

#1
import math

class Complex:
    def __init__(self, re=0, im=0): 
        self.re = re
        self.im = im
    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Complex(self.re + other,self.im)
        elif  isinstance(other, Complex):
            return Complex(self.re + other.re , self.im + other.im)
        else:
            raise TypeError
    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Complex(self.re - other,self.im)
        elif  isinstance(other, Complex):
            return Complex(self.re - other.re, self.im - other.im)  
        else:
            raise TypeError
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Complex(self.re * other, self.im * other)
        elif isinstance(other, Complex):
        #   (a+bi)*(c+di) = ac + adi +bic -bd
            return Complex(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)
        else:
            raise TypeError
    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Complex(self.re / other, self.im / other)
        elif isinstance(other, Complex):
            x = other.re
            y = other.im
            u = self.re
            v = self.im
            repart = 1/(x**2+y**2)*(u*x + v*y)
            impart = 1/(x**2+y**2)*(v*x - u*y)
            return Complex(repart,impart)
        else:
            raise TypeError
    def value(self):
        return math.sqrt(self.re**2 + self.im**2)
    def __eq__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return  self.value() == other
        elif  isinstance(other, Complex):
            return  self.value() == other.value()
        else:
            raise TypeError
    def __lt__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return  self.value() < other
        elif  isinstance(other, Complex):
            return  self.value() < other.value()
        else:
            raise TypeError
    def __gt__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return  self.value() > other
        elif  isinstance(other, Complex):
            return  self.value() > other.value()
        else:
            raise TypeError
    def __str__(self):
        if self.im>=0:
            return f"{self.re}+{self.im}i"
        else:
            return f"{self.re}{self.im}i"
    def __len__(self):
           return int(math.sqrt(self.re**2 + self.im**2))
        
a=Complex(3,4)
b=Complex(4,5)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a>b)
print(a<b)
print(a==b)
print(len(a))

#2
class TransactionBook:
    def __init__(self, user_id, shares=[]):
        self.user_id = user_id
        self.shares = shares
    def add_trade(self, name , quantity, buySell):
        self.shares.append([name,quantity,buySell])
    def __getitem__(self, i):
        return self.shares[i]

t1=TransactionBook('Kshitij')
t1.add_trade('ABC',2,'B')
t1.add_trade('abc',2,'B')
t1.add_trade('ABCC',2,'S')
print(t1[1])
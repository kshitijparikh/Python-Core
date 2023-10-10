
# SyntaxError: This exception is raised when the interpreter encounters a syntax error in the code, such as a misspelled keyword, a missing colon, or an unbalanced parenthesis.
# TypeError: This exception is raised when an operation or function is applied to an object of the wrong type, such as adding a string to an integer.
# NameError: This exception is raised when a variable or function name is not found in the current scope.
# IndexError: This exception is raised when an index is out of range for a list, tuple, or other sequence types.
# KeyError: This exception is raised when a key is not found in a dictionary.
# ValueError: This exception is raised when a function or method is called with an invalid argument or input, such as trying to convert a string to an integer when the string does not represent a valid integer.
# AttributeError: This exception is raised when an attribute or method is not found on an object, such as trying to access a non-existent attribute of a class instance.
# IOError: This exception is raised when an I/O operation, such as reading or writing a file, fails due to an input/output error.
# ZeroDivisionError: This exception is raised when an attempt is made to divide a number by zero.
# ImportError: This exception is raised when an import statement fails to find or load a module.

#1
try: 
    k = 5//0   
    print(k) 
  
except ZeroDivisionError: 
    print("Can't divide by zero") 
  
finally: 
    print('This is always executed')
    
#2
list1=[None,None,None]
i=0
while True:
    try:
        list1[i]=1
        i=i+1
        if i>=len(list1):raise IndexError
    except IndexError:
        print('Dont try buffer overflow attacks in Python')
        break
    
#3
def func1(filepath):
    f=open(filepath)
    lines=[]
    while True:
        try:
            line=f.readline()
            if line=='':raise EOFError
            lines.insert(0,line[:-1])
        except EOFError:
            for i in lines:
                print(i)
            return 
func1(r'C:\Users\k.park99\Desktop\sample.txt')
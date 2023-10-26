#1
class Operation:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    @staticmethod
    def add(x,y):
        return x+y

obj1=Operation(10,20).add(10,20)
print(obj1)


#2
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y == 0:
            return "Cannot divide by zero."
        return x / y

class ComplexCalculator:
    @staticmethod
    def complex_operation(a, b, operation):
        if operation == 'add':
            result = MathOperations.add(a, b)
        elif operation == 'subtract':
            result = MathOperations.subtract(a, b)
        elif operation == 'multiply':
            result = MathOperations.multiply(a, b)
        elif operation == 'divide':
            result = MathOperations.divide(a, b)
        else:
            result = "Invalid operation"
        return result

# Using static methods
result1 = MathOperations.add(10, 5)
result2 = ComplexCalculator.complex_operation(8, 4, 'multiply')
result3 = ComplexCalculator.complex_operation(20, 0, 'divide')

print("Result 1:", result1)
print("Result 2:", result2)
print("Result 3:", result3)

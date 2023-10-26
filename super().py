class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

class Address:
    def __init__(self, street, city, zip_code):
        self.street = street
        self.city = city
        self.zip_code = zip_code

    def display_address(self):
        print(f"Address: {self.street}, {self.city} {self.zip_code}")

class ContactInfo(Person, Address):
    def __init__(self, name, age, street, city, zip_code, email):
        # Call the constructors of both parent classes
        Person.__init__(self, name, age)
        Address.__init__(self, street, city, zip_code)
        self.email = email

    def introduce(self):
        super().introduce()  # Call the introduce method of the Person class
        print(f"Email: {self.email}")

    def display_address(self):
        super().display_address()  # Call the display_address method of the Address class
        print(f"Email: {self.email}")

class Student(ContactInfo):
    def __init__(self, name, age, street, city, zip_code, email, student_id):
        super().__init__(name, age, street, city, zip_code, email)
        self.student_id = student_id

    def introduce(self):
        super().introduce()  # Call the introduce method of the ContactInfo class
        print(f"Student ID: {self.student_id}")

student = Student("Alice", 20, "123 Main St", "Springfield", "12345", "alice@example.com", "S12345")
student.introduce()
student.display_address()
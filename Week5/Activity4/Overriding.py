
class Person:
    def __init__(self, name, address, age, ID):
        # Initialize basic person details
        self.name = name
        self.address = address
        self.age = age
        self.ID = ID


class Student(Person):
    def __init__(self, name, address, age, ID):
        # Use Person's __init__ to set common info
        super().__init__(name, address, age, ID)

    def greet(self):
        # Show basic person information
        print("Greeting from Person class, Hello " + self.name)


def main():
    student1 = Student("Allan", "123 Flat Bush St", 20, "S123")
    student1.greet()


if __name__ == "__main__":
    main()
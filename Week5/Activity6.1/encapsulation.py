#Can you add one more method to the class that uses the private attribute? 
#Also, please create a new class to demonstrate the use of the public and protected attributes. 

# Encapsulation = hiding internal details and controlling access to data

class Student:
    def __init__(self, name, age):
        # PUBLIC attribute: accessible from anywhere
        self.name = name 
        
        # PROTECTED attribute: intended for class and subclasses only (convention: single _)
        self._age = age 
        
        # PRIVATE attributes: only accessible within this class (convention: double __)
        self.__grade = 'A' 
        self.__address = '888 yard st'

    # Method using PRIVATE attribute - this is encapsulation in action!
    def get_address(self):
        """Controlled access to private address data"""
        return self.__address

    # Another method using PRIVATE attribute
    def get_grade(self):
        """Controlled access to private grade data"""
        return self.__grade
    
    # Additional method using PRIVATE attribute
    def set_grade(self, new_grade):
        """Controlled way to modify private grade with validation"""
        if new_grade in ['A+', 'B+', 'C+', 'D+', 'F+']:
            self.__grade = new_grade
            return f"Grade updated to {new_grade}"
        return "Invalid grade!"
        

# INHERITANCE + ENCAPSULATION
class Stud_info(Student):
    def __init__(self, name, age):
        super().__init__(name, age)  # Call parent constructor

    # Accessing PROTECTED attribute (allowed in subclass)
    def get_age(self):
        """Can access protected _age because this is a subclass"""
        return self._age
    
    # Accessing PUBLIC attribute
    def get_name(self):
        """Public attributes are accessible everywhere"""
        return self.name

# CREATING OBJECTS
s = Student('Allan', 20)
info = Stud_info('Vian', 18)

# DEMONSTRATING ENCAPSULATION LEVELS:

print("=== PUBLIC ACCESS ===")
print(s.name)  # Direct access to public attribute - OK!

print("\n=== PRIVATE ACCESS (Proper Way) ===")
print(s.get_address())  # Must use method to access private data - ENCAPSULATION!
print(s.get_grade())    # Methods provide controlled access to private data

print("\n=== INHERITANCE + ENCAPSULATION ===")
print(info.get_age())   # Subclass can access protected attribute
print(info.get_name())  # Subclass can access public attribute

print("\n=== NEW METHOD DEMO ===")
print(s.set_grade('B+'))  # Using private attribute with validation
print(s.get_grade())     # Verify the change

# ENCAPSULATION VIOLATIONS (what NOT to do):
print("\n=== WHAT HAPPENS IF WE BREAK ENCAPSULATION ===")

# This works but breaks the protected convention:
print(f"Direct protected access: {info._age}")  # Not recommended!

# This would cause an error (uncomment to see):
# print(s.__grade)  # AttributeError! Private attributes are name-mangled

# The actual mangled name would be:
print(f"Name demo: {s._Student__grade}")  # This works but defeats the purpose!

print("\n=== ENCAPSULATION SUMMARY ===")
print("Public (name): Accessible everywhere")
print("Protected (_age): Accessible in class and subclasses")  
print("Private (__grade): Only accessible through class methods")
print("Encapsulation protects data and provides controlled access!")
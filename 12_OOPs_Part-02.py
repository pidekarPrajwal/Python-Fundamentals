"""
===================================================================
  OBJECT-ORIENTED PROGRAMMING (OOP) - PART 02: THE 4 PILLARS OF OOP
===================================================================

This module covers the 4 fundamental pillars of Object-Oriented Programming:
  1. Encapsulation
  2. Inheritance
  3. Polymorphism
  4. Abstraction
"""

from abc import ABC, abstractmethod

# =================================================================
# PILLAR 1: ENCAPSULATION
# =================================================================
"""
1. ENCAPSULATION
----------------
- Definition: Encapsulation is the bundling of data (attributes) and methods 
  (functions) into a single unit (class) while restricting direct access to 
  some of the object's components.
- Why Use It?: 
  - Prevents accidental modification of internal data.
  - Ensures data validation before updating attributes.
  - Promotes security and modularity.

Access Specifiers in Python (Naming Conventions):
  - Public: Accessible from anywhere inside or outside the class (e.g., self.name).
  - Protected: Intended for internal class and subclass access (e.g., self._age).
    (Indicated by a single underscore '_', enforced by convention).
  - Private: Accessible ONLY inside the defining class (e.g., self.__balance).
    (Indicated by double underscore '__', enforced by Python Name Mangling: _ClassName__attribute).

Getters and Setters:
  - Methods or @property decorators used to safely retrieve (get) and update (set) private attributes.
"""

class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder  # Public attribute
        self._account_type = "Savings"        # Protected attribute
        self.__balance = initial_balance      # Private attribute

    # Getter for balance using @property decorator
    @property
    def balance(self):
        return self.__balance

    # Setter for balance with validation
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Error: Balance cannot be negative!")
        else:
            self.__balance = amount
            print(f"Balance updated successfully to: ${self.__balance}")

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New Balance: ${self.__balance}")
        else:
            print("Invalid deposit amount!")

    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. Remaining Balance: ${self.__balance}")
        else:
            print("Insufficient funds or invalid amount!")


print("=========================================================")
print("  1. ENCAPSULATION DEMONSTRATION")
print("=========================================================")

account = BankAccount("Prajwal", 1000.0)
print(f"Account Holder (Public): {account.account_holder}")
print(f"Account Type (Protected): {account._account_type}")
print(f"Balance via Getter (@property): ${account.balance}")

# Depositing and withdrawing
account.deposit(500.0)
account.withdraw(200.0)

# Updating balance via property setter
account.balance = 2000.0
account.balance = -500.0  # Should trigger validation error

# Attempting direct private access (Raises AttributeError)
try:
    print(account.__balance)
except AttributeError as e:
    print(f"Direct private access failed: {e}")

# Accessing private attribute via Name Mangling (_ClassName__attribute)
print(f"Access via Name Mangling: ${account._BankAccount__balance}")


# =================================================================
# PILLAR 2: INHERITANCE
# =================================================================
"""
2. INHERITANCE
--------------
- Definition: Inheritance is the mechanism by which a child class (derived class) 
  inherits attributes and methods from a parent class (base class).
- Why Use It?:
  - Promotes code reusability and eliminates duplication.
  - Establishes an 'IS-A' relationship (e.g., Dog IS-A Animal).
  - Allows extending functionality without modifying existing parent code.

Types of Inheritance in Python:
  1. Single Inheritance: Child inherits from 1 Parent class.
  2. Multi-Level Inheritance: Child inherits from Parent, which inherits from Grandparent.
  3. Multiple Inheritance: Child inherits from 2 or more Parent classes.
  4. Hierarchical Inheritance: Multiple Child classes inherit from 1 Parent class.
  5. Hybrid Inheritance: Combination of two or more inheritance types.

Key Concepts:
  - super(): Built-in function to invoke parent class constructors or methods.
  - Method Resolution Order (MRO): The order in which Python searches for methods in inheritance hierarchies (accessible via `__mro__` or `.mro()`).
"""

# --- 2.1 Single-Level Inheritance ---
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"Vehicle: {self.brand} {self.model}"

class Car(Vehicle):  # Single Inheritance
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)  # Calling parent constructor
        self.num_doors = num_doors

    def display_car_info(self):
        return f"{self.display_info()} with {self.num_doors} doors"

# --- 2.2 Multi-Level Inheritance ---
class ElectricCar(Car):  # Multi-Level Inheritance (Vehicle -> Car -> ElectricCar)
    def __init__(self, brand, model, num_doors, battery_capacity):
        super().__init__(brand, model, num_doors)
        self.battery_capacity = battery_capacity

    def display_electric_info(self):
        return f"{self.display_car_info()}, Battery: {self.battery_capacity} kWh"

# --- 2.3 Multiple Inheritance & MRO ---
class Engine:
    def start_engine(self):
        return "Engine started with fuel."

class Motor:
    def start_engine(self):
        return "Electric motor activated."

class HybridCar(Engine, Motor):  # Multiple Inheritance
    def __init__(self, name):
        self.name = name

print("\n=========================================================")
print("  2. INHERITANCE DEMONSTRATION")
print("=========================================================")

tesla = ElectricCar("Tesla", "Model S", 4, 100)
print(tesla.display_electric_info())

# Multiple Inheritance & MRO demonstration
prius = HybridCar("Prius")
print(f"Hybrid Car Engine Start: {prius.start_engine()}")
print("Method Resolution Order (MRO) for HybridCar:")
for cls in HybridCar.__mro__:
    print(f"  -> {cls.__name__}")


# =================================================================
# PILLAR 3: POLYMORPHISM
# =================================================================
"""
3. POLYMORPHISM
---------------
- Definition: Polymorphism means "many forms". It allows objects of different classes 
  to respond to the same method call in unique ways.
- Why Use It?:
  - Provides flexibility and uniformity in code design.
  - Allows writing clean, generic interface code that handles multiple object types.

Forms of Polymorphism in Python:
  1. Method Overriding: Child class redefines a method present in its Parent class.
  2. Duck Typing: "If it walks like a duck and quacks like a duck, it's a duck."
     Python checks for method presence rather than formal object type.
  3. Operator Overloading: Redefining built-in operators (+, -, *, ==) using dunder methods (__add__, __str__, etc.).
  4. Method Overloading (Simulated): Python does not support traditional method overloading natively;
     it is achieved using default arguments or *args / **kwargs.
"""

# --- 3.1 Method Overriding ---
class Shape:
    def area(self):
        return "Area formula not defined for generic shape."

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):  # Overriding parent area method
        return 3.14159 * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):  # Overriding parent area method
        return self.width * self.height

# --- 3.2 Duck Typing ---
class PDFDocument:
    def show(self):
        return "Displaying PDF document content."

class WordDocument:
    def show(self):
        return "Displaying Word document content."

def render_document(doc):  # Duck typing in action (expects any object with a .show() method)
    return doc.show()

# --- 3.3 Operator Overloading ---
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):  # Overloading '+' operator
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

print("\n=========================================================")
print("  3. POLYMORPHISM DEMONSTRATION")
print("=========================================================")

# Method Overriding Example
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(f"Area of {type(shape).__name__}: {shape.area()}")

# Duck Typing Example
docs = [PDFDocument(), WordDocument()]
for d in docs:
    print(render_document(d))

# Operator Overloading Example
c1 = ComplexNumber(2, 3)
c2 = ComplexNumber(4, 5)
c3 = c1 + c2  # Calls c1.__add__(c2)
print(f"Complex Number Addition ({c1}) + ({c2}) = {c3}")


# =================================================================
# PILLAR 4: ABSTRACTION
# =================================================================
"""
4. ABSTRACTION
--------------
- Definition: Abstraction is the concept of hiding complex internal implementation 
  details and exposing only essential, high-level features to the user.
- Why Use It?:
  - Reduces code complexity.
  - Enforces design rules and contracts across subclasses.
  - Enhances code maintainability.

Implementation in Python:
  - Python uses the `abc` (Abstract Base Class) module.
  - Abstract Base Class: Inherits from `abc.ABC`. Cannot be instantiated directly.
  - Abstract Method: Marked with `@abstractmethod`. MUST be overridden by any concrete subclass.
"""

class PaymentGateway(ABC):  # Abstract Base Class
    @abstractmethod
    def process_payment(self, amount):
        """Abstract method to process payment."""
        pass

    @abstractmethod
    def generate_receipt(self, transaction_id):
        """Abstract method to generate receipt."""
        pass

    # Concrete method inside abstract class
    def common_security_check(self):
        return "Security Check Passed: Connection encrypted via TLS 1.3."

class CreditCardPayment(PaymentGateway):
    def process_payment(self, amount):
        return f"Processed Credit Card payment of ${amount}"

    def generate_receipt(self, transaction_id):
        return f"Credit Card Receipt generated for TXN ID: {transaction_id}"

class PayPalPayment(PaymentGateway):
    def process_payment(self, amount):
        return f"Processed PayPal payment of ${amount}"

    def generate_receipt(self, transaction_id):
        return f"PayPal Receipt generated for TXN ID: {transaction_id}"

print("\n=========================================================")
print("  4. ABSTRACTION DEMONSTRATION")
print("=========================================================")

# Attempting to instantiate Abstract Class directly (Raises TypeError)
try:
    pg = PaymentGateway()
except TypeError as e:
    print(f"Cannot instantiate Abstract Class: {e}")

# Working with Concrete Subclasses
cc = CreditCardPayment()
print(cc.common_security_check())
print(cc.process_payment(250.0))
print(cc.generate_receipt("TXN_CC_99812"))

paypal = PayPalPayment()
print(paypal.process_payment(120.0))
print(paypal.generate_receipt("TXN_PP_44321"))


# =================================================================
# SUMMARY OF BEST PRACTICES & COMMON MISTAKES:
# =================================================================
# 1. ENCAPSULATION: Always use getters/setters (@property) for private data rather than accessing mangled names directly.
# 2. INHERITANCE: Favor Composition over Inheritance if the relationship is "HAS-A" instead of "IS-A".
# 3. POLYMORPHISM: Use Duck Typing responsibly; handle missing method errors if unexpected objects are passed.
# 4. ABSTRACTION: Ensure ALL abstract methods defined in an ABC are implemented in concrete child classes; missing one causes instant instantiation failure.
"""
Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class
(subclass or derived class) to inherit properties and methods from an existing class (base class or parent class).
"""

class Animal():
    def __init__(self):
        self.num_of_eyes=2

    def breathe(self):
        print("inhale and exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()
    def breathe(self):
        super().breathe()
        print("under the water")
    def swim(self):
        print("moving in water")

namo=Fish()
namo.breathe()
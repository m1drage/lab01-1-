
from materials.base import Material

class Laminate(Material):
    def calculate_area(self):
        return self.length * self.width

    def calculate_cost(self):
        return self.calculate_area() * 1.8

    def __str__(self):
        return "Ламинат"

    def __repr__(self):
        return f"Laminate(length={self.length}, width={self.width})"

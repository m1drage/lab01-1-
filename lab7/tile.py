
from materials.base import Material

class Tile(Material):
    def calculate_area(self):
        return self.length * self.width

    def calculate_cost(self):
        return self.calculate_area() * 2.5

    def __str__(self):
        return "Плитка"

    def __repr__(self):
        return f"Tile(length={self.length}, width={self.width})"

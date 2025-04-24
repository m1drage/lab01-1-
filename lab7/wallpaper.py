
from materials.base import Material

class Wallpaper(Material):
    def calculate_area(self):
        return self.length * self.width

    def calculate_cost(self):
        return self.calculate_area() * 1.2

    def __str__(self):
        return "Обои"

    def __repr__(self):
        return f"Wallpaper(length={self.length}, width={self.width})"

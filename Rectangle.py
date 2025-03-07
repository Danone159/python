class Rectangle:
    def __init__(self, width: float, height: float, x: float, y: float):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def update_dimensions(self, width: float, height: float):
        self.width = width
        self.height = height

    def get_dimensions(self):
        return self.width, self.height

    def is_square(self):
        return self.width == self.height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def move(self, dx: float, dy: float):
        self.x += dx
        self.y += dy

if __name__ == "__main__":
    r = Rectangle(8, 5, 1, 2)
    print("Rozmery:", r.get_dimensions())
    print("Je to štvorec?", r.is_square())
    print("Obsah:", r.get_area())
    print("Obvod:", r.get_perimeter())

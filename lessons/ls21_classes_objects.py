"""Examples of object-oriented programming concepts."""

class Point:

    # Defining attributes(related variables) of our class
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point by giving x and y args."""
        self.x = x
        self.y = y
    
    def __repr__(self) -> str:
        """Magic metjid to represent object as string."""
        return f"{self.x}, {self.y}"
    
    def invert(self) -> None:
        """Method to inver† the attributes (swap) pf the Point."""
        temp: float = self.x
        self.x = self.y
        self.y = temp




a: Point = Point(4.0, 5.0)
print(a.__repr__()) # The same as print(a)
a.invert()
print(a.x)
print(a.y)

b: Point = Point(0.0, 0.0)
#Assign to attributes of an object.
b.x = 2.0
b.y = -1.0
print(b)

"""Examples of obeject-oriented programming concepts."""

from __future__ import annotations

class Point:
    # Defining attributes (related variables)
    # of our class
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point by giving x and y args."""
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """Magic methods to represent object as string."""
        return f"{self.x}, {self.y}"

    def scale_by(self, factor: float) -> None:
        """Example method that mutates object it is called on."""
        self.x *= factor
        self.y *= factor

    def __mul__(self, factor: float) -> Point:
        """Overload the multiplication operator fro a Point * float."""
        print("__mul__ was called")
        return Point(self.x * factor, self.y * factor)
    # dont need scale method now with this

    def scale(self, factor: float) -> Point:
        """Does not muatate object."""
        # x: float = self.x * factor
        # y: float = self.y * factor
        # p: Point = Point(x, y)
        # return p
        return Point(self.x * factor, self.y * factor)
    
    def __add__(self, rhs: Point) -> Point:
        """Add two point."""
        print("__add__ was called")
        return Point(self.x +rhs.x, self.y + rhs.y)

    def __getitem__(self, index: int) -> float:
        """Overload the subscroption notation."""
        if index == 0:
            return self.x
        elif index ==1:
            return self.y
        else:
            raise IndexError


a: Point = Point(1.0, 2.0)
# a.scale_by(2.0)

b: Point = a * 2.0
c: Point = a + b

print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")

print(a[0])
print(a[1])
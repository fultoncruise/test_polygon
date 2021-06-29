from polygon import Polygon, Triangle
from polygon import Rectangle
from polygon import Square
from polygon import Circle


def test_polygon():
    polygon = Polygon('yellow', 3)
    assert polygon.color == 'yellow'
    assert polygon.num_sides == 3


def test_triangle():
    triangle = Triangle('red', 4, 3)
    assert triangle.area() == 6.0
    assert triangle.num_sides == 3


def test_method_rectangle():
    rectangle = Rectangle("blue", 2.5, 2,)
    assert rectangle.area() == 5.0


def test_method_square():
    square = Square("green", 4)
    assert square.area() == 16


def test_method_circle():
    circle = Circle('yellow', 2)
    assert circle.area() == (12.57)
    assert circle.radius == (2)
    assert circle.color == 'yellow'
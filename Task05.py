import unittest


class Rectangle:
    """Класс, реализующий прямоугольник"""

    def __init__(self, width, height = None):
        self.__width = width
        if height is None:
            self.__height = width
        else:
            self.__height = height

    def perimeter(self):
        """Метод вычисления периметра прямоугольника"""
        return 2 * (self.__height + self.__width)

    def area(self):
        """Метод вычисления площади прямоугольника"""
        return self.__width * self.__height

    def __add__(self, other):
        return Rectangle((self.perimeter() + other.perimeter()) / 4)

    def __sub__(self, other):
        if other.perimeter() > self.perimeter():
            return Rectangle(0)
        return Rectangle((self.perimeter() - other.perimeter()) / 4)

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __str__(self):
        return f"Прямоугольник со сторонами {self.__height} и {self.__width}"

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"


class TestRectangle(unittest.TestCase):

    def test_perimeter(self):
        r = Rectangle(5, 5)
        self.assertEqual(r.perimeter(), 20, "Периметр неверен")

    def test_area(self):
        r = Rectangle(5, 5)
        self.assertEqual(r.area(), 25, "Площадь неверна")

    def test_add(self):
        r_1 = Rectangle(5, 5)
        r_2 = Rectangle(2, 2)
        r_3 = r_1 + r_2
        self.assertEqual(r_3.perimeter(), r_1.perimeter() + r_2.perimeter(), "Площадь неверна")


if __name__ == "__main__":
    unittest.main()


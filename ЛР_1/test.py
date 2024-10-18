import unittest
from shapes import Square, Triangle

class TestSquare(unittest.TestCase):

    def setUp(self):
        """Создаем экземпляр Square для тестов"""
        self.square = Square(2)

    def test_initialization_with_positive_side_length(self):
        """Проверяем инициализацию с положительной длиной стороны"""
        self.assertEqual(self.square.side_length, 2)

    def test_area_calculation(self):
        """Проверяем расчет площади квадрата"""
        self.assertEqual(self.square.area, 4)

    def test_perimeter_calculation(self):
        """Проверяем расчет периметра квадрата"""
        self.assertEqual(self.square.perimeter, 8)

    def test_side_length_setter_with_negative_value(self):
        """Проверяем, что установка отрицательной длины стороны вызывает ошибку"""
        with self.assertRaises(ValueError):
            self.square.side_length = -1

    def test_scale_function(self):
        """Проверяем функцию масштабирования квадрата"""
        self.square.scale(2)
        self.assertEqual(self.square.side_length, 4)

    def test_scale_function_with_negative_factor(self):
        """Проверяем, что масштабирование с отрицательным фактором вызывает ошибку"""
        with self.assertRaises(ValueError):
            self.square.scale(-1)


class TestTriangle(unittest.TestCase):

    def setUp(self):
        """Создаем экземпляр Triangle для тестов"""
        self.triangle = Triangle(3, 4, 5)

    def test_initialization_with_positive_sides(self):
        """Проверяем инициализацию с положительными длинами сторон"""
        self.assertEqual(self.triangle.a, 3)
        self.assertEqual(self.triangle.b, 4)
        self.assertEqual(self.triangle.c, 5)

    def test_initialization_with_invalid_sides(self):
        """Проверяем инициализацию с невалидными длинами сторон"""
        with self.assertRaises(ValueError):
            Triangle(1, 1, 3)  # Не образует треугольник

    def test_area_calculation(self):
        """Проверяем расчет площади треугольника"""
        self.assertAlmostEqual(self.triangle.area, 6)

    def test_perimeter_calculation(self):
        """Проверяем расчет периметра треугольника"""
        self.assertEqual(self.triangle.perimeter, 12)

    def test_invalid_side_length(self):
        """Проверяем, что установка отрицательной длины стороны вызывает ошибку"""
        with self.assertRaises(ValueError):
            self.triangle.a = -1


if __name__ == '__main__':
    unittest.main()

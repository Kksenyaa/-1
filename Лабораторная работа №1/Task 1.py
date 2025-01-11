# TODO Написать 3 класса с документацией и аннотацией типов

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass

from typing import List


class Point:
    """
    Класс для представления точки в двумерном пространстве.

    Attributes:
        x (float): Координата X.
        y (float): Координата Y.
    """

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_to_origin(self) -> float:
        """
        Возвращает расстояние от точки до начала координат.

        >>> Point(3, 4).distance_to_origin()
        5.0
        """
        return (self.x ** 2 + self.y ** 2) ** 0.5


class Rectangle:
    """
    Класс для представления прямоугольника.

    Attributes:
        width (float): Ширина прямоугольника.
        height (float): Высота прямоугольника.
    """

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        """
        Возвращает площадь прямоугольника.

        >>> Rectangle(5, 10).area()
        50.0
        """
        return self.width * self.height


class Student:
    """
    Класс для представления студента.

    Attributes:
        name (str): Имя студента.
        grades (List[float]): Список оценок.
    """

    def __init__(self, name: str, grades: List[float]):
        self.name = name
        self.grades = grades

    def average_grade(self) -> float:
        """
        Возвращает среднюю оценку студента.

        >>> Student("Иван", [4.0, 5.0, 3.0, 4.0]).average_grade()
        4.0
        """
        return sum(self.grades) / len(self.grades)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

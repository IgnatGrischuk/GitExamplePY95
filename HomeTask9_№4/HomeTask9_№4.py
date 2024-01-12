import math as m


class Sphere:

    def __init__(self, radius=None, value_one=0, value_two=0, value_three=0):
        if radius is None:
            self.radius = 1  # единичный радиус
            self.center = (0, 0, 0)  # центр в начале координат
        else:
            self.radius = radius
            self.center = (value_one, value_two, value_three)

    def get_volume(self):
        return (4 / 3) * m.pi * self.radius ** 3

    def get_square(self):
        return 4 * m.pi * self.radius * 2

    def get_radius(self):
        return self.radius

    def get_center(self):
        return self.center

    def set_radius(self, radius):
        self.radius = radius

    def set_center(self, value_one, value_two, value_three):
        self.center = (value_one, value_two, value_three)

    def is_point_inside(self, value_one, value_two, value_three):
        distance = m.sqrt((value_one - self.center[0]) ** 2
                          + (value_two - self.center[1]) ** 2
                          + (value_three - self.center[2]) ** 2)
        return distance <= self.radius


# Пример использования:

sphere_one = Sphere()  # создание сферы с единичным радиусом и центром в
# начале координат
print(sphere_one.get_volume())  # вывод объема
print(sphere_one.is_point_inside(0.7, 0.7, 0.7))   # проверка, находится ли
# точка внутри сферы

sphere_two = Sphere(radius=3, value_one=4, value_two=6, value_three=3)  #
# создание сферы с заданным радиусом и координатами центра
print(sphere_two.get_square())  # вывод площади внешней поверхности
print(sphere_two.get_center())  # вывод координат центра
sphere_two.set_radius(4)  # установка нового радиуса
print(sphere_two.get_radius())  # вывод нового радиуса

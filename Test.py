import math
from matplotlib import pyplot as plt


class Point_n:
    instances = 0

    def __init__(self, x=0.0, y=0.0):
        if -100 <= x <= 100:
            self.__x = x
        else:
            self.__x = 0

        if -100 <= y <= 100:
            self.__y = y

        else:
            self.__y = 0

        Point_n.instances += 1
        self.number = Point_n.instances


@property
def x(self):
    return self.__x


@x.setter
def x(self, value):
    if -100 <= value <= 100:
        self.__x = value
    else:
        self.__x = 0


@property
def y(self):
    return self.__y


@y.setter
def y(self, value):
    if -100 <= value <= 100:
        self.__y = value
    else:
        self.__y = 0


@classmethod
def count_instances(cls):
    return cls.instances


def move(self, dx, dy):
    self.__x += dx
    self.__y += dy


def distance_to(self, other):
    return math.sqrt((self.__x - other.__x) * 2 + (self.__y - other.__y) * 2)

    def __del__(self):
        print(f"Point {self.number} deleted.")


# Створюємо чотири точки


point1 = Point_n(1.0, 2.0)
point2 = Point_n(3.0, 4.0)
point3 = Point_n(5.0, 6.0)
point4 = Point_n(7.0, 8.0)

# Відображення точок перед змінами
plt.scatter([point1.x, point2.x, point3.x, point4.x], [point1.y, point2.y, point3.y, point4.y], label='Before')
plt.text(point1.x, point1.y, "Point 1")
plt.text(point2.x, point2.y, "Point 2")
plt.text(point3.x, point3.y, "Point 3")
plt.text(point4.x, point4.y, "Point 4")

# Відстань між другою і четвертою точкою
distance = point2.distance_to(point4)
print(f"Distance between point 2 and point 4: {distance}")

# Пересунути третю точку на 21 вліво
point3.move(-21, 0)

# Відображення точок після змін
plt.scatter([point1.x, point2.x, point3.x, point4.x], [point1.y, point2.y, point3.y, point4.y], label='After')
plt.text(point1.x, point1.y, "Point 1")
plt.text(point2.x, point2.y, "Point 2")
plt.text(point3.x, point3.y, "Point 3")
plt.text(point4.x, point4.y, "Point 4")

# Зберегти координати точок у текстовому файлі
with open("points.txt", "w") as file:
    if point1.number % 2 == 0:
        file.write(f"{point1.number}:{point1.x}:{point1.y}\n")
    else:
        file.write(f"{point1.number}:{point1.x};{point1.y}\n")

    if point2.number % 2 == 0:
        file.write(f"{point2.number}:{point2.x}:{point2.y}\n")
    else:
        file.write(f"{point2.number}:{point2.x};{point2.y}\n")

    if point3.number % 2 == 0:
        file.write(f"{point3.number}:{point3.x}:{point3.y}\n")
    else:
        file.write(f"{point3.number}:{point3.x};{point3.y}\n")

    if point4.number % 2 == 0:
        file.write(f"{point4.number}:{point4.x}:{point4.y}\n")
    else:
        file.write(f"{point4.number}:{point4.x};{point4.y}\n")

plt.legend()
plt.show()

class Rectangle:

 def __init__(self, width, height):
  self.width = width
  self.height = height

 def calculate_area(self):
  return self.width * self.height

 def calculate_perimeter(self):
  return 2 * (self.width + self.height)

# Создание трех объектов прямоугольника
rectangle1 = Rectangle(width = 6, height = 12)
rectangle2 = Rectangle(width = 5, height = 10)
rectangle3 = Rectangle(width = 4, height = 8)

# Расчет площади и периметра для каждого прямоугольника
area1 = rectangle1.calculate_area()
perimeter1 = rectangle1.calculate_perimeter()

area2 = rectangle2.calculate_area()
perimeter2 = rectangle2.calculate_perimeter()

area3 = rectangle3.calculate_area()
perimeter3 = rectangle3.calculate_perimeter()

# Вывод результатов в консоль
print("Прямоугольник 1:")
print("Площадь:", area1)
print("Периметр:", perimeter1)

print("\nПрямоугольник 2:")
print("Площадь:", area2)
print("Периметр:", perimeter2)

print("\nПрямоугольник 3:")
print("Площадь:", area3)
print("Периметр:", perimeter3)
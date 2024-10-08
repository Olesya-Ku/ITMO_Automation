class Car:
    def __init__(self, color="", car_type="", year=0):
        self.color = color
        self.car_type = car_type
        self.year = year

    def start(self):
        """Запуск авто"""
        print("Автомобиль заведен")

    def stop(self):
        """Отключение авто"""
        print("Автомобиль заглушен")

    def set_year(self, year):
        """Присвоение авто года выпуска"""
        self.year = year
        print(f"Год выпуска автомобиля : {self.year}")

    def set_type(self, car_type):
        """Присвоение авто типа"""
        self.car_type = car_type
        print(f"Тип автомобиля : {self.car_type}")

    def set_color(self, color):
        """Присвоение авто цвета"""
        self.color = color
        print(f"Цвет автомобиля : {self.color}")

# Пример использования класса Car
my_car = Car()

# Установка атрибутов и выполнение методов
my_car.start()
my_car.set_year(2024)
my_car.set_type("Кроссовер")
my_car.set_color("Чёрный")
my_car.stop()
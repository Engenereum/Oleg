class Bike:
    def __init__(self):
        self.color = "Black"
        self.height = 12
        self.max_speed = 22

    def get_color(self):
        print(f"Цвет: {self.color}")

    def ride(self, distance):
        time = distance / self.max_speed
        print(f"Минимальное время преодоления: {distance} километров, {time} часов")


bike = Bike()
bike2 = Bike()

bike2.get_color()
bike.get_color()
bike.color = "Red"
bike.get_color()
bike2.get_color()


class Computer:
    def __init__(self, proc):
        self.type_proc = proc
        self.type_comp = "Ноутбук"
        self.height = 3
        self.display = "1920 x 1080"

    def a(self):
        print(f"Тип процессора: {self.type_proc}")
        print(f"Тип компьютера: {self.type_comp}")
        print(f"Вес: {self.height}")
        print(f"Размер дисплея: {self.display}")

comp = Computer()
comp.a()
print("Компьютер запущен")


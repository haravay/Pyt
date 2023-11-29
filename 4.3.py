class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} поехала")
    def stop(self):
        print(f"{self.name} остановилась")
    def turn(self, direction):
        print(f"{self.name} повернула {direction}")
    def show_speed(self):
        print(f"Текущая скорость {self.name}: {self.speed} км/ч")

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Превышение скорости! {self.name} движется со скоростью {self.speed} км/ч")
        else:
            print(f"Текущая скорость {self.name}: {self.speed} км/ч")

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        speed = int(self.speed)
        if self.speed > 60:
            print(f"Превышение скорости! {self.name} движется со скоростью {self.speed} км/ч")
        else:
            print(f"Текущая скорость {self.name}: {self.speed} км/ч")

class PoliceCar(Car):
    pass

car = Car(80, "Красный", "Машина", False)
car.go()
car.turn("налево")
car.show_speed()
car.stop()

car = Car(50, "Зеленый", "Рабочая машина", False)
car.go()
car.turn("направо")
car.show_speed()
car.stop()

car = Car(90, "Синий", "Полицейская машина", True)
car.go()
car.turn("налево")
car.show_speed()
car.stop()
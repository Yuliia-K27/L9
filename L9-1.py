# створюємо клас автомобіль
class Car:
    # додаємо атрибути (марка, колір, об'єм двигуна)
    def __init__(self, brand, color, motor):
        self.brand = brand
        self.color = color
        self.motor = motor

    # додаємо методи (їхати вперед і назад)
    @staticmethod
    def forward():
        print('drive forward')

    @staticmethod
    def back():
        print('drive back')


# створюємо дочірній клас Motorbike від батьківського Car
class Motorbike(Car):
    # додаємо методи повороту вліво і вправо
    @staticmethod
    def right():
        print('turn right')

    @staticmethod
    def left():
        print('turn left')

# перевіряємо


Car = Motorbike('Scoda', 'grey', 1.6)
Car.left()
Car.back()
Car.right()
Car.forward()

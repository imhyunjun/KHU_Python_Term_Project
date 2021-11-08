
class Counter:
    def __init__(self, initValue = 0):
        self.count = initValue
    def increment(self):
        self.count += 1

a = Counter()
b = Counter(100)
print("카운터의 값 = ", a.count)
print("카운터의 값 = ", b.count)
a.increment()
b.increment()
print("카운터의 값 = ", a.count)
print("카운터의 값 = ", b.count)

class Car:
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model
    
    def drive(self, cur_speed):
        self.speed = cur_speed

myCar = Car(0, "blue", "E-class")

print("자동차 객체를 생성하였습니다.")
print("자동차의 속도는 ", myCar.speed)
print("자동차의 색상은 ", myCar.color)
print("자동차의 모델은 ", myCar.model)

myCar.drive(70)
print("자동차의 속도는 ", myCar.speed)

class Student:
    def __init__(self, name = None, age = 0):
        self.__name = name
        self.__age = age
    
    def getName(self):
        return self.__name

obj = Student("Hong", 20)
print(obj.getName())

a = Counter(1)
b = Counter(1)
print( a == b)
print( a is b)

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

u = Vector2D(0, 1)
v = Vector2D(1, 0)
w = Vector2D(1, 1)
a = u + v


from random import randint
class Dice:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__size = 30
        self.__value = 1
    def read_dice(self):
        return self.__value
    def print_dice(self):
        print("주사위의 값 = ", self.__value)
    def roll_dice(self):
        self.__value = randint(1, 6)

d = Dice(100, 100)
d.roll_dice()
d.print_dice()
        
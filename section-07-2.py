#상속 다중상속

#상속 기본
# 슈퍼클래스(부모) 및 서브클래스(자식) -> 모슨 속성, 메소드 사용 가능
#라면 -> 속성(종류, 회사, 맛, 면 종류, 이름) : 부모

class Car:
    """Prent  Class"""
    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def show(self):
        return 'Car Class "show method"'

class BmwCar(Car):
    """Sub class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name: %s" % self.car_name

class BenzCar(Car):
    """Sub class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name: %s" % self.car_name

    def show(self): #부모 메소드 오버라읻
        print(super().show())
        return 'Car Info : %s, %s, %s' % (self.car_name, self.type, self.color)


#일반 사용
model1 = BmwCar('520d', 'sedan', 'red')

print(model1.color) #부모에서 가져옴
print(model1.type) #부모에서 가져옴
print(model1.car_name) #Sub
print(model1.show()) #Sub
print(model1.__dict__) #Sub

# method Orerriding(오버라이딩)

model2 = BenzCar('520d', 'sedan', 'red')

print(model2.show());


# Inheritance Info
print(BmwCar.mro())
print(BenzCar.mro())



#다중 상속
class x():
    pass
class y():
    pass
class z():
    pass
class A(x, y):
    pass
class B(y, z):
    pass
class M(B, A, z):
    pass

print(M.mro()) #다중 상속 가능





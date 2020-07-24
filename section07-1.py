#파이썬 클래스 상세 이해
#self, 클래스, 인스턴스 변수

#선언
#class 클래스명:
 #   함수
 #   함수
 #   함수


#속성, 메소드
class UserInfo:
    def __init__(self, name):
        self.name = name
        print("초기화 :", name)
    def user_info_p(self):
         print("Name :", self.name)


user1 = UserInfo("kim")
user1.user_info_p()

user2 = UserInfo("Back")
user2.user_info_p()

print(id(user1))
print(id(user2))
print(user1.__dict__) #namespace출력
print(user2.__dict__)

#클래스, 인스턴스 차이
# 네임스페이스: 객체를 인스턴스화 할때 저장된 공간
#클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성
#인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용


#self의 이해

class SelfTest:
    def function1(): #self인자가 없기 때문에 self가 없는 것들은 공통으로 사용하는 메소드 클래스 메소드라고 보면됨
        print('function1')

    def funciton2(self): #인스턴스 메소드는 self가 있음
        print(id(self))
        print('function2')

slf_test = SelfTest();
#slf_test.function1() 에러 발생
slf_test.funciton2();

SelfTest.function1()

print(id(slf_test))
SelfTest.funciton2(slf_test)

# 클래스 변수, 인스턴스 변수

class WareHouse:
    #클래스 변수
    stock_num = 0

    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1
    def __del__(self):
        WareHouse.stock_num -= 1

user1 = WareHouse("KIm")
user2 = WareHouse("Park")
user3 = WareHouse("Lee")

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__) #클래스 네임스페이스 클래스 변수(공유


print(user1.stock_num) #자기 네임스페이스에 없으면 클래스 네임스페이스에서 찾고 그래도 없으면 에러
print(user2.stock_num)
print(user3.stock_num)

user1.__del__()

print(user1.stock_num)
print(user2.stock_num)
print(user3.stock_num)






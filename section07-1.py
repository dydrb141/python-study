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




#파이썬 흐름제어

print(type(True))
print(type(False))

if True:
    print("Yes")
if False:
    print("No")
else:
    print("yes2")


#관계연산자
# > >= < <= == !=

a = 10
b = 0

print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)

#참 거짓 종ㄹ류 (Ture, False)
# 참 : "내용", [내용], (내용"), {내용},1
# 거짓 : "" , [], (), {}, 0

city = ""

if city:
    print(">>>Ture")
else:
    print(">>>False")


#논리 연산자
# and or not
a = 100
b = 60
c = 15

print('and :', a > b > c)
print('or :', a > b or c > b)
print('not :', not a > b)
print('not :', not True)
print('not :', not False)


# 산술 , 관계, 논리 연산자
# 산술 > 관계 > 논리 순서로 적용

print('ex1 : ', 5 + 10 > 0 and not 7 + 3  == 10)

score1 = 90
score2 = 'A'

if score1 >= 90 and score2 == 'A':
    print("합격")
else:
    print("미안")

# 다중 조건문
num = 91
if num >= 90:
    print("num 등급 A", num)
elif num >= 80:
    print("num 등급 B", num)
else :
    print("꽝")

age = 27
hegiht = 175

if age >= 20:
    if hegiht >= 170:
        print("A지망 지원 가능")
    elif height >= 160:
        print("B지망 지원 가능")
    else:
        print("지원 불가")
else:
    print("20세 이상 지원 가능 ")

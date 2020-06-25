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

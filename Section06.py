#파이썬 함수식 및 람다

# 함수 정의 방법
#def 함수명(paramter):
# code

#함수 호출
# 함수명(parameter)

#예제1

#hello("Python!") 함수 정의보다 위에 있으면 안됨
#hello(7777)

def hello(world):
    print("HEllo", world)


hello("Python!")
hello(7777)

def hello_return(word):
    val = "HEllo" + str(word) #숫자는 스트링으로 형변환 해주지 않으면 에러
    return val

str = hello_return("Python!!!")
print(str)

#예제3(다중리턴)
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 200
    return y1, y2, y3


val1, val2, val3 = func_mul(100) #리턴되는 값의 숫자만큼 받아야 에러가 나지 않음
print(val1, val2)

def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 200
    return [y1, y2, y3]


ls = func_mul(100)
print(ls, type(ls))



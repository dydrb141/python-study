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

#예제4

def args_func(*args):
    for t in args:
        print(args)

def args_func2(*args):
    for i,v in enumerate(args): #index까지 가능
        print(i, v)

args_func("han")
args_func("han", "gabun")
args_func("han", "gabun", "lee")
args_func2("han", "gabun", "lee")


# 키워드 함수
#** 는 dictionary로 받음
#* 는 tuple로 받음
def kwargs_func(**args):
    for k, v in args.items():
        print(k, v)

kwargs_func(name1='han')


#전체  혼합
def ex_mul(arg1, args2, *args, **args3):
    print(arg1, args2, args, args3)

ex_mul(10, 20)
ex_mul(10, 20, 'park', 'kim', age=24, age2=34)

# 중첩함수(클로저)
def nested_func(num):
    def func_in_func(num):
        print('>>>', num)
    print("in func")
    func_in_func(num + 1000)

nested_func(10000)

#클로저 데코레이터 찾아보기


#힌트
def func_mul(x : int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 200
    return [y1, y2, y3]

print(func_mul(2.0)) #예외를 유발하지 않음


# 람다식 예저ㅔ
# 람다식 :메모리 절약, 가독성 향상, 코드간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(heap 초기화) -> 메모리 초기화


#일반적 함수 -> 변수 활당
def mul_10(num : int) -> int: #메모리를 할당
    return num * 10

var_funct = mul_10 #메모리를 할당
print(type(var_funct))
print(var_funct)


lambda_mul_10 = lambda num: num * 10

print('>>>', lambda_mul_10(10))

def func_final(x, y, func):
    print(x * y * func(10))

#func_final(10, 10, lambda_mul_10)
print(func_final(10,10 , lambda x: x * 1000))



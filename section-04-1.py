#데이터 타입

v_str1 = "Niceman"
v_bool = True
v_str2 = "GooodBoy"
v_float = 10.3
v_int = 7
v_dit = {
    "name": "Kim",
    "age": 25
}

v_tuple = 3, 5, 7
v_set = {7, 8, 9}
v_list = [3, 5, 7]

print(type(v_tuple))
print(type(v_set))
print(type(v_float))
print(type(v_int))
print(type(v_dit))

i1 = 39
i2 = 939
big_int1 = 9999999999999999999999999999999999999999999999999
big_int2 = 777777777777777777777777777777777777777777777777
f1 = 1.234
f2 = 3.789
f3 = .5
f4 = 10.

print(i1 * i2)
print(big_int1 * big_int2)
print(f1 ** f2)
print(f3 + i2) # 실수로 자동 형변환

result = f3 + i2
print(result, type(result))

print(4 / 2)
print(4 // 2)

a = 5.
b = 4
c = 10

print(type(a), type(b))

result2 = a + b
print(result2)

#형변환

print(int(result2))
print(float(c))

#복수수
print(complex(3))

print(int(True))
print(int(False))
print(int('3'))
print(complex(False))
#지수 구하기
print(2 ** 3)

y = 100
y *= 100
print(y)


# 수치 연산 함수
#https://docs.python.org/3/library/math.html

#절대값
print(abs(-7))

#나누기와 몫을 구해서 각각 변수에 담아줌
n, m = divmod(100 ,8)
print(n, m)

import math

#5.1보다 크면서 가장 가까운 정수
print(math.ceil(5.1))
#3.874보다 작으면서 가장 가까운 정수
print(math.floor(3.874))



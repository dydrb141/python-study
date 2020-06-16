#리스트 (순서o, 중복o, 수정o, 삭제o)
a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'pan', 'Banana', 'Orenge']
e = [10, 100, ['pan', 'Banana', 'Orenge']]

# 인덱싱
print(d[3])
print(d[-2])
print(d[0] + d[1])
print(e[2][1])
print(e[-1][-2])

# 슬라이싱
print(d[0:3])
print(e[2][1:3])

# 연산
print(c + d)
print(c * 3)
print(str(c[0]) + 'hi')

#리스트 수정 삭제
c[0] = 77
print(c)

c[1:2] = [100, 1000, 10000]
print(c)

c[1] = ['a', 'b', 'c']
print(c)

del c[1]
print(c)
del c[-1]
print(c)

#리스트 함수
y = [5, 2, 3, 1, 4]
print(y)

y.append(6)
print(y)

y.sort()
print(y)

y.reverse()
print(y)

y.insert(2, 7)
print(y)

y.remove(2)
print(y)

#del과  remove의 차이 del 은 index를 가지고 지우고 remove는 값을 찾아서 지움
# y.remove(111) 찾는값이 없으면 에러

y.pop()
print(y)

ex = [88, 77]
y.extend(ex)

print(y)

y.append(ex)

print(y)

#append와 extend의 차이 append는 리스트 자체가 들어가지면 extend는 리스트의 원소를 다른 리스트 끝에 추가함.

# 튜플 (순서o, 중복o, 수정x, 삭제x)

a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))
# del c[2]튜플은 삭제되지 않음

print(c[2])
print(c[3])
print(d[2][1])

print(d[2:])
print(d[2][0:2])


print(c + d)
print(c * 3)

#튜플 함수

z = (5, 2, 1, 3, 4)

print(z)
print(3 in z) #튜플 안에 3이 있는지 true false

print(z.index(4))




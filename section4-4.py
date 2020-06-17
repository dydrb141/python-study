#파이썬 데이터 타입
# 딕셔너리, 집합, 자료형

#딕셔너리 : 순서x 중복x 수정o 삭제o
#key, value (Json) 키는 중복되지 않음
#선언

a = {'name': 'Kim', 'Phone' : '010-777-777', 'birth': 870123}
b = {0: 'Hello Python', 1: 'Hello Coding'}
c = {'arr': [1, 2, 3, 4, 5]}

print(a['name']) #키가 없으며 에러
print(a.get('address')) #get을 사용하면 에러 발생하지 않고 None으로 출력
print(c['arr'][1:2])

# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1, 2, 3]
a['rank2'] = (1, 2, 3,)

print(a)

#keys, valus, items

print(a.keys()) #index에 접근은 안됨 list로 형변환 해야함
print(list(a.keys()))

temp = list(a.keys())
print(temp[1:3])

print(a.values())
print(list(a.values()))

print(list(a.items())) # list안에 튜플형식
print(2 in b)
print('name' in  a)
print('name2' not in a)





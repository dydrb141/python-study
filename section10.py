#파이썬 예외처리

#예외 종류
# 문법적으로 에러가 없지만 코드 실행(런타임)프로세스에서 발생하는 예외 처리 중요
#SyntaxError: 잘못된 문법 문법이 잘못된 경우

#NAmeError: 참조변수 없음

a = 10
b = 15

# print(c)

# ZeroDivisionError : 0 나누기 에러
# print(10 /0)

# indexError: 인덱스 범위 오버

x = [10, 20, 30]
#print(x[3])

# keyError
dic = {'name' : 'kim'}

#print (dic['hobby'])
print(dic.get('name')) #직접 접근하지 말고get을 통해서 접근하면 에러 발생하지 않음


# AttributeError: 모듈, 클래스에 있는 잘못된 송성 사용시 예외
import time
print(time.time())
#print(time.sadf())

# ValueError : 참조값이 없을때

x = [1,3,5]
#x.remove(10)
#x.index(10)

#FileNotFoundError
#f = open('test.xtst', 'r') #예외

# TypeError
x = [1,2]
y = (1,2)
z = 'test'

#print (x + y)
#print (x + z)
print(x + list(y))

#항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그후 런타임 예외 발생시 예외 처리 코딩 권장 (EAFP 코딩 스타일)


#예외 처리 기본
#try : 에러가 발생할 가능성이 있는 코드 실행
# exception : 에러명
# else : 에러가 발생하지 않았을 경우
# fynally : 항상 실행

#예제 1
name = ['Kim', 'Lee', 'Park']

try:
    z = 'Kim'
    x = name.index(z);
    print('{} Fond it in name'.format(z, x +1))
except ValueError:
    print('NOtFoundIt valueError')
else:
    print("Ok else")

try:
    z = 'dd'
    x = name.index(z);
    print('{} Fond it in name'.format(z, x +1))
except:
    print('NOtFoundIt valueError')
else:
    print("Ok else")



try:
    z = 'dd'
    x = name.index(z);
    print('{} Fond it in name'.format(z, x +1))
except:
    print('NOtFoundIt valueError')
else:
    print("Ok else")
finally:
    print("finallyyyyyyy")



#예제4

# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴
try:
    print('ttest')
finally:
    print("finally")


try:
    z = 'dd'
    x = name.index(z);
    print('{} Fond it in name'.format(z, x +1))
except ValueError:
    print('NOtFoundIt valueError')
except IndexError:
    print('NOtFoundIt valueError')
except Exception:
    print('NOtFoundIt valueError')
else:
    print("Ok else")


#예제 6
#예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = 'Kim'
    if a == 'Kim':
        print("오케이 허가")
    else:
        raise ValueError
except ValueError:
    print('NOtFoundIt valueError')
except Exception as f:
    print(f)
else:
    print("Ok else")




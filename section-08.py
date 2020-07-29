#파이썬 모듈과 패키지
#패키지 예제
#상대 경로
#..:부모 디렉토리
#. : 현재 디렉토리


from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)

print(Fibonacci.fib2(300))
print("ex:", Fibonacci().title)


# 사용 2(클래스
from  pkg.fibonacci import * #권장하지 않음 필요 없는 클래스도 모두 가져옴

#사용 3(클래스)
from pkg.fibonacci import Fibonacci as fb

fb.fib(300)

#사용 (함수)
import pkg.calculations as c

print("ex:", c.add(10, 100))
print("ex:", c.mul(10, 100))

#사용 (함수)

from pkg.calculations import div as d
print ("ex", d(100, 10))


# 사용6
import pkg.prints as p
p.prt1()
p.prt2()


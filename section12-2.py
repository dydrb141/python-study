# 파이썬 데이터베이스 연동
# 테이블 조회

import sqlite3

conn = sqlite3.connect('D:/project/python_basic/resource/database.db')

#커서 바인딩
c = conn.cursor();

c.execute("select * from users")

#커서 위치가 변경
#1개 로우 선택
#print("One -< \n", c.fetchone())


#지정 로우 선택
#print("Threee -< \n", c.fetchmany(size=3))

#전체 로우 선택
#print("All -< \n", c.fetchall())

# 순회1
#rows = c.fetchall()


#for row in rows:
  #  print('retrievel > ', row);

#for row in c.fetchall():
   # print('reterieve2 > ', row)

 #순회 3

#for row in c.execute("select * from users order by id desc"):
 #   print("rere > ", row)



param1 = (3,)
c.execute("select * from users where id=?", param1)

print('param1', c.fetchone())
print('param1', c.fetchall()) #데이터 없음 3번은 하나밖에 없기 때문에 커서가 없음


param2 = 4
c.execute('select * from users where id="%s"' % param2) # %s, %$f, %d

print('param1', c.fetchone())
print('param1', c.fetchall()) #데이터 없음 3번은 하나밖에 없기 때문에 커서가 없음


c.execute('select * from users where id=:Id', {"Id": 5})

print('param1', c.fetchone())
print('param1', c.fetchall()) #데이터 없음 3번은 하나밖에 없기 때문에 커서가 없음

param4 = (3,5)
c.execute('select * from users where id IN(?, ?)', param4)
print('param1', c.fetchall())


c.execute("select * from users where id IN('%d', '%d')" % (3,4))
print('param1', c.fetchall())

c.execute("select * from users where id=:id1 OR id=:id2" , {"id1": 2, "id2": 5})
print('param1', c.fetchall())

#Dump 출력
with conn:
    with open('D:/project/python_basic/resource/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dumpt print complete')









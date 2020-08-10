#파이썬 데이터베이스 연동
# 테이블 데이터 수정 및 삭제

import sqlite3
conn = sqlite3.connect('D:/project/python_basic/resource/database.db')
c = conn.cursor()

c.execute('update users set username = ? where id = ?', ('naceman', 2))

c.execute('update users set username = :name where id = :id', {"name" :'goodman', "id" : 2})

c.execute("update users set username = '%s' where id = '%s'" % ('badbody', 3))

for user in c.execute("select * from users"):
    print(user)



#row delete
c.execute("delete from users where id= ?", (2,))

c.execute("delete from users where id= :id", {"id" : 3})

c.execute("delete from users where id= %s" % 4)

for user in c.execute("select * from users"):
    print(user)


print("user db delte: ", conn.execute("delete from users").rowcount, "rowcount")

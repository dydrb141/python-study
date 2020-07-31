# 파이썬 데이터베이스 연동 (sqlLIte)
# 데이터 생성 및 삽입

import sqlite3
import datetime

#삽입 날짜 생성
now = datetime.datetime.now()
print ('now', now)

nowDateTime = now.strftime('%Y-%m-%d %H:%M:$s')
print ('nowdatetiem:', nowDateTime)

#sqllite3
print('sqllie.veriosn', sqlite3.version)
print('sqllie.sqite_version', sqlite3.sqlite_version)

#DB생성 & AUTO COMMIT( rollback)

conn = sqlite3.connect('D:/project/python_basic/resource/database.db', isolation_level=None)

# Cursor

c = conn.cursor()
print ('Cusor Type', type(c))

#테이블 생성(Data Type: TExt, NUMERIC INTEGER REAl BLOB)
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text"
          ", phone text, website text, regdate text )")

#데이터 삽입
c.execute("INSERT INTO users VALUES(1, 'kim', 'kim@naver.com', '0101-1111-1111', 'kim.com', ?)", (nowDateTime,))
c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?,?,?,?,?,?)", (2, 'kim', 'kim@naver.com', '0101-1111-1111', 'kim.com', nowDateTime))


#Mny 삽입 (튜플, 리스트)

userList = {
    (3, 'LEE', 'LEE@naver.com', '010-1111-1111-1111', 'kim.com', nowDateTime),
    (4, 'FEE', 'FEE@naver.com', '010-1111-1111-1111', 'FEE.com', nowDateTime),
    (5, 'CEE', 'CEE@naver.com', '010-1111-1111-1111', 'CEEcom', nowDateTime)
}

c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?,?,?,?,?,?)", userList)


#데이블 데이터 삭제
#conn.execut("DELETE FORM users")

#print('users db deleted: ', conn.execute("DELETE FROM users").rowcount)


#커밋 isolation_level = None 일 경우 자동 반영(으로 커밋)
#conn.commit

#롤백
# conn.rollback()

#접속 해제
conn.close()
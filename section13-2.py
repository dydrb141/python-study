# 타이핑 게임 제작 및 기본완성

import random
import time

# 사운드 출력 필요 모듈
import winsound
import sqlite3
import datetime

conn = sqlite3.connect('D:/project/python_basic/resource/database.db', isolation_level=None) #None으로 해줘야 오토커밋 됨
c = conn.cursor()

c.execute("create table if not exists records(id integer primary key autoincrement, cor_cnt integer, record text, regdate text)")



words = []  # 영어 단어 리스트 (1000개 로드)

n = 1  # 게임 시도 횟수
cor_cnt = 0  # 정답 개수

with open('./resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip())  # 양쪽 공백 제거

print(words)

a = input("Ready Press Enter key!")  # game Start

print(a)

start = time.time()

while n <= 5:
    random.shuffle(words)
    q = random.choice(words)

    print()

    print("Qeujstion # {}".format(n))
    print(q)  # 문제출력

    x = input()

    print()
    n += 1

    if str(q).strip() == str(x).strip():
        print("pass")
        winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)
        cor_cnt += 1
    else:
        print("wrong")
        winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)


end = time.time()
et = end - start
et = format(et, ".3f")

conn.execute("INSERT INTO records(cor_cnt, record, regdate) VALUES (?,?,?)", (cor_cnt, et, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
#c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?,?,?,?,?,?)", (2, 'kim', 'kim@naver.com', '0101-1111-1111', 'kim.com', nowDateTime))

if cor_cnt >= 3:
    print("합격")
else:
    print("불합격")

# 수행 시간 출력
print("게임 시간: ", et, "초", "정답 개수: {}".format(cor_cnt))

# 시작지점
if __name__ == '__main__': #메인일 경우에만 실행
    pass

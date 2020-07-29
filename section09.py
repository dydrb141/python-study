#파일 읽기, 쓰기
# 일기 모드: r, 쓰기ㅂ모드 (기존파일 삭제) :w , 추가모드 (파일 생성성 추가) : a

#파일 읽기
f = open('./resource/review.txt', 'r')
content = f.read();
print(content)
print(dir(f))
#반드시 close로 리소스 반환
f.close()
print('------------------------------')

#예제 2번
with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))
#with 를 씀녀 자동으로 리소스 반환
print('------------------------------')

#예제3
with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip()) #양쪽 공백 제거

#예제4
with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print(">", content)
    content = f.read() #내용 없음 커서가 이미 끝으로 가있음
    print(">", content)

#예제5
with open('./resource/review.txt', 'r') as f:
    line = f.readline()
    while line:
        print(line, end=' ####')
        line = f.readline()
#예제6
with open('./resource/review.txt', 'r') as f:
    contents = f.readlines()
    print(contents)

    for c in contents:
        print(c, end= '*****')


#예제7
score = []
with open('./resource/score.txt', 'r') as f:
    for line in f:
        score.append(int(line))
    print(score)

print('average : {:6.3}'.format(sum(score)/len(score)))


#파일 쓰기
#예제1
with open('./resource/text1.txt', 'w') as f:
    f.write('NiceMan')

with open('./resource/text1.txt', 'a') as f:
        f.write('GOoodMan\n')

from random import randint
with open('./resource/text2.txt', 'a') as f:
    for cnt in range(6):
        f.write(str(randint(1, 50)))
        f.write('\n')

#writeLines : list -> 파일로 저장
with open('./resource/text3.txt', 'w') as f:
    list = ['kim\n', 'park']
    f.writelines(list)

with open('./resource/text4.txt', 'w') as f:
    print('Test Contest1', file=f)
    print('Test Contest2', file=f)
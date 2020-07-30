#파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

#CSV: MIME -text/csv

#예제 1
import csv
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.reader(f)
    #next(reader) 헤더를 스킵할때

    #확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        print(c)


#예제 2
import csv
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')
    #next(reader) 헤더를 스킵할때

    #확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        print(c)

#예제 3 (Dict변환

with open('./resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f)

    for c in reader:
        for k, v in c.items():
            print(k, v)
        print('----------------')


# 예제4
w = [[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18]]

#with문에서 한번 줄바꿈 해주고 csv write에서 줄바꿈을 자동으로 해주기 때문에 엔터를 2번 친다
#newline: 이걸 통해 newLine을 없앨수 있다

with open('./resource/sample3.csv', 'w', newline='') as f:
    wt = csv.writer(f)

    for s in w:
        wt.writerow(s)

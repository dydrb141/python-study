#Section 05-2 반복문 실습

v1 = 1
while v1 < 11:
    print("v1 is : ", v1)
    v1 += 1

for v2 in range(10):
    print("v2 is : ", v2)


for v3 in range(1, 11):
    print("v3 is: ", v3)

# 1 ~ 100합

sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1;
    cnt1 += 1;

print("1 ~100: ", sum1)
print("1 ~ 100 :", sum(range(1, 101)))
print("1 ~ 100 :", sum(range(1, 101, 2)))



# Section 04-2
# 문자열, 문자열연산, 슬라이싱

str1 = "I am boy"
str2 = "NiceMan"
str3 = ''
str4 = str('')

print(len(str1), len(str2), len(str3), len(str4))

escape_str1 = "Do you have a \"big collection\""
print(escape_str1)

escape_str2 = "Tab\tTab\tTab"
print(escape_str2)

# Raw String
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)

raw_s2 = r"\\a\\a"
print(raw_s2)

# 멀티라인
multi = \
""" 
문자열 

멀티라인 

테스트 

"""
print(multi)

# 문자열 연산
str_o1 = '*'
str_o2 = 'abc'
str_o3 = "def"
str_04 = "Niceman"

print(str_o1 * 100)
print(str_o2 + str_o3)
#print(str_o1 + 3) 는 결합 불가 * 는 가능
print(str_o1 * 3)

#str_04에 a가 포함 되어있냐

print('a' in str_04)
print('f' in str_04)
print('z' not in str_04)
print('z' not in str_04)


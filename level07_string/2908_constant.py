# 백준 7단걔 7번 - 상수
# 숫자를 뒤집에서 비교하는 문제


# 숫자 2개 입력받기
_num1, _num2 = input().split()
num1 = ""
num2 = ""

# 숫자 뒤집기
for i in range(len(_num1)-1, -1, -1):
    num1 += _num1[i]
for i in range(len(_num2)-1, -1, -1):
    num2 += _num2[i]

# 큰 숫자 출력
if num1 > num2:
    print(num1)
else:
    print(num2)
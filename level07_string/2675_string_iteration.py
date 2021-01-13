# 백준 7단계 4번 - 문자열 반복
# 각 문자를 반복하여 출력하는 문제


# 입력받을 문자열 개수
count = int(input())

# 문자열 입력받아 반복해서 출력하기
for i in range(count):
    num, str = input().split()
    text = ""
    for i in str:
        text += int(num)*i
    print(text)
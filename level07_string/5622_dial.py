# 백준 7단계 8번 - 다이얼
# 규칙에 따라 문자에 대응하는 수를 출력하는 문제

# 문자열 입력
nums = input()
phone = []

# 숫자로 변환
for i in range(len(nums)):
    if (65 <= ord(nums[i])) and (ord(nums[i]) <=67):
        phone.append(2)
    elif (ord(nums[i]) <= 70):
        phone.append(3)
    elif (ord(nums[i]) <= 73):
        phone.append(4)
    elif (ord(nums[i]) <= 76):
        phone.append(5)
    elif (ord(nums[i]) <= 79):
        phone.append(6)
    elif (ord(nums[i]) <= 83):
        phone.append(7)
    elif (ord(nums[i]) <= 86):
        phone.append(8)
    elif (ord(nums[i]) <= 90):
        phone.append(9)

# 걸리는 시간 구하기
print(sum(phone) + len(phone))
# 백준 1차원 배열- 10818번: 최소, 최대

# 정수 입력받기
count=int(input())  # 정수의 개수
numbers=[]
for i in range(count):
    num=int(input())
    numbers.append(num)
print(numbers)

# 최소값, 최대값 찾기
min=numbers[0]
max=numbers[0]
for i in range(count):
    if(min>numbers[i]):
        min=numbers[i]
    if(max<numbers[i]):
        max=numbers[i]
print(min, max)

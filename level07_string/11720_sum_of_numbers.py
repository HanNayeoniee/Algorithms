# 백준 7단계 2번 - 숫자의 합
# N개의 숫자가 공백 없이 쓰여있을 때 숫자를 모두 합해서 출력하는 프로그램

count = int(input())
numbers = list(input())
total = 0

for i in range(count):
    total += int(numbers[i])
print(total)
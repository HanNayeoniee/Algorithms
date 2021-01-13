# 백준 12단계 2750번: 수 정렬하기
# 시간 복잡도가 O(n^2)인 정렬 알고리즘

def bubble_sort(data):
    for i in range(len(data)):
        for j in range(len(data)-1-i):  # 반복문을 한번 거칠 때마다 숫자를 하나씩 정렬해, 비교해야하는 숫자가 줄어들기 때문
            if(data[j] > data[j+1]):
                data[j], data[j+1] = data[j+1], data[j]

    return data

# 정렬할 숫자 입력받기
count = int(input())  # 정렬할 숫자의 개수
nums = []  # 정렬할 숫자
for i in range(count):
    num = int(input())
    nums.append(num)


res = bubble_sort(nums)
for i in range(len(res)):
    print(res[i])
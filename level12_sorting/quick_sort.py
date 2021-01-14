# 퀵 정렬/ quick sorted

# start는 시작원소, end는 끝나는 원소
def quick_sort(data, start, end):
    if (start >= end):  # 원소가 한개인 경우
        return

    key = start  # pivot값을 첫번째 값으로 선택
    i = start+1  # 왼쪽 출발 지점
    j = end  # 오른쪽 출발 지점

    while(i <= j):
        while(data[i] <= data[key] and i<=end):  # key값보다 큰값을 만날 때까지 오른쪽으로 이동
            i +=1
        while(data[j] >= data[key] and j>start):  # key값보다 작은 값을 만날 때까지 오른쪽으로 이동
            j -=1
        if(i > j):  # 엇갈린 상태면 키 값과 교체
            data[j], data[key] = data[key], data[j]
        else:
            data[i], data[j] = data[j], data[i]

    quick_sort(data, start, j-1)
    quick_sort(data, j+1, end)

data = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
quick_sort(data, 0, len(data)-1)
print(data)


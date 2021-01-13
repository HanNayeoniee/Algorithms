# 선택 정렬(selection sort)

def selection_sort(data):
    for i in range(len(data)):
        min = 9999  # 모든 원소보다 큰 숫자로 넣기
        for j in range(i, len(data), +1):
            if (min > data[j]):
                min = data[j]
                index = j
        data[i], data[index] = data[index], data[i]
    return data

data = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
res = selection_sort(data)
print(res)
# 삽입 정렬/insertion sort

data = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

for i in range(len(data)-1):  # 첫번째 요소는 정렬되어 있다고 가정
    j = i
    while(data[j] > data[j+1]) :
        data[j] , data[j+1] = data[j+1], data[j]
        j = -1  # j보다 인덱스가 작은 요소들은 이미 정렬되어 있음
    print(data)
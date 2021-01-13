# 버블 정렬(bubble sort)
# 인접한 두개의 데이터를 비교해, 앞의 데이터가 뒤에 있는 데이터보다 크면, 자리를 바꾸는 정렬 알고리즘

data = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
n = len(data)

for i in range(len(data)):
    for j in range(len(data)-1-i):  # 반복문을 한번 거칠 때마다 숫자를 하나씩 정렬해, 비교해야하는 숫자가 줄어들기 때문
        if(data[j] > data[j+1]):  
            data[j], data[j+1] = data[j+1], data[j]
    print(i, data)
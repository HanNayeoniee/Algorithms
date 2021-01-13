# 백준 1차원 배열- 2577번: 숫자의 개수

# 3개의 자연수 입력받기
a = int(input())
b = int(input())
c = int(input())
num_input=a*b*c
num_str=str(num_input)

# count는 숫자별로 개수가 몇개인지 담겨있음
count=[0,0,0,0,0,0,0,0,0,0]
num=0
for i in range(len(num_str)):
    for num in range(0, 10, 1):
        if(num_str[i]==str(num)):
            count[num]+=1
# 결과 출력
for i in range(len(count)):
    print(count[i])

# 백준 1차원 배열- 3052번: 나머지

# 입력 10개 받기
num_list = list(int(input()) for i in range(10))

# 42로 나눈 나머지 계산
for i in range(len(num_list)):
    num_list[i]=num_list[i]%42

# 방법1: 하나씩 비교한 후 서로 다른 값 넣기
# whatsin 리스트 안에 있는지 검사 후 없으면 append
whatsin=[]
for i in range(len(num_list)):
    if num_list[i] in whatsin:
        continue
    else:
        whatsin.append(num_list[i])
print(len(whatsin))

# 방법2: set 사용하기
num_list = set(num_list)
print(len(num_list))

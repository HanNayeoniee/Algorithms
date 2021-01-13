# 백준 1차원 배열- 8958번: OX퀴즈 점수 구하기

# 테스트 케이스 개수 입력
n=int(input())
case=[]
for i in range(n):
    case.append(input())
res=[]  # 테스트 케이스마다 점수를 담을 리스트


# 테스트 케이스 개수만큼 반복: c는 0~4
for c in range(n):
    score=[0] * len(case[c])
    # 각각 케이스 길이만큼 반복: i는 0~각각 길이
    for i in range(len(case[c])):
        # 첫번째 요소일 때
        if(i==0):
            if(case[c][i]=='O'):
                score[i]=1
            elif(case[c][i]=='X'):
                score[i]=0
        else:
            # 0이 연속되는 경우
            if(score[i-1]>0 and case[c][i]=='O'):
                score[i]=score[i-1]+1
            # 0이 연속되지 않는 경우
            elif(case[c][i]=='O'):
                score[i]=1
            # X인 경우
            else:
                score[i]=0
    total=sum(score)
    res.append(total)

# print(res)
for r in range(n):
    print(res[r])

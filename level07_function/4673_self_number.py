# 백준 함수- 4673번: 셀프 넘버

def d(n):
    res=n
    for i in list(str(n)):
        res+=int(i)
    return res

# 셀프넘버가 아닌 숫자 구하기
not_self_number=[]
for i in range(1, 10001):
    res=d(i)
    not_self_number.append(res)

# 셀프넘버 구하기
# 전체에서 셀프넘버가 아닌 숫자를 제외
for i in range(1, 10001):
    if i in not_self_number:
        pass
    else:
        print(i)

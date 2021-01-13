# 백준 7단계 10번 - 그룹 단어 체커
# 조건에 맞는 문자열을 찾는 문제
# sorted에서 key=word.find로 설정하면 "a"부터 정렬되지 않고, word에서 찾아지는 character순서대로 정렬됨

cnt = 0  # 그룹단어 개수

for i in range(int(input())):
    word = input()
    cnt += list(word)==sorted(word, key=word.find)
print(cnt)
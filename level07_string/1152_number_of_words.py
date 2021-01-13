# 백준 7단계 6번 - 단어의 개수
# 단어의 개수를 구하는 문제


# 버전1 - 코드 여러줄
sentence = input()
word = sentence.split()
# print(word)
print(len(word))

# 버전2 - 코드 한 줄
print(len(input().split()))
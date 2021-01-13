# 백준 7단계 5번 - 단어 공부
# 주어진 단어에서 가장 많이 사용된 알파벳을 출력하는 문제

# 단어 입력받기
word = input()
word = word.lower()
word_set = set(word)
alphabet = [0]*26

# 알파벳 개수 세기
for i in range(len(word)):
    char = word[i]
    if char in word_set:
        alphabet[ord(char)-97] += 1

# 가장 많이 사용된 알파벳이 여러개인 경우
# 정렬 후 빈도수가 같으면 ?출력
alphabet_sort = sorted(alphabet)
if (alphabet_sort[25]==alphabet_sort[24]):
    print("?")

# 가장 많이 사용된 알파벳이 1개인 경우
# 빈도수가 가장 많은 알파벳을 찾아
# 인덱스의 chr(아스키코드->알파벳으로 변환) 출력
# 입력에 상관없이 출력이 대문자로 나와야 해서 65를 더함
# 알파벳 소문자를 출력하려면 +97
else:
    max = alphabet[0]
    for i in range(len(alphabet)):
        if (max < alphabet[i]):
            max = alphabet[i]
    print(chr(alphabet.index(max)+65))
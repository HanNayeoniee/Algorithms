# 백준 7단계 3번 - 알파벳 찾기
# 한 단어에서 각 알파벳이 처음 등장하는 위치를 찾는 문제

# alphabet 리스트는 알파벳 26개의 시작 위치를 담아야 하니까 크기는 26
# 알파벳 "a"의 index가 0이 되어야 하므로 알파벳의 index는 'ord(알파벳)-97' 로 계산함


word_list = list(input())  # 입력받을 단어
word_set = set(word_list)  # 입력 단어의 알파벳 집합
alphabet = [-1] * 26  # 알파벳의 위치를 담을 리스트, -1로 초기화

for i in range(len(word_list)):
    char = word_list[i]
    if alphabet[ord(char) - 97] == -1:
        if (char in word_set):
            alphabet[ord(char) - 97] = i

for i in range(len(alphabet)):
    print(alphabet[i], end=' ')
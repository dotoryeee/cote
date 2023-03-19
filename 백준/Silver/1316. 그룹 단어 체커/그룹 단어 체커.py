import sys

count = int(sys.stdin.readline().rstrip())
words = []
for i in range(count):
    words.append(sys.stdin.readline().rstrip())

def check(word):
    word_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    word_list[ord(word[0])-97] = 1
    for num, char in enumerate(word[1:]):
        cursor = ord(char)-97
        #print(f'{word[num]} / {char}')
        if char == word[num]: #바로 앞 단어랑 알파벳 같으면 스킵
            pass
        else:
            if word_list[cursor] == 1: #알파벳이 나온 적 있으면 False
                #print(f'{word} is False')
                return False
            word_list[cursor] = 1 #중복 확인을 위해 알파벳 나왔던 것을 체크
    #print(f'{word} is True')
    return True

sum = 0
for word in words:
    if check(word):
        sum += 1

print(sum)
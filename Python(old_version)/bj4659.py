# 비밀번호 발음하기

import sys
input = sys.stdin.readline

vowels = {'a', 'e', 'i', 'o', 'u'}
def check_password(string):
    vowel_count = 0
    consonant_count = 0
    exist_vowel = False
    prev = ''
    for i in range(len(string)):
        if i != 0:
            prev = string[i-1]
        now = string[i]

        if prev and prev == now:
            if prev == "e" or prev == "o":
                continue
            else:
                return False

        if now in vowels:
            consonant_count = 0
            vowel_count += 1
            exist_vowel = True
        else:
            vowel_count = 0
            consonant_count += 1
        
        if vowel_count == 3 or consonant_count == 3:
            return False

    if not exist_vowel:
        return False
    return True

password = input().strip()

while password != "end":

    result = check_password(password)

    if result:
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')


    password = input().strip()
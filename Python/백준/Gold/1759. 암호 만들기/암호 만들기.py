import sys
input = sys.stdin.readline

L, C = map(int, input().split())
letters = list(input().split())
letters.sort()
password = []
vowels = {'a', 'e', 'i', 'o', 'u'}

def available_passwords(x):
    if len(password) == L:
        vowel_cnt = 0
        consonant_cnt = 0

        for char in password:
            if char in vowels:
                vowel_cnt += 1
            else:
                consonant_cnt += 1

        if (
            vowel_cnt >= 1
            and consonant_cnt >= 2
        ):
            print(''.join(password))
        
        return
            
    for i in range(x, C):
        password.append(letters[i])
        available_passwords(i + 1)
        password.pop()
    

available_passwords(0)
        

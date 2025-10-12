# 팬그램

# print(ord("A"))
# 65
# print(ord("Z"))
# 90
# print(ord("a"))
# 97
# print(ord("z"))
# 122
# print(ord("1"))
# 49
# print(ord(" "))
# 32

import sys
input = sys.stdin.readline

def check_pangram(arr):
    minimum = min(num for num in arr)

    if minimum == 0:
        return("Not a pangram")
    elif minimum == 1:
        return("Pangram!")
    elif minimum == 2:
        return("Double pangram!!")
    else:
        return("Triple pangram!!!")

N = int(input())

for tc in range(1, N+1):
    sentence = input()
    arr = [0] * 26
    for i in range(len(sentence)):
        num = ord(sentence[i])
        if 65 <= num <= 90:
            arr[num-65] += 1
        elif 97 <= num <= 122:
            arr[num-97] += 1
        else:
            continue
    
    result = check_pangram(arr)

    print(f'Case {tc}: {result}')
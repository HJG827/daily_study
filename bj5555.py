# 반지
import sys
input = sys.stdin.readline

string = input().strip()

N = int(input())
ans = 0

def check_letter(string, sentence):
    result = 0
    for i in range(20-len(string)):
        for j in range(len(string)):
            if string[j] != sentence[i+j]:
               result = 0
               break
            result = 1
        if result == 1:
            break
    if result:
        return 1
    else:
        return 0

for i in range(N):
    sentence = input().strip()
    ring = sentence * 2
    if check_letter(string, ring):
        ans += 1

print(ans)
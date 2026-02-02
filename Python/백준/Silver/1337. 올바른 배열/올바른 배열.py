import sys
input = sys.stdin.readline

N = int(input())
numbers = [int(input()) for _ in range(N)]
numbers.sort()

best = 0
j = 0

for i in range(N):
    while j < N and numbers[j] <= numbers[i] + 4:
        j += 1

    cnt = j - i
    if cnt > best:
        best = cnt
    
print(5 - best)
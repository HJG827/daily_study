# 라디오
import sys
input = sys.stdin.readline

A, B = list(map(int, input().split()))
ans = abs(A-B)

N = int(input())

for i in range(N):
    signal = int(input())
    move = abs(B - signal) + 1
    if move < ans:
        ans = move
    
print(ans)
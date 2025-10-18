# 로프

import sys
input = sys.stdin.readline

N = int(input())
ropes = [int(input()) for _ in range(N)]

ropes.sort(reverse=True)

results = []

for i in range(1, N+1):
    results.append(ropes[i-1] * i)

print(max(results))
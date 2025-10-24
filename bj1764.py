# 듣보잡
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
heard = {}
both = []
for _ in range(N):
    heard[input().strip()] = 1

for _ in range(M):
    name = input().strip()
    if heard.get(name):
        both.append(name)

both.sort()
print(len(both))
for i in range(len(both)):
    print(both[i])
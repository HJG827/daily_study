# 나는야 포켓몬 마스터 이다솜

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
name_dict = {}
num_dict = {}

for i in range(1, N+1):
    name = input().strip()
    name_dict[name] = i
    num_dict[i] = name

for j in range(M):
    index = input().strip()
    if index.isdigit():
        print(num_dict[int(index)])
    else:
        print(name_dict[index])
# 수 정렬하기 2

import sys
input = sys.stdin.readline

# arr = [0] * 2000001
# N = int(input())
# cnt = 0

# for _ in range(N):
#     num = int(input()) + 1000000
#     arr[num] += 1

# for i in range(2000001):
#     if arr[i]:
#         for _ in range(arr[i]):
#             print(i-1000000)
#         cnt += arr[i]
#         arr[i] = 0
#     if cnt == N:
#         quit


N = int(input())
arr = []

for _ in range(N):
    num = int(input())
    arr.append(num)

arr.sort()

for i in range(N):
    print(arr[i])
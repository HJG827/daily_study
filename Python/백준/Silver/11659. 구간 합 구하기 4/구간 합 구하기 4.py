import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
sums = [0] * N
sums[0] = numbers[0]

for i in range(1, N):
    sums[i] = sums[i-1] + numbers[i]

for _ in range(M):
    start, end = map(int, input().split())
    if start == 1:
        print(sums[end - 1])
    else:
        print(sums[end - 1] - sums[start - 2])
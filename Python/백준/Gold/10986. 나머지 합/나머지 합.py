import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

sums = [0] * N
sums[0] = numbers[0] % M

ans = 0

for i in range(1, N):
    sums[i] = (numbers[i] + sums[i-1]) % M

sum_dict = {}

for idx in range(N):
    if sum_dict.get(sums[idx]):
        sum_dict[sums[idx]] += 1
    else:
        sum_dict[sums[idx]] = 1

for key, value in sum_dict.items():
    if value > 1:
        ans += (value * (value - 1) // 2)
    if key == 0:
        ans += value

print(ans)
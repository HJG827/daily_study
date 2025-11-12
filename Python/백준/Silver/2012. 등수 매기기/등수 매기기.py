import sys
input = sys.stdin.readline

N = int(input())

hopes = [int(input()) for _ in range(N)]
hopes.sort()

result = 0

for i in range(1, N+1):
    result += abs(hopes[i-1] - i)

print(result)
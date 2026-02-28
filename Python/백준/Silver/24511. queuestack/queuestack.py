from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

result = []
q = deque()

for i in range(N):
    if A[i] == 0:
        q.append(B[i])

for j in range(M):
    x = C[j]

    if q:
        q.appendleft(x)
        pop = q.pop()
    else:
        pop = x

    result.append(pop)

print(*result)

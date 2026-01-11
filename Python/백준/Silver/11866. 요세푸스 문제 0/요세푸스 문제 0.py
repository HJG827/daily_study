from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
q = deque(range(1, N + 1))
ans = []

while q:
    q.rotate(-(K - 1))
    ans.append(q.popleft())

print("<"+", ".join(map(str, ans))+">")
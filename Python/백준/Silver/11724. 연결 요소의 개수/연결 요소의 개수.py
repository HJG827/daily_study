import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (N+1)
ans = 0

for i in range(1, N+1):
    if not visited[i]:
        ans += 1
        q = deque([i])
        visited[i] = 1

        while q:
            node = q.popleft()
            for next_node in graph[node]:
                if not visited[next_node]:
                    visited[next_node] = 1
                    q.append(next_node)

print(ans)
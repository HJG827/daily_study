import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]

mark = 0
visited = [[0] * M for _ in range(N)]
dist = [[0] * M for _ in range(N)]
ans = 0

dir_r = [1, 0, -1, 0]
dir_c = [0, 1, 0, -1]

lands = []
for r in range(N):
    row = arr[r]
    for c in range(M):
        if row[c] == 'L':
            lands.append((r, c))

def bfs(sr, sc):
    global mark
    mark += 1
    q = deque()
    q_append = q.append
    q_popleft = q.popleft

    visited[sr][sc] = mark
    dist[sr][sc] = 0
    q_append((sr, sc))
    best = 0

    while q:
        r, c = q_popleft()
        d = dist[r][c]

        if d > best:
            best = d

        for k in range(4):
            nr = r + dir_r[k]
            nc = c + dir_c[k]
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == 'L' and visited[nr][nc] != mark:
                    visited[nr][nc] = mark
                    dist[nr][nc] = d + 1
                    q_append((nr, nc))

    return best

ans = 0
for r, c in lands:
    val = bfs(r, c)
    if val > ans:
        ans = val

print(ans)
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

INF = 10**9
visited = [[[INF] * 3 for _ in range(M)] for _ in range(N)]
space = [list(map(int, input().split())) for _ in range(N)]
dirs = [-1, 0, 1]

q = deque()

for c in range(M):
    for dir in range(3):
        visited[0][c][dir] = space[0][c]
        q.append([0, c, dir])

while q:
    tr, tc, td = q.popleft()
    nr = tr + 1

    if nr >= N:
        continue

    for nd in range(3):
        if nd == td:
            continue

        nc = tc + dirs[nd]
        if 0 <= nc < M:
            next_fuel = visited[tr][tc][td] + space[nr][nc]
            if next_fuel < visited[nr][nc][nd]:
                visited[nr][nc][nd] = next_fuel
                q.append([nr, nc, nd])

ans = INF
for fuels in visited[N-1]: 
    ans = min(ans, min(fuels))
print(ans)
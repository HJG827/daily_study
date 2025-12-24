from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
town = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

dir_r = [1, 0, -1, 0]
dir_c = [0, 1, 0, -1]

def bfs(sr, sc):
    q = deque()
    q.append([sr, sc])
    visited[sr][sc] = 1

    house = 1

    while q:
        tr, tc = q.popleft()
        for dr, dc in zip(dir_r, dir_c):
            nr = tr + dr
            nc = tc + dc
            if (
                0 <= nr < N
                and 0 <= nc < N
                and town[nr][nc] == 1
                and not visited[nr][nc]
            ):
                visited[nr][nc] = 1
                q.append([nr, nc])
                house += 1

    return house

houses = []

for r in range(N):
    for c in range(N):
        if town[r][c] and not visited[r][c]:
            houses.append(bfs(r, c))

print(len(houses))

houses.sort()
for house in houses:
    print(house)

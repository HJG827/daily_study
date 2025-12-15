from collections import deque
import sys
input = sys.stdin.readline

dir_r = [1, 0, -1, 0]
dir_c = [0, 1, 0, -1]

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

def find_start(arr):
    for r in range(n):
        for c in range(m):
            if arr[r][c] == 2:
                return r, c

sr, sc = find_start(arr) 
visited[sr][sc] = 0
q = deque()
q.append([sr, sc])

while q:
    tr, tc = q.popleft()
    for dr, dc in zip(dir_r, dir_c):
        nr = tr + dr
        nc = tc + dc

        if (
            0 <= nr < n
            and 0 <= nc < m
            and visited[nr][nc] == -1
        ):
            if arr[nr][nc] == 1:
                visited[nr][nc] = visited[tr][tc] + 1
                q.append([nr, nc])

for r in range(n):
    line = []
    for c in range(m):
        if arr[r][c] == 0:
            line.append("0")
        else:
            line.append(str(visited[r][c]))

    print(" ".join(line))
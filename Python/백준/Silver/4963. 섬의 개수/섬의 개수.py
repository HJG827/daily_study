import sys
input = sys.stdin.readline
from collections import deque

dir_r = [1, 1, 1, 0, 0, 0, -1, -1, -1]
dir_c = [1, 0, -1, 1, 0, -1, 1, 0, -1]

def bfs(arr, r, c):
    q = deque()
    q.append([r, c])

    while q:
        tr, tc = q.popleft()
        for dr, dc in zip(dir_r, dir_c):
            nr = tr + dr
            nc = tc + dc
            if (
                0 <= nr < h
                and 0 <= nc < w
                and arr[nr][nc] == 1
            ):
                arr[nr][nc] = 2
                q.append([nr, nc])

w, h = map(int, input().split())

while w != 0 and h != 0:
    arr = [list(map(int, input().split())) for _ in range(h)]
    ans = 0

    for r in range(h):
        for c in range(w):
            if arr[r][c] == 1:
                bfs(arr, r, c)
                ans += 1
    
    print(ans)
    w, h = map(int, input().split())
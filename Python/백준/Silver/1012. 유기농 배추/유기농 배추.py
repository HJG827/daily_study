import sys
input = sys.stdin.readline
from collections import deque

def bfs(arr, sr, sc):
    q = deque()
    q.append([sr, sc])

    while q:
        tr, tc = q.popleft()
        for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nr = tr + dr
            nc = tc + dc
            if (
                0 <= nr < N
                and 0 <= nc < M
                and arr[nr][nc] == 1
            ):
                arr[nr][nc] = 2
                q.append([nr, nc])


T = int(input())

for tc in range(1, T + 1):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]

    for _ in range(K):
        c, r = map(int, input().split())
        field[r][c] = 1

    ans = 0

    for r in range(N):
        for c in range(M):
            if field[r][c] == 1:
                bfs(field, r, c)
                ans += 1

    print(ans)
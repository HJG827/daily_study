import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
INF = 10 ** 9
t = 1

def bfs(N, sr, sc, arr):
    check = [[INF] * N for _ in range(N)]
    check[sr][sc] = arr[sr][sc]

    q = deque()
    q.append([sr, sc])

    while q:
        tr, tc = q.popleft()
        for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nr = tr + dr
            nc = tc + dc

            if (
                0 <= nr < N
                and 0 <= nc < N
            ):
                next_rufee = check[tr][tc] + arr[nr][nc]
                if next_rufee < check[nr][nc]:
                    check[nr][nc] = next_rufee
                    q.append([nr, nc])

    return check[N-1][N-1]

while N != 0:
    cave = [list(map(int, input().split())) for _ in range(N)]
    ans = bfs(N, 0, 0, cave)
    print(f'Problem {t}: {ans}')

    N = int(input())
    t += 1
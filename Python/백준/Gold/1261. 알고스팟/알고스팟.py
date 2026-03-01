from collections import deque
import sys
input = sys.stdin.readline

dir_r = [1, 0, -1, 0]
dir_c = [0, 1, 0, -1]

INF = 10 ** 15

M, N = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
dist = [[INF] * M for _ in range(N)]
dist[0][0] = 0

q = deque()
q.append((0, 0))

while q:
    r, c = q.popleft()

    for d in range(4):
        nr = r + dir_r[d]
        nc = c + dir_c[d]

        if (
            0 <= nr < N
            and 0 <= nc < M
        ):
            
            dd = arr[nr][nc]
            nd = dist[r][c] + dd

            if nd < dist[nr][nc]:
                dist[nr][nc] = nd
                if dd == 0:
                    q.appendleft((nr, nc))
                elif dd == 1:
                    q.append((nr, nc))

print(dist[N-1][M-1])
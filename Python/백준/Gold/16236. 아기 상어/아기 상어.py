import sys
input = sys.stdin.readline
from collections import deque

dir_r = [1, 0, -1, 0]
dir_c = [0, 1, 0, -1]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def find_shark():
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 9:
                arr[r][c] = 0
                return (r, c, 2)

r, c, now_size = find_shark()

def find_fish(r, c, size):
    q = deque()
    q.append((r, c))
    visited = [[-1] * N for _ in range(N)]
    visited[r][c] = 0
    fish = []

    while q:
        tr, tc = q.popleft()

        for d in range(4):
            nr = tr + dir_r[d]
            nc = tc + dir_c[d]

            if (
                0 <= nr < N
                and 0 <= nc < N
                and arr[nr][nc] <= size
                and visited[nr][nc] == -1
            ):
                visited[nr][nc] = visited[tr][tc] + 1
                q.append((nr, nc))

                if 0 < arr[nr][nc] < size:
                    fish.append((visited[nr][nc], nr, nc))


    fish.sort(key=lambda x : (x[0], x[1], x[2]))
    if fish:
        return fish[0]
    else:
        return

total_time = 0
now_fish = 0

while True:
    fish = find_fish(r, c, now_size)
    if fish:
        time, fr, fc = fish
        total_time += time
        now_fish += 1
        arr[fr][fc] = 0

        if now_fish >= now_size:
            now_size += 1
            now_fish = 0

        r = fr
        c = fc

    else:
        break

print(total_time)

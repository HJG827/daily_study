import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = -1
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

visited = [[False] * M for _ in range(N)]

def dfs(r, c, size, val):
    global ans, visited
    if size == 4:
        ans = max(ans, val)
        return
    
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if (
            0 <= nr < N
            and 0 <= nc < M
            and not visited[nr][nc]
        ):
            visited[nr][nc] = True
            dfs(nr, nc, size + 1, val + arr[nr][nc])
            visited[nr][nc] = False
    

# T자 형태 예외 직접 처리
def check_t(r, c):
    global ans

    center = arr[r][c]
    sides = []

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if (
            0 <= nr < N
            and 0 <= nc < M
        ):
            sides.append(arr[nr][nc])

    if len(sides) < 3:
        return
    
    elif len(sides) == 3:
        ans = max(ans, center + sum(sides))

    else:
        ans = max(ans, center + sum(sides) - min(sides))



for r in range(N):
    for c in range(M):
        visited[r][c] = True
        dfs(r, c, 1, arr[r][c])
        visited[r][c] = False

        check_t(r, c)

print(ans)
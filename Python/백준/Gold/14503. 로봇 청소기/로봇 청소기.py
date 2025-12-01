import sys
input = sys.stdin.readline

N, M = map(int, input().split())
sr, sc, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dir_r = [-1, 0, 1, 0]
dir_c = [0, 1, 0, -1]

def check_four(r, c):
    for i in range(4):
        if arr[r + dir_r[i]][c + dir_c[i]] == 0:
            return i
    return -1

ans = 0
operate = True
tr, tc = sr, sc

while operate:
    if arr[tr][tc] == 0:
        ans += 1
        # 청소된 칸을 2라고 표시
        arr[tr][tc] = 2
    
    check = check_four(tr, tc)
    if check == -1:
        nr = tr + dir_r[(d + 2) % 4]
        nc = tc + dir_c[(d + 2) % 4]
        if (
            0 <= nr < N
            and 0 <= nc < M
            and arr[nr][nc] != 1
        ):
            tr, tc = nr, nc
        else:
            operate = False
            break
    else:
        clean = True
        nd = (d + 3) % 4
        while clean:
            nr = tr + dir_r[nd]
            nc = tc + dir_c[nd]
            if (
                0 <= nr < N
                and 0 <= nc < M
                and arr[nr][nc] == 0
                ):
                tr, tc = nr, nc
                d = nd
                clean = False
            else:
                nd = (nd + 3) % 4

print(ans)
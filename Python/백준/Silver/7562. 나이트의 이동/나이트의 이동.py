from collections import deque
import sys
input = sys.stdin.readline

dir_r = [-2,-2,-1,-1, 1, 1, 2, 2]
dir_c = [-1, 1,-2, 2,-2, 2,-1, 1]

def bfs(sr, sc):
    if sr == knight_move[0] and sc == knight_move[1]:
        return 0
    
    dist = [[-1]*I for _ in range(I)]
    dist[sr][sc] = 0
    q = deque()
    q.append([sr, sc])

    while q:
        r, c = q.popleft()
        for dr, dc in zip(dir_r, dir_c):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < I and 0 <= nc < I and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                if nr == knight_move[0] and nc == knight_move[1]:
                    return dist[nr][nc]
                q.append([nr, nc])
    
    return dist[knight_move[0]][knight_move[1]]

T = int(input())

for tc in range(T):
    I = int(input())
    knight_now = list(map(int, input().split()))
    knight_move = list(map(int, input().split()))
    
    print(bfs(knight_now[0], knight_now[1]))
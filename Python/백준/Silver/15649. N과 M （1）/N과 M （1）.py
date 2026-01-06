import sys
input = sys.stdin.readline

N, M = map(int, input().split())

path = []
visited = [0] * (N + 1)

def backtrack():
    if len(path) == M:
        print(*path)
        return
    
    for i in range(1, N + 1):
        if not visited[i]:
            path.append(i)
            visited[i] = 1
            backtrack()
            visited[i] = 0
            path.pop()

backtrack()
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

visited = [0] * (N + 1)
path = []

def backtrack():
    if len(path) == M:
        print(*path)
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            path.append(numbers[i])
            backtrack()
            path.pop()
            visited[i] = 0

backtrack()
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
path = []

def backtrack(start):
    if len(path) == M:
        print(*path)
        return
    
    for i in range(start, N + 1):
        path.append(i)
        backtrack(i)
        path.pop()

backtrack(1)
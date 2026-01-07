import sys
input = sys.stdin.readline

N, M = map(int, input().split())
path = []

def backtrack(start):
    if len(path)== M:
        print(*path)
        return

    for x in range(start, N + 1):
        path.append(x)
        backtrack(x + 1)
        path.pop()

backtrack(1)
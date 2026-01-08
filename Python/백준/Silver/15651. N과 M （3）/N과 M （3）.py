import sys
input = sys.stdin.readline

N, M = map(int, input().split())
path = []

def backtrack():
    if len(path)== M:
        print(*path)
        return

    for x in range(1, N + 1):
        path.append(x)
        backtrack()
        path.pop()

backtrack()
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

path = []

def backtrack():
    if len(path) == M:
        print(*path)
        return
    
    for i in range(N):
        path.append(numbers[i])
        backtrack()
        path.pop()

backtrack()
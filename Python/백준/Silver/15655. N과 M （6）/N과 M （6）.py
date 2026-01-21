import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

path = []

def backtrack(start):
    if len(path) == M:
        print(*path)
        return
    
    for i in range(start, N):
        path.append(numbers[i])
        backtrack(i + 1)
        path.pop()

backtrack(0)
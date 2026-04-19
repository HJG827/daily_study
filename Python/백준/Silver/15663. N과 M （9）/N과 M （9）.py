import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

path = []
visited = [0] * (N)

def search():
    if len(path) == M:
        print(*path)
        return
    
    prev = -1

    for i in range(N):
        if not visited[i] and prev != numbers[i]:
            visited[i] = 1
            path.append(numbers[i])
            prev = numbers[i]

            search()

            visited[i] = 0
            path.pop()

search()
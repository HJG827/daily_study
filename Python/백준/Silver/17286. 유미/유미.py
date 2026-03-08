import sys, math
input = sys.stdin.readline

cat = list(map(int, input().split()))
people = list(list(map(int, input().split())) for _ in range(3))

ans = 10 ** 15

def get_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

order = []
visited = [0] * 3

def dfs():
    global ans

    if len(order) == 3:
        dist = 0
        now = cat

        for ord in order:
            dist += get_distance(people[ord], now)
            now = people[ord]

        ans = min(ans, dist)
        return
    
    for i in range(3):
        if visited[i]:
            continue

        visited[i] = 1
        order.append(i)
        
        dfs()

        order.pop()
        visited[i] = 0

dfs()
print(int(ans))
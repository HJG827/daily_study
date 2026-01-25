import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

invite = []

for i in range(len(graph[1])):
    invite.append(graph[1][i])
    invite += graph[graph[1][i]]

if 1 in set(invite):
    print(len(set(invite)) - 1)
else:
    print(len(set(invite)))
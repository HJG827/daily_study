import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

def bfs(A, B):
    prev = [-1] * 10000
    path = [''] * 10000

    q = deque()
    q.append(A)
    prev[A] = A

    while q:
        num = q.popleft()

        if num == B:
            break
        
        d = (num * 2) % 10000
        if prev[d] == -1:
            prev[d] = num
            path[d] = 'D'
            q.append(d)

        s = 9999 if num == 0 else num - 1
        if prev[s] == -1:
            prev[s] = num
            path[s] = 'S'
            q.append(s)

        l = (num % 1000) * 10 + num // 1000
        if prev[l] == -1:
            prev[l] = num
            path[l] = 'L'
            q.append(l)

        r = (num % 10) * 1000 + num // 10
        if prev[r] == -1:
            prev[r] = num
            path[r] = 'R'
            q.append(r)


    result = []
    now = B
    while now != A:
        result.append(path[now])
        now = prev[now]

    return ''.join(reversed(result))


for _ in range(T):
    A, B = map(int, input().split())

    print(bfs(A, B))


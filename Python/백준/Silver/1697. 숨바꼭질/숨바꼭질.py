from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

if N >= K:
    print(N - K)

else:
    MAX = 100001
    dist = [MAX] * MAX
    q = deque()
    q.append(N)
    dist[N] = 0
    while q:
        now = q.popleft()
        
        for next in (now + 1, now - 1, now * 2):
            if (0 <= next < 100001
                and dist[next] >= dist[now] + 1):
                dist[next] = dist[now] + 1
                q.append(next)

    print(dist[K])
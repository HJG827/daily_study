import heapq
import sys
input = sys.stdin.readline

n = int(input())
present = []

for _ in range(n):
    a, *gift = map(int, input().split())
    if a == 0:
        if present:
            print(-heapq.heappop(present))
        else:
            print(-1)
    else:
        for a in gift:
            heapq.heappush(present, -a)
import sys, heapq
input = sys.stdin.readline

N, H, T = map(int, input().split())

heap = [-int(input()) for _ in range(N)]
heapq.heapify(heap)

magic = 0

while T > 0 and -heap[0] >= H and -heap[0] > 1:
    tallest = -heapq.heappop(heap)
    tallest //= 2
    heapq.heappush(heap, -tallest)
    magic += 1
    T -= 1

tallest = -heap[0]

if tallest >= H:
    print("NO")
    print(tallest)

else:
    print("YES")
    print(magic)
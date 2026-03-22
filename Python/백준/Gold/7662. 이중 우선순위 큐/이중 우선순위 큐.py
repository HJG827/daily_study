import sys, heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    
    min_heapq = []
    max_heapq = []
    check = [True] * k

    for i in range(k):
        command, num = input().split()
        num = int(num)

        if command == "I":
            heapq.heappush(min_heapq, (num, i))
            heapq.heappush(max_heapq, (-num, i))

        elif command == "D":
            if num == 1:
                while max_heapq and check[max_heapq[0][1]] == False:
                    heapq.heappop(max_heapq)
                if max_heapq:
                    _, idx = heapq.heappop(max_heapq)
                    check[idx] = False

            elif num == -1:
                while min_heapq and check[min_heapq[0][1]] == False:
                    heapq.heappop(min_heapq)
                if min_heapq:
                    _, idx = heapq.heappop(min_heapq)
                    check[idx] = False
    
    while max_heapq and check[max_heapq[0][1]] == False:
        heapq.heappop(max_heapq)
    while min_heapq and check[min_heapq[0][1]] == False:
        heapq.heappop(min_heapq)
        
    if max_heapq and min_heapq:
        print(-max_heapq[0][0], min_heapq[0][0])
    else:
        print("EMPTY")
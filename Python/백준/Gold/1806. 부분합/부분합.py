import sys
input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

INF = float('inf')
ans = INF

left, right = 0, 0
now_sum = 0

while True:
    if now_sum >= S:
        ans = min(ans, right - left)
        now_sum -= numbers[left]
        left += 1
    
    elif right == N:
        break

    else:
        now_sum += numbers[right]
        right += 1

if ans == INF:
    print(0)
else:
    print(ans)
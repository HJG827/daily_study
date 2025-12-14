import sys
input = sys.stdin.readline

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort(key=lambda x:(x[1], x[0]))

ans = 0
i = 0
start = end = 0

while i < N:
    new_start, new_end = meetings[i]
    if new_start >= end:
        ans += 1
        start = new_start
        end = new_end
    
    i += 1

print(ans)
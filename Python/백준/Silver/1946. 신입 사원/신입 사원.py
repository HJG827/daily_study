import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    employees = [list(map(int, input().split())) for _ in range(N)]
    employees.sort(key=lambda x:x[0])

    ans = 0
    best = 10 ** 9

    for doc, interview in employees:
        if interview < best:
            ans += 1
            best = interview
    
    print(ans)

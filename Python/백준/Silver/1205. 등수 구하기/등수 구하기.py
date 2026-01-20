import sys
input = sys.stdin.readline

N, new_score, P = map(int, input().split())
if N == 0:
    print(1)
else:    
    scores = list(map(int, input().split()))
    ans = 1

    if N < P:
        for i in range(N):
            if scores[i] > new_score:
                ans += 1
            else:
                break
        print(ans)

    elif N >= P:
        if scores[-1] >= new_score:
            print(-1)
        else:
            for i in range(N + 1):
                if scores[i] > new_score:
                    ans += 1
                else:
                    break
            print(ans)
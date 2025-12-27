from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    q = deque([i, numbers[i]] for i in range(N))
    
    cnt = [0] * 10
    for num in numbers:
        cnt[num] += 1

    now_idx = 0
    max_value = max(i for i in range(1, 10) if cnt[i])

    while q:
        idx, importance = q.popleft()
        if importance < max_value:
            q.append([idx, importance])
        else:
            now_idx += 1
            cnt[importance] -= 1

            if idx == M:
                print(now_idx)
                break

            elif cnt[importance] == 0:
                for j in range(importance - 1, 0, -1):
                    if cnt[j]:
                        max_value = j
                        break
                else:
                    max_value = 0

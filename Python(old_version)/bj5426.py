# 비밀편지
import sys, math
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    secret = input().strip()
    secret_len = int(math.sqrt(len(secret)))
    arr = [[] for _ in range(secret_len)]
    ans = ''
    for i in range(secret_len):
        for j in range(secret_len):
            arr[i].append(secret[secret_len*i+j])
    # print(arr)

    for c in range(secret_len-1, -1, -1):
        for r in range(secret_len):
            # print(r, c)
            ans += arr[r][c]
            # print(arr[r][c])

    print(ans)
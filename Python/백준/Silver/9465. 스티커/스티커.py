import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    sticker_top = list(map(int, input().split()))
    sticker_bottom = list(map(int, input().split()))

    if n == 1:
        print(max(sticker_top[0], sticker_bottom[0]))
        continue

    dp_top = [0] * n
    dp_bottom = [0] * n
    dp_skip = [0] * n

    dp_top[0] = sticker_top[0]
    dp_bottom[0] = sticker_bottom[0]

    for i in range(1, n):
        dp_top[i] = sticker_top[i] + max(dp_bottom[i - 1], dp_skip[i - 1])
        dp_bottom[i] = sticker_bottom[i] + max(dp_top[i - 1], dp_skip[i - 1])
        dp_skip[i] = max(dp_top[i - 1], dp_bottom[i - 1], dp_skip[i - 1])

    print(max(dp_top[n - 1], dp_bottom[n - 1], dp_skip[n - 1]))
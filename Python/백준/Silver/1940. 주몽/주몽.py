import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

materials = list(map(int, input().split()))
materials.sort()

left = 0
right = N-1
ans = 0

while left < right:
    A = materials[left]
    B = materials[right]

    if A + B < M:
        left += 1
    elif A + B == M:
        ans += 1
        left += 1
        right -= 1
    else:
        right -= 1

print(ans)
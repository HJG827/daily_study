# 덩치

N = int(input())
bodies = []
ans = ''
for _ in range(N):
    x, y = map(int, input().split())
    bodies.append((x, y))

for i in range(N):
    rank = 1
    for j in range(N):
        if i == j:
            continue
        if bodies[i][0] < bodies[j][0] and bodies[i][1] < bodies[j][1]:
            rank += 1

    ans += str(rank)
    ans += ' '

print(ans)
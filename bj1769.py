# 3의 배수

N = input()
cnt = 0

while int(N) // 10 > 0:
    num = 0
    for i in range(len(N)):
        num += int(N[i])
    cnt += 1
    N = str(num)

print(cnt)

if int(N) % 3 == 0:
    print("YES")
else:
    print("NO")
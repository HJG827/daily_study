# 아시아 정보올림피아드

N = int(input())
arr = []

for _ in range(N):
    a, b, c = map(int, input().split())
    arr.append([a,b,c])

arr.sort(key=lambda x: x[-1], reverse=True)

cnt = 0
country = {}
for i in range(N):
    a, b, c = arr[i]
    if a not in country:
        country[a] = 1
        print(a, b)
        cnt += 1
    else:
        if country[a] < 2:
            country[a] += 1
            print(a,b)
            cnt += 1
        else:
            continue

    if cnt == 3:
        break
import sys
input = sys.stdin.readline

N = int(input())

students = [list(map(int, input().split())) for _ in range(N)]
max_classmate = 0
ans = 1

for i in range(N):
    classmate = 0
    for j in range(N):
        if i == j:
            continue
        for grade in range(5):
            if students[i][grade] == students[j][grade]:
                classmate += 1
                break
    if classmate > max_classmate:
        max_classmate = classmate
        ans = i + 1

print(ans)
    
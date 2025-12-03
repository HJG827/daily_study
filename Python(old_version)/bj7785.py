# 회사에 있는 사람

import sys
input = sys.stdin.readline

N = int(input())
company = {}
names = []

for _ in range(N):
    name, record = input().split()
    if record == "enter":
        company[name] = 1
    else:
        company[name] = 0

for name in company.keys():
    if company[name] == 1:
        names.append(name)

names.sort(reverse=True)

for name in names:
    print(name)
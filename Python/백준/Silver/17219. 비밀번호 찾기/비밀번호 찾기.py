import sys
input = sys.stdin.readline

N, M = map(int, input().split())

password_dict = {}

for _ in range(N):
    site, password = input().split()
    password_dict[site] = password

for _ in range(M):
    now = input().strip()
    print(password_dict.get(now))
import sys
input = sys.stdin.readline

N, G = input().split()
players = set()

for _ in range(int(N)):
    players.add(input())

if G == "Y":
    ans = len(players) // 1
    print(ans)
elif G == "F":
    ans = len(players) // 2
    print(ans)
else:
    ans = len(players) // 3
    print(ans)
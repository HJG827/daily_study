import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
find = list(map(int, input().split()))

cards_dict = {}

for idx in range(N):
    if cards_dict.get(cards[idx]):
        cards_dict[cards[idx]] += 1
    else:
        cards_dict[cards[idx]] = 1

for i in range(M):
    if cards_dict.get(find[i]):
        print(cards_dict[find[i]], end=" ")
    else:
        print(0, end=" ")
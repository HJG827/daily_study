# 숫자 카드
import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
my_cards = {a:1 for a in cards}

M = int(input())
arr = list(map(int, input().split()))
ans = []
for i in range(M):
    if my_cards.get(arr[i]):
        ans.append(1)
    else:
        ans.append(0)

print(' '.join(map(str, ans)))
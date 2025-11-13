import sys
input = sys.stdin.readline

N = int(input())
dict = {}

for _ in range(N):
    book = input().strip()
    if dict.get(book):
        dict[book] += 1
    else:
        dict[book] = 1

max_value = max(dict.values())
bestsellers = [key for key, value in dict.items() if value == max_value]

if len(bestsellers) != 1:
    bestsellers.sort()
print(bestsellers[0])
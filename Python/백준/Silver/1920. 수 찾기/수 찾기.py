import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
num_dict = {x:1 for x in numbers}

M = int(input())
check = list(map(int, input().split()))

for num in check:
    if num_dict.get(num) == 1:
        print(1)
    else:
        print(0)
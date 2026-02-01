import sys
input = sys.stdin.readline

X = int(input())

num = 1
sum_num = 1

while sum_num < X:
    num += 1
    sum_num = num * (num + 1) // 2

sum_num = (num - 1) * num // 2
order = X - sum_num

if num % 2 == 0:
    print(f'{order}/{num + 1 - order}')
else:
    print(f'{num + 1 - order}/{order}')
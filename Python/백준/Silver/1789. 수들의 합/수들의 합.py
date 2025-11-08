S = int(input())
num = 0
result = 0
while result < S:
    num += 1
    result += num

if result > S:
    num -= 1

print(num)
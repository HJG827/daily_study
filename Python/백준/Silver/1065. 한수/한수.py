import sys
input = sys.stdin.readline

N = int(input().strip())

def check_number(number):
    if number < 100:
        return True
    if number == 1000:
        return False
    a = number // 100
    b = (number // 10) % 10
    c = number % 10

    return a - b == b - c

ans = 0
for num in range(1, N + 1):
    if check_number(num):
        ans += 1

print(ans)
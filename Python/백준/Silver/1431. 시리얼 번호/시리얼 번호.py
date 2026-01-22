import sys
input = sys.stdin.readline

N = int(input())
guitars = [input() for _ in range(N)]

def sum_digit(number):
    total = 0
    for digit in number:
        if digit.isdigit():
            total += int(digit)

    return total

guitars.sort(key=lambda x: (len(x), sum_digit(x), x))

for guitar in guitars:
    print(guitar.strip())
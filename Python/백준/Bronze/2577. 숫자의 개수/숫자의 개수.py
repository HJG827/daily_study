import sys
input = sys.stdin.readline

A = int(input().strip())
B = int(input().strip())
C = int(input().strip())

number = str(A * B * C)
digits = [0] * 10

for i in range(len(number)):
    digits[int(number[i])] += 1

for digit in digits:
    print(digit)
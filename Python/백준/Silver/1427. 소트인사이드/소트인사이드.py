import sys
input = sys.stdin.readline

N = input().strip()
digits = list(N)
digits.sort(reverse=True)

print("".join(digits))
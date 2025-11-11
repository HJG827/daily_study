import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

a = 0
b = 0

for i in range(N):
    a += A[i]*B[i]
    b += A[i]*B[N-1-i]

print(min(a, b))
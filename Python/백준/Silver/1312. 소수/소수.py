A, B, N = map(int, input().split())

for i in range(N+1):
    result = A // B
    A = (A % B) * 10

print(result)
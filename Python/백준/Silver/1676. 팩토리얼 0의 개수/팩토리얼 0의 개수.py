def find_zero(num):
    ans = 0
    for i in range(1, 4):
        ans += num // (5 ** i)

    return ans

N = int(input())

result = find_zero(N)
print(result)

def atm_minimum_time(N, P):
    P.sort()
    for i in range(1, len(P)):
        P[i] += P[i-1]

    result = sum(P)
    return result

n = int(input())
p = list(map(int, input().split()))
print(atm_minimum_time(n,p))
# 귀걸이

N = int(input())
T = 1
while N != 0:
    check = [0] * (N+1)
    names = []
    for _ in range(N):
        name = input()
        names.append(name)
    
    for _ in range(2*N-1):
        num, alpha = input().split()
        check[int(num)] += 1

    for i in range(1, N+1):
        if check[i] % 2 == 1:
            print(f'{T} {names[i-1]}')
    N = int(input())
    T += 1
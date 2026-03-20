import sys
input = sys.stdin.readline

numbers = list(map(int, input().split()))

def get_numbers(a):
    global k, path, S
    if len(path) == 6:
        print(*path)

    for i in range(a, k):
        if not visited[i]:
            visited[i] = 1
            path.append(S[i])
            get_numbers(i + 1)
            path.pop()
            visited[i] = 0


while numbers != [0]:
    path = []
    k, *S = numbers
    visited =  [0] * k
    get_numbers(0)   
    print()

    numbers = list(map(int, input().split()))
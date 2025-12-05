import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    note1 = {x : 1 for x in map(int, input().split())}

    M = int(input())
    note2 = list(map(int, input().split()))

    for i in range(M):
        if note1.get(note2[i]):
            print(1)
        else:
            print(0)
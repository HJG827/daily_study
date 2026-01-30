import sys
input = sys.stdin.readline

N = int(input())
switch = [8] + list(map(int, input().split()))

S = int(input())
for _ in range(S):
    gender, number = map(int, input().split())

    # 남학생
    if gender == 1:
        for i in range(number, N + 1, number):
            switch[i] = (switch[i] + 1) % 2

    # 여학생
    elif gender == 2:
        symmetric = True
        i = 0
        while symmetric:
            if number - i > 0 and number + i <= N:
                if switch[number - i] == switch[number + i]:
                    if i == 0:
                        switch[number] = (switch[number] + 1) % 2
                    else:
                        switch[number - i] = (switch[number - i] + 1) % 2
                        switch[number + i] = (switch[number + i] + 1) % 2
                    i += 1
                else:
                    symmetric = False

            else:
                symmetric = False

result = switch[1 : ]
for i in range(0, N, 20):
    print(*result[i : i + 20])
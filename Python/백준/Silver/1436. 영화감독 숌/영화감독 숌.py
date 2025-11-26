N = int(input())
order = 0
num = 666

while order <= N:
    if "666" in str(num):
        order += 1
        if order == N:
            print(num)
    num += 1


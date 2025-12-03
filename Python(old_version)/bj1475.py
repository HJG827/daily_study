# 방 번호

N = input()

arr = [0]*10

for i in range(len(N)):
    arr[int(N[i])] += 1

exc = arr[6] + arr[9]
if exc % 2 == 1:
    arr[6] = exc // 2 + 1
    arr[9] = exc // 2
else:
    arr[6] = arr[9] = exc//2

print(max(arr))
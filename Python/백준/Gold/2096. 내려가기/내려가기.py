import sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
    number = list(map(int, input().split()))

    if i == 0:
        prev_min = number[:]
        prev_max = number[:]
    
    else:
        cur_min = [0] * 3
        cur_max = [0] * 3

        cur_min[0] = min(prev_min[0], prev_min[1]) + number[0]
        cur_min[1] = min(prev_min[0], prev_min[1], prev_min[2]) + number[1]
        cur_min[2] = min(prev_min[1], prev_min[2]) + number[2]

        cur_max[0] = max(prev_max[0], prev_max[1]) + number[0]
        cur_max[1] = max(prev_max[0], prev_max[1], prev_max[2]) + number[1]
        cur_max[2] = max(prev_max[1], prev_max[2]) + number[2]

        prev_min = cur_min[:]
        prev_max = cur_max[:]

print(max(prev_max), min(prev_min))
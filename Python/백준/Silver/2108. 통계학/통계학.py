from decimal import Decimal, ROUND_HALF_UP
import sys
input = sys.stdin.readline

N = int(input())
numbers = [int(input()) for _ in range(N)]
numbers.sort()

avg = Decimal(sum(numbers)) / Decimal(N)

cnt = [0] * 8001
for x in numbers:
    cnt[x + 4000] += 1

max_c = max(cnt)
modes = []
for v in range(8001):              
    if cnt[v] == max_c:
        modes.append(v - 4000)    
        if len(modes) == 2:    
            break
mode = modes[1] if len(modes) >= 2 else modes[0]

print(int(avg.quantize(Decimal('1'), rounding=ROUND_HALF_UP)))
print(numbers[N // 2])
print(mode)
print(numbers[N - 1] - numbers[0])
import sys
input = sys.stdin.readline

N = int(input())
numbers = {}

for _ in range(N):
    number = input()
    if numbers.get(number):
        numbers[number] += 1
    else:
        numbers[number] = 1

max_value = max(numbers.values())
max_numbers = [int(key) for key, value in numbers.items() if max_value == value]

print(min(max_numbers))
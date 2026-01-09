import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    commands = list(input().strip())
    n = int(input())

    if n > 0:
        numbers = deque(map(int, input()[1: -2].split(",")))
    else:
        input()
        numbers = deque()
    
    error = False
    reverse = False

    for command in commands:
        if command == "R":
            reverse = not reverse
        elif command == "D":
            if numbers:
                if not reverse:
                    numbers.popleft()
                else:
                    numbers.pop()
            else:
                error = True
                print("error")
                break
    if not error:
        if reverse:
            numbers.reverse()
        print("[" + ",".join(map(str, numbers)) + "]")
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
q = deque()

for _ in range(N):
    words = input().split()

    command = words[0]

    if command == 'push_front':
        x = int(words[1])
        q.appendleft(x)
    elif command == 'push_back':
        x = int(words[1])
        q.append(x)
    elif command == 'pop_front':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif command == 'pop_back':
        if q:
            print(q.pop())
        else:
            print(-1)
    elif command == 'size':
        print(len(q))
    elif command == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif command == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)
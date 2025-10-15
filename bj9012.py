# 괄호
import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    parenthesis = input()
    stack = []
    top = -1
    for i in range(len(parenthesis)):
        if parenthesis[i] == "(":
            stack.append(parenthesis[i])
            top += 1
        elif parenthesis[i] == ")":
            top -= 1
            if top >= -1:
                stack.pop()
            else:
                break
        
    if top == -1 and len(stack) == 0:
        print("YES")

    else:
        print("NO")

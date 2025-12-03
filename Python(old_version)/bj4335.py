# 숫자 맞추기
import sys
input = sys.stdin.readline

N = int(input())
arr = [1] * 11

while N != 0:
    num = N
    res = input().strip()

    if res == "too high":
        for i in range(num, 11):
            arr[i] = 0
        
    elif res == "too low":
        for j in range(num+1):
            arr[j] = 0
    else:
        if arr[num]:
            print("Stan may be honest")
            arr = [1] * 11
        else:
            print("Stan is dishonest")
            arr = [1] * 11

    N = int(input())
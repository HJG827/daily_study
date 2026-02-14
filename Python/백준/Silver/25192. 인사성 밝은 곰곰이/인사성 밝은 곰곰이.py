import sys
input = sys.stdin.readline

N = int(input())
ans = 0
people = {}

for i in range(N):
    text = input().strip()

    if text == "ENTER":
        people = {}
    
    else:
        if people.get(text) is None:
            people[text] = 1
            ans += 1
        else:
            continue

print(ans)
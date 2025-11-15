import sys
input = sys.stdin.readline

word = input().strip()
ans = 0

index = 0
while index < len(word):
    if word[index] == "c":
        if index+1 < len(word) and (word[index+1] == "=" or word[index+1] == "-"):
            index += 1
    elif word[index] == "d":
        if index+1 < len(word) and word[index+1] == "-":
            index += 1
        elif index+2 < len(word) and word[index+1] == "z" and word[index+2] == "=":
            index += 2
    elif word[index] == "l":
        if index+1 < len(word) and word[index+1] == "j":
            index += 1
    elif word[index] == "n":
        if index+1 < len(word) and word[index+1] == "j":
            index += 1
    elif word[index] == "s":
        if index+1 < len(word) and word[index+1] == "=":
            index += 1
    elif word[index] == "z":
        if index+1 < len(word) and word[index+1] == "=":
            index += 1
    index += 1
    ans += 1

print(ans)
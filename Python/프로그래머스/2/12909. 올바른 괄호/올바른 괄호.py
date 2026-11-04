def solution(s):
    answer = True
    
    arr = []
    top = -1
    
    for i in range(len(s)):
        if s[i] == "(":
            arr.append("(")
            top += 1
            
        elif s[i] == ")":
            top -= 1
            
        if top < -1:
            return False

    if top != -1:
        return False
    
    return True
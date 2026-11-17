def solution(s):
    answer = [0, 0]
    
    while s != '1':
        cnt = 0
        
        for i in range(len(s)):
            if s[i] == '0':
                cnt += 1

        s = bin(len(s) - cnt)[2:]
        answer[0] += 1
        answer[1] += cnt
        
    return answer
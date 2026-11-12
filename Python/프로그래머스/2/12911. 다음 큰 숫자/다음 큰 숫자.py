def solution(n):
    def count_one(num):
        num = str(num)
        cnt = 0
        for i in range(len(num)):
            if num[i] == "1":
                cnt += 1
        
        return cnt
    
    answer = n + 1
    ones = count_one(bin(n)[2:])
    
    while True:
        check = count_one(bin(answer)[2:])
        
        if ones == check:
            break
        else:
            answer += 1
    
    return answer
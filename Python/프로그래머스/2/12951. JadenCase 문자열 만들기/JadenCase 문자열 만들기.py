def solution(s):
    answer = ''
    
    words = s.split(' ')
    
    
    for i in range(len(words)):
        if words[i] == '':
            word = ''
        elif words[i][0].isdigit():
            word = words[i][0] + words[i][1:].lower()
        else:
            word = words[i][0].upper() + words[i][1:].lower()
        
        answer += word
        
        if i != len(words) - 1:
            answer += ' '

    return answer
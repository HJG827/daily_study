function solution(brown, yellow) {
    var area = brown + yellow;
    var width = 0;
    var height = 0;
    
    width = Math.ceil(Math.sqrt(area));
    
    while (true) {
        if (area % width === 0) {
            height = area / width;
            
            if ((width - 2) * (height - 2) === yellow) {
                break;
            }
        } 
        width++;
    }
    
    var answer = [width, height];
    return answer;
}
function solution(s) {
    let zero = 0;
    let change = 0;
    
    while (s != "1") {
       let one = 0;
        for (let i = 0; i < s.length; i++) {
            if (s[i] == '0') {
                zero += 1
            }
            else {
                one += 1
            }
        }
        
        s = one.toString(2);
        change += 1
    }
    
    return [change, zero];
}
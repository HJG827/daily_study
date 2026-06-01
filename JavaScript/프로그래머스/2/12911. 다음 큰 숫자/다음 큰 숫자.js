function solution(n) {
    function countOne(num) {
        const binary = num.toString(2);
        let cnt = 0;
        
        for (let i = 0; i < binary.length; i++) {
            if (binary[i] === "1") {
                cnt++;
            }
        }
        return cnt;
    }
    
    const targetOne = countOne(n);
    
    let number = n + 1;
    while (true) {
        if (targetOne === countOne(number)) {
            return number;
        }
        
        number++;
    }
}
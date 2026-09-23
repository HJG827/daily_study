function solution(numbers) {
    var answer = [];
    
    for (const x of numbers) {
        if (x % 2 === 0) {
            answer.push(x + 1);
        } else {
            let binary = "0" + x.toString(2);
            const idx = binary.lastIndexOf("0");
            
            binary = binary.slice(0, idx) + "10" + binary.slice(idx + 2);
            
            answer.push(parseInt(binary, 2));
            
            } 
        }
    
    return answer;
}
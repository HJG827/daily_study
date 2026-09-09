function solution(arr1, arr2) {
    const answer = Array.from({length:arr1.length}, () => 
        Array(arr2[0].length).fill(0));
    
    for (let r = 0; r < arr1.length; r++) {
        for (let c = 0; c < arr2[0].length; c++) {
            let sum = 0;
            
            for (let k = 0; k < arr2.length; k++) {
                sum += arr1[r][k] * arr2[k][c];
            }
            
            answer[r][c] = sum;
        }
    }
    
    return answer;
}
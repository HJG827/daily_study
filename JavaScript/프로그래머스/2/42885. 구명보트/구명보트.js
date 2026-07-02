function solution(people, limit) {
    var answer = 0;
    
    people.sort((a, b) => a - b);
    
    var left = 0;
    var right = people.length - 1;
    
    while (left <= right) {
        const weight = people[left] + people[right];
        if (weight > limit) {
            answer++;
            right--;
        }
        else {
            answer++;
            left++;
            right--;
        }
    }
    return answer;
}
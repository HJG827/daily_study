function solution(progresses, speeds) {
    var answer = [];
    const days = progresses.map((progress, index) => {
        return Math.ceil((100 - progress) / speeds[index]);
    });
    
    let nowDay = days[0];
    let cnt = 1;
    
    for (let i = 1; i < days.length; i++) {
        if (days[i] <= nowDay) {
            cnt++;
        }
        else {
            answer.push(cnt);
            nowDay = days[i];
            cnt = 1;
        }
    }
    
    answer.push(cnt);
    
    return answer;
}
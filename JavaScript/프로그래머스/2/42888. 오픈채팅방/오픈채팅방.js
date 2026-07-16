function solution(record) {
    var answer = [];
    const arr = record.map((str) => str.split(" "))
    const map = new Map();
    arr.forEach(([command, id, nickname]) => {
    if (command !== "Leave") {
        map.set(id, nickname);
    }
    })
    
    arr.forEach(([command, id, nickname]) => {
        if (command === "Enter") {
            answer.push(`${map.get(id)}님이 들어왔습니다.`);
        }
        else if (command === "Leave") {
            answer.push(`${map.get(id)}님이 나갔습니다.`)
        }
    })
    
    
    return answer;
}
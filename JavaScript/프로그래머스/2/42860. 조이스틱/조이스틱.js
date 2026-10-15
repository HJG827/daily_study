function solution(name) {
    var control = 0;
    
    for (let i = 0; i < name.length; i++) {
        const code = name[i].charCodeAt(0);

        control += Math.min(
            code - 65,
            91 - code
        );
    }
    
    let move = name.length - 1;

    for (let i = 0; i < name.length; i++) {
        let next = i + 1;

        while (next < name.length && name[next] === "A") {
            next++;
        }

        move = Math.min(
            move,
            i * 2 + name.length - next,
            (name.length - next) * 2 + i
        );
    }
    
    return control + move;
}
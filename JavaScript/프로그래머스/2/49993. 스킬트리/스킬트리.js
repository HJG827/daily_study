function solution(skill, skill_trees) {
    var answer = 0;
    
    for (const skill_tree of skill_trees) {
        let idx = 0;
        let status = 0;
        let possible = true;
        
        while (idx < skill_tree.length) {
            const now = skill_tree[idx];
            
            if (!skill.includes(now)) {
                idx++;
                continue;
            }
            
            if (now === skill[status]) {
                status++;
            } else {
                possible = false;
                break;
            }
            idx++;
        }
        
        if (possible) {
            answer++;
        }
    }
    
    return answer;
}
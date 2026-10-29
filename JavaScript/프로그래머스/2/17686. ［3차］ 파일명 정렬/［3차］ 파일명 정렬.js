function solution(files) {
    const parsed = files.map((file, index) => {
        const match = file.match(/^(\D+)(\d{1,5})(.*)$/);
        
        return {
            file: file,
            head: match[1],
            number: Number(match[2]),
            index: index
        };
    });
    
    parsed.sort((a, b) => {
        const headA = a.head.toLowerCase();
        const headB = b.head.toLowerCase();
        
        if (headA < headB) return -1;
        if (headA > headB) return 1;
        
        if (a.number !== b.number) {
            return a.number - b.number;
        }
        
        return a.index - b.index;
    });
    
    return parsed.map(item => item.file);
}
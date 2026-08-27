function solution(m, n, board) {
    let answer = 0;
    
    board = board.map((row) => row.split(""));
    
    function findBlocks() {
        var clearBlock = new Set();
        
        for (let r = 0; r < m - 1; r++) {
            for (let c = 0; c < n - 1; c++) {
                const now = board[r][c];
                
                if (now === " ") continue;
                
                if (
                    board[r][c + 1] === now &&
                    board[r + 1][c] === now &&
                    board[r + 1][c + 1] === now
                ) {
                    clearBlock.add(`${r},${c}`);
                    clearBlock.add(`${r},${c + 1}`);
                    clearBlock.add(`${r + 1},${c}`);
                    clearBlock.add(`${r + 1},${c + 1}`);
                }   
            }
        }
        return clearBlock;
    }
    
    function removeBlocks(clearBlocks) {
        for (const pos of clearBlocks) {
            const [r, c] = pos.split(",").map(Number);
            board[r][c] = " ";
        }    
    }
    
    function dropBlocks() {
        for (let c = 0; c < n; c++) {
            const stack = [];
            
            for (let r = m - 1; r >= 0; r--) {
                if (board[r][c] !== " ") {
                    stack.push(board[r][c]);
                }
            }
            
            for (let r = m - 1; r >= 0; r--) {
                if (stack.length > 0) {
                    board[r][c] = stack.shift();
                } else {
                    board[r][c] = " ";
                }
            }
        }
    }
    
    while (true) {
        const clearBlock = findBlocks();
        
        if (clearBlock.size === 0) {
            break;
        }
        
        answer += clearBlock.size;
        removeBlocks(clearBlock);
        dropBlocks();
    }
    
    return answer;
}
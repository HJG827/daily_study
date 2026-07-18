function solution(book_time) {
    function toMinute(time) {
        const [hour, minute] = time.split(":").map(Number);
        return hour * 60 + minute;
    }
    
    const times = book_time.map(([time1, time2]) => [toMinute(time1), toMinute(time2)])
    times.sort((a, b) => a[0] - b[0])
    
    const rooms = [];
    
    for (const [start, end] of times) {
        let available = false;
        
        for (let i = 0; i < rooms.length; i++) {
            if (rooms[i] <= start) {
                rooms[i] = end + 10;
                available = true;
                break;
            }
        }

        if (!available) {
            rooms.push(end + 10);
        }
    }
    
    return rooms.length;
}
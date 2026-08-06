function solution(fees, records) {
    function setMinute(input) {
        const [hour, minute] = input.split(":").map(Number);
        return hour * 60 + minute;
    }
    
    var answer = [];
    const inCars = new Map();
    const totalCars = new Map();
    
    records.forEach(record => {
        const [timestr, number, history] = record.split(' ');
        const time = setMinute(timestr);

        if (history === "IN") {
            inCars.set(number, time);
        }
        else if (history === "OUT") {
            const inTime = inCars.get(number);
            const parkingTime = time - inTime;
            
            totalCars.set(number, (totalCars.get(number) || 0) + parkingTime);
            inCars.delete(number);
        }
    })
    
    const endTime = setMinute("23:59");
    
    for (const [number, inTime] of inCars) {
        const parkingTime = endTime - inTime;
        totalCars.set(number, (totalCars.get(number) || 0) + parkingTime);
    }
    
    const cars = [...totalCars.entries()];
    
    cars.sort((a, b) => a[0].localeCompare(b[0]));
    
    for (let i = 0; i < cars.length; i++) {
        const [number, time] = cars[i];
        let fee = 0;
        let parkingTime = time;
        
        if (parkingTime > fees[0]) {
            fee += fees[1];
            parkingTime -= fees[0];
             
            if (parkingTime % fees[2] !== 0) {
                fee += (Math.trunc(parkingTime / fees[2]) + 1) * fees[3]
            }
            else {
                fee += (parkingTime / fees[2]) * fees[3]
            }
        }
        else {
            fee = fees[1];
        }
        answer.push(fee);
    }
    return answer;
}
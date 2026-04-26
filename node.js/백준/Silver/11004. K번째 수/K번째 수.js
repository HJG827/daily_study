const fs = require("fs");

const input = fs.readFileSync(0, "utf8").trim().split("\n");

const [N, K] = input[0].split(" ").map(Number);
const arr = input[1].split(" ").map(Number);

arr.sort((a, b) => a - b);

console.log(arr[K - 1]);
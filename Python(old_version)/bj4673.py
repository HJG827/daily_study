# 셀프 넘버

arr = [num for num in range(1, 10001)]
for i in range(1, 10001):
    number = str(i)
    result = i
    for digit in range(len(number)):
        result += int(number[digit])
    
    if result in arr:
        arr.remove(result)

for j in range(len(arr)):
    print(arr[j])
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
white_square = 0
blue_square = 0


def check_square(sr, sc, size):
    start = arr[sr][sc]
    for r in range(sr, sr + size):
        for c in range(sc, sc + size):
            if arr[r][c] != start:
                return False
    
    if start == 1:
        return "blue"
    else:
        return "white"

def divide(r, c, size):
    global white_square, blue_square
    if check_square(r, c, size) == "blue":
        blue_square += 1
        return
    elif check_square(r, c, size) == "white":
        white_square += 1
        return
    
    half = size // 2

    divide(r, c, half)
    divide(r + half, c, half)
    divide(r, c + half, half)
    divide(r + half, c + half, half)

divide(0, 0, N)
print(white_square)
print(blue_square)
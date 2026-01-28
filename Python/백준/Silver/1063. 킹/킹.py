import sys
input = sys.stdin.readline

dir_r = [0, 0, -1, 1,  1, 1, -1, -1]
dir_c = [1, -1, 0, 0, 1, -1, 1, -1]
dirs = {"R":0, "L":1, "B":2, "T":3, "RT":4, "LT":5, "RB":6, "LB":7}

def change_number(loc):
    c, r = loc[0], loc[1]
    r = int(r) - 1
    c = ord(c) - ord('A')
    return r, c

def change_location(r, c):
    c = chr(c + ord('A'))
    r = str(r + 1)
    return c + r

king, rock, N = input().split()
kr, kc = change_number(king)
rr, rc = change_number(rock)

for _ in range(int(N)):
    idx = dirs[input().strip()]
    dr, dc = dir_r[idx], dir_c[idx]

    nr = kr + dr
    nc = kc + dc

    if not (0 <= nr < 8 and 0 <= nc < 8):
        continue

    if nr == rr and nc == rc:
        if (
            0 <= rr + dr < 8
            and 0 <= rc + dc < 8
        ):
            rr += dr
            rc += dc
        else:
            continue
    
    kr = nr
    kc = nc

print(change_location(kr, kc))
print(change_location(rr, rc))
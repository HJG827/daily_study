import sys
input = sys.stdin.readline

N, M = map(int, input().split())
truth, *truth_people = list(map(int, input().split()))

parent = [i for i in range(N + 1)]
parties = []
unavailable_root = set()
ans = 0

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    ra = find(a)
    rb = find(b)

    if ra != rb:
        parent[rb] = ra

for _ in range(M):
    party, *participant = list(map(int, input().split()))

    parties.append(participant)

    if party == 1:
        continue

    else:
        for i in range(1, party):
            union(participant[0], participant[i])

for person in truth_people:
    unavailable_root.add(find(person))

for party in parties:
    if find(party[0]) in unavailable_root:
        continue
    else:
        ans += 1

print(ans)
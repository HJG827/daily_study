# 좌표 압축
import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
# 서로 달라야 하므로 중복 제거 위해 set 변형
sorted_numbers = sorted(set(numbers))

# 조회 시간 줄이기 위해 딕셔너리 생성
rank = {}
for a in range(len(sorted_numbers)):
    rank[sorted_numbers[a]] = a

ans = []
for i in range(N):
    num = numbers[i]
    ans.append(rank[num])

print(" ".join(map(str, ans)))
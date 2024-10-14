# # 1037.약수
# count = int(input())
# nums = list(map(int, input().split()))

# N = min(nums) * max(nums)
# print(N)

# # 25192.인사성 밝은 곰곰이
# N = int(input())
# users = [input() for _ in range(N)]

# answer = 0
# current_users = set()

# for user in users:
#     if user == "ENTER":
#         current_users.clear()
#     else:
#         if user not in current_users:
#             answer += 1
#             current_users.add(user)

# print(answer)

# # 26069.붙임성 좋은 총총이
# N = int(input())
# dance = {"ChongChong"}

# for _ in range(N):
#     A,B = input().split()
#     if A in dance or B in dance:
#         dance.add(A)
#         dance.add(B)

# answer = len(dance)
# print(answer)

# 2108.통계학
from collections import Counter
N = int(input())
nums = [int(input()) for _ in range(N)]
# 산술평균
a = round(sum(nums)/N)
# 중앙값
b = sorted(nums)[N//2]
# 최빈값
count = Counter(nums)
most = count.most_common()

if len(most) > 1 and most[0][1] == most[1][1]:
    same_frequency = [key for key, value in most if value == most[0][1]]
    c = sorted(same_frequency)[1]  # 두 번째로 작은 값
else:
    c = most[0][0]
    
# 범위
d = max(nums) - min(nums)

print(a)
print(b)
print(c)
print(d)
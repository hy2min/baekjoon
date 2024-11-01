
# s = list(str(n))
# leng = len(s)

# i = leng - 2
# while i >= 0 and s[i] >= s[i+1] :
#     i -= 1

# j = leng - 1
# while s[j] <= s[i] :
#     j -= 1
# s[i], s[j] = s[j], s[i]

# s = s[:i + 1] + sorted(s[i + 1:])

# print(int(''.join(s))) 


# # 정리 정돈을 좋아하는 k씨
# n, m = map(int,input().split())
# a = list(map(int,input().split()))
# queries = []
# for _ in range(m) :
#     i,j,k = map(int,input().split())
#     queries.append((i,j,k))

# for (i,j,k) in queries :
#     subquery = sorted(a[i-1:j])
#     answer = subquery[k-1]
#     print(answer)

# 빨간 선과 파란 선
n = int(input())
colors = map(int, input().split())
parent = list(range(n))

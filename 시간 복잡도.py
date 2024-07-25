# # 24262.알고리즘 수업
# n = int(input())
# count = 1
# complexity = 0
# print(count)
# print(complexity)

# # 24263.알고리즘 수업
# n = int(input())
# cnt = n
# complexity = 1
# print(cnt)
# print(complexity)

# # 24264.알고리즘 수업
# n = int(input())
# cnt = n**2
# complexity = 2
# print(cnt)
# print(complexity)

# # 24265.알고리즘 수업
# n = int(input())
# cnt = (n*(n-1))//2
# complexity = 2
# print(cnt)
# print(complexity)

# # 24266.알고리즘 수업
# n = int(input())
# cnt = n**3
# complexity = 3
# print(cnt)
# print(complexity)

# # 24267.알고리즘 수업
# n = int(input())
# cnt = n*(n-1)*(n-2)//6
# complexity = 3
# print(cnt)
# print(complexity)

# # 24313.알고리즘 수업
a_1,a_0 = map(int,input().split())
c = int(input())
n_0 = int(input())
is_valid = True
for n in range(n_0,101) :
    if n*(c-a_1) < a_0 :
        is_valid=False
        break

if is_valid :
    print(1)
else :
    print(0)
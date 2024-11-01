# # 10807.개수 세기
# N = int(input())
# n_list = list(map(int,input().split()))
# v = int(input())
# print(n_list.count(v))

# 10871.X보다 작은 수
# N,X = map(int,input().split())
# A = list(map(int,input().split()))
# for i in A :
#     if i < X :
#         print(i, end = ' ')

# 10818.최소,최대
# N = int(input())
# for i in range(N) :
#     n_list = list(map(int,input().split()))
#     print(str(min(n_list))+" "+str(max(n_list)))

# # 2562.최댓값
# n_list = []
# for i in range(9) :
#     n_list.append(int(input()))
# print(max(n_list))
# print(n_list.index(max(n_list))+1)

# # 10810.공 넣기
# n,m = map(int,input().split())
# basket = [0 for i in range(n)]
# for _ in range(m) :
#     i,j,k = map(int,input().split())
#     for x in range(i-1,j) :
#         basket[x] = k
# for i in range(n) :
#     print(basket[i], end=" ")

# # 10813.공 바꾸기
# n,m = map(int,input().split())
# basket = list(range(1,n+1))
# for _ in range(m) :
#     i,j = map(int,input().split())
#     basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

# for i in range(n) :
#     print(basket[i],end= ' ')    

# # 5597.과제 안 내신 분..?
# students = [i for i in range(1,31)]
# for _ in range(28) :
#     n = int(input())
#     if n in students :
#         students.remove(n)
# print(min(students))
# print(max(students))

# # 3052.나머지
# numbers = []
# for _ in range(10) :
#     n = int(input())
#     numbers.append(n)
# remainders = [n%42 for n in numbers]
# count_num = set(remainders)
# print(len(count_num))

# # 10811.바구니 뒤집기
# n, m = map(int, input().split())
# nums = []
# for num in range(n) :
#     nums.append(num+1)
# for _ in range(m) :
#     i, j = map(int,input().split())
#     nums[i-1:j] = nums[i-1:j][::-1] 
# answer = " ".join(map(str,nums))
# print(answer)

# 1546.평균
n = int(input())
score = list(map(int,input().split()))
average = sum(score)*100/(n*max(score))
print(average)
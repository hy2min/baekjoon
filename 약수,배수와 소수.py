# # 5086.배수와 약수
# while True :
#     a,b = map(int,input().split())
#     if a == 0 and b == 0 :
#         break
#     if a % b == 0 :
#         print("multiple")
#     elif b % a == 0 :
#         print("factor")
#     else : 
#         print("neither")

# # 2501.약수 구하기
# n,k = map(int,input().split())
# num_list = []
# for i in range(1,n+1) :
#     if n % i == 0 :
#         num_list.append(i)
# if len(num_list) < k :
#     print(0)
# else :
#     print(num_list[k-1])

# # 9506.약수들의 합
# while True:
#     n = int(input())
#     if n == -1 :
#         break
#     num_list = []
#     for i in range(1,n) :
#         if n % i == 0 :
#             num_list.append(i)
#     if sum(num_list) == n :
#         plus_num = " + ".join(map(str, num_list))
#         print(f'{n} = {plus_num}')
#     else :
#         print(f'{n} is NOT perfect.')

# # 1978.소수 찾기
# n = int(input())
# num_list = list(map(int,input().split()))

# def is_prime(num) :
#     if num < 2 :
#         return False
#     for i in range(2, int(num**0.5) +1) :
#         if num % i == 0 :
#             return False
#     return True

# count = 0
# for i in num_list :
#     if is_prime(i) :
#         count += 1
# print(count)

# # 2581.소수
# m = int(input())
# n = int(input())

# def is_prime(num) :
#     if num < 2 :
#         return False
#     for i in range(2, int(num**0.5)+1) :
#         if num % i == 0 :
#             return False
#     return True

# result = []
# for i in range(m,n+1) :
#     if is_prime(i) :
#         result.append(i)

# if result == [] : 
#     print(-1)
# else :
#     print(sum(result))
#     print(result[0])

# 11653.소인수 분해
n = int(input())
answer = []
i = 2

while i*i <= n  :
    while n % i == 0 :
        print(i)
        n //= i
    i += 1

if n > 1 :
    print(n)
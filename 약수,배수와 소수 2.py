# # 1934.최소공배수
# import math
# n = int(input())
# for _ in range(n) :
#     n,m = map(int,input().split())
#     print(math.lcm(n,m))

# # 13241.최소공배수
# def gcd(a,b) :
#     while b :
#         a,b = b,a%b
#     return a

# def lcm(a,b) :
#     return (a*b)//gcd(a,b)

# a,b = map(int,input().split())
# print(lcm(a,b))

# # 1735.분수 합
# def gcd(a,b) :
#     while b:
#         a,b = b,a%b
#     return a
# a,b = map(int,input().split())
# c,d = map(int,input().split())
# m = a*d + c*b
# n = b*d
# answer = [str(m//gcd(m,n)),str(n//gcd(m,n))]
# print(" ".join(answer))

# # 2485.가로수
# import math
# n = int(input())
# trees = [int(input()) for _ in range(n)]
# gaps = [trees[i+1]- trees[i] for i in range(n-1)]

# gcd = gaps[0]
# for gap in gaps[1:] :
#     gcd = math.gcd(gcd,gap)

# tree_cnt = 0
# for gap in gaps :
#     tree_cnt += (gap//gcd)-1

# print(tree_cnt)

# # 4134.다음 소수
# def is_prime(n) :
#     if n < 2 :
#         return False
#     if n ==2 :
#         return True
#     if n % 2 == 0 :
#         return False
#     i = 3
#     while i * i <= n :
#         if n % i == 0 :
#             return False
#         i= i + 2
#     return True

# def next_prime(n) :
#     while True :
#         if is_prime(n) :
#             return n
#         n += 1

# n = int(input())
# cases = [int(input()) for _ in range(n)]
# for case in cases :
#     print(next_prime(case))

# # 1929.소수 구하기
# def is_prime(n) :
#     if n < 2 :
#         return False
#     if n == 2 :
#         return True
#     if n % 2 == 0 :
#         return False
#     i = 3
#     while i * i <= n :
#         if n % i == 0 :
#             return False
#         i += 2
#     return True

# m,n = map(int,input().split())
# for i in range(m,n+1) :
#     if is_prime(i) :
#         print(i)

# 4948.베르트랑 공준
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


while True:
    n = int(input())
    if n == 0:
        break
    answer = 0
    for i in range(n+1, (2*n)+1):
        if is_prime(i):
            answer += 1
    print(answer)

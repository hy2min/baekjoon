# # 15439.베라의 패션
# n = int(input())
# print(n*(n-1))

# # 24723.녹색거탑
# n = int(input())
# print(2**n)

# # 10872.팩토리얼
# def factorial(n) :
#     if n == 1 or n == 0 :
#         return 1
#     else :
#         return n * factorial(n-1)

# n = int(input())
# print(factorial(n))

# # 11050.이항 계수 1
# def factorial(n) :
#     if n == 1 or n == 0 :
#         return 1
#     else :
#         return n * factorial(n-1)

# n, k = map(int,input().split())
# answer = factorial(n)//(factorial(n-k)*factorial(k))
# print(answer)

# 1010.다리 놓기
def factorial(n) :
    if n ==1 or n ==0 :
        return 1
    else:
        return n * factorial(n-1)

t = int(input())
for _ in range(t) :
    n, m = map(int,input().split())
    answer = factorial(m)//(factorial(m-n) * factorial(n))
    print(answer)
# # 27433. 팩토리얼2
# n = int(input())

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(n))

# 10870. 피보나치 수 5
n = int(input())

def fibo(n):
    if n == 0: 
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
print(fibo(n))
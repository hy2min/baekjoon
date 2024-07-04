# # 2739.구구단2
# n = int(input())
# for i in range(1,10) :
#     print(str(n)+ " * " + str(i) + " = " + str(n*i))

# # 10950.A+B-3
# T = int(input())
# for i in range(T) :
#     A,B = map(int,input().split())
#     print(A+B)

# # 8393.합
# n = int(input())
# answer = 0
# for i in range(1,n+1) :
#     answer += i
# print(answer)

# # 25304.영수증
# X = int(input())
# N = int(input())
# answer = 0
# for i in range(N) :
#     a,b = map(int,input().split())
#     answer += a*b
# if X == answer :
#     print("Yes")
# else : 
#     print("No")

# # 11021.A+B - 7
# T = int(input())
# for i in range(1,T+1) :
#     a,b = map(int,input().split())
#     print(f"Case #{i}: {a+b}")

# # 11022.A+B - 8
# T = int(input())
# for i in range(1,T+1) :
#     a,b = map(int,input().split())
#     print(f"Case #{i}: {a} + {b} = {a+b}")

# # 2439.별 찍기 - 1
# N = int(input())
# for i in range(1,N+1) : 
#     print("*"*i)

# # 2439.별 찍기 - 2
# N = int(input())
# for i in range(1,N+1) :
#     print(" "*(N-i)+"*"*i)

# # 10952.A+B - 5
# while True :
#     a,b = map(int,input().split())
#     if a == 0 and b == 0 :
#         break
#     else :
#         print(a+b)

# # 25314.코딩은 체육과목입니다
# N = int(input())
# print("long "*(N//4)+"int")

# 10951.A+B - 4
while True:
    try :        
        a,b = map(int,input().split())
        print(a+b)
    except :
        break
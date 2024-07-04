# # 1330.두 수 비교하기
# A, B = map(int,input().split())
# if A > B :
#     print(">")
# elif A < B :
#     print("<")
# elif A == B:
#     print("==")

# # 9498.시험 성적
# n = int(input())
# if n >= 90 :
#     print("A")
# elif n >= 80 :
#     print("B")
# elif n >= 70 :
#     print("C")
# elif n >= 60 :
#     print("D")
# else :
#     print("F")

# # 2753.윤년
# y = int(input())
# if y % 4 == 0 and (y % 100 != 0 or y % 400 ==0) :
#     print(1)
# else :
#     print(0)

# # 14681.사분면 고르기
# x = int(input())
# y = int(input())
# if x > 0 :
#     if y > 0 :
#         print(1)
#     elif y < 0 :
#         print(4)
# elif x < 0 : 
#     if y > 0 :
#         print(2)
#     elif y < 0 :
#         print(3)

# # 2884.알람 시계
# H, M = map(int,input().split())
# if M >=45 :
#     M = M - 45
# else :
#     if H == 0 :
#         H = 23
#     else :
#         H = H -1
#     M = M + 15 
# print(str(H)+" "+str(M))

# # 2525.오븐 시계
# A, B = map(int,input().split()) 
# C = int(input())
# B = B+C
# if B>= 60 :
#     A = A+ (B//60)
#     B = B % 60
# if A >= 24 :
#         A = A % 24
# print(str(A)+ " " + str(B))

# # 2480.주사위 세 개
# a,b,c = map(int,input().split())
# if a == b == c :
#     print(10000+a*1000)
# elif a == b or b == c :
#     print(1000+b*100)
# elif a == c : 
#     print(1000+a*100)
# else :
#     print(max(a,b,c)*100)
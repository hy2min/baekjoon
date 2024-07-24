# # 27323.직사각형
# a = int(input())
# b = int(input())

# print(a*b)

# # 1085.직사각형에서 탈출
# x,y,w,h = map(int,input().split())
# answer = min(x,y,w-x,h-y)
# print(answer)

# # 3009.네 번째 점
# x_list = []
# y_list = []
# for _ in range(3) :
#     x,y = map(int,input().split())
#     x_list.append(x)
#     y_list.append(y)

# if x_list.count(x_list[0]) == 1 :
#     a = x_list[0]
# elif x_list.count(x_list[1]) == 1 :
#     a = x_list[1]
# else :
#     a = x_list[2]

# if y_list.count(y_list[0]) == 1 :
#     b = y_list[0]
# elif y_list.count(y_list[1]) == 1 :
#     b = y_list[1]
# else :
#     b = y_list[2]

# print(a,b)

# # 15894.수학은 체육과목 입니다.
# n = int(input())
# print(n*4)

# 9063.대지
# x_list = []
# y_list = []
# n = int(input())
# for _ in range(n) :
#     x, y = map(int,input().split())
#     x_list.append(x)
#     y_list.append(y)
# answer = (max(x_list)-min(x_list))*(max(y_list)-min(y_list))
# print(answer)

# # 10101.삼각형 외우기
# a = int(input())
# b = int(input())
# c = int(input())

# if a+b+c != 180 :
#     print("Error")
# elif a==60 and b==60 and c==60 :
#     print("Equilateral")
# elif a==b or b==c or c==a :
#     print("Isosceles")
# else :
#     print("Scalene")

# # 5073.삼각형과 세 변
# while True:
#     a,b,c = map(int,input().split())
#     if (a,b,c) == (0,0,0) :
#         break
#     length = [a,b,c]
#     length.sort()
#     if length[0] + length[1] <= length[2] :
#         print("Invalid")
#     else :
#         if a == b == c :
#             print("Equilateral")
#         elif a == b or b == c or c == a :
#             print("Isosceles")
#         else :
#             print("Scalene")

# 14215.세 막대
length = list(map(int,input().split()))
length.sort()


while length[0] + length[1] <= length[2] :
    length[2] -= 1

print(sum(length))

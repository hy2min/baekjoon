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

# 2753.윤년
y = int(input())
if y % 4 == 0 and (y % 100 != 0 or y % 400 ==0) :
    print(1)
else :
    print(0)
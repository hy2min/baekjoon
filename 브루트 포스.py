# # 2798.블랙잭
# n,m = map(int,input().split())
# cards = list(map(int,input().split()))
# result = 0
# for i in range(n) :
#     for j in range(i+1,n) :
#         for k in range(j+1,n) :
#             card_sum = cards[i] + cards[j] + cards[k]
#             if card_sum <= m and card_sum > result :
#                 result = card_sum
# print(result)

# # 2231.분해합
# n = int(input())
# answer = 0
# for m in range(n+1) :
#     string = str(m)
#     separate = 0
#     for i in range(len(string)) :
#         separate += int(string[i])
#     if n == m + separate :
#         answer = m
#         break
# print(answer)

# # 19532.수학은 비대면강의입니다
# a,b,c,d,e,f = map(int,input().split())
# x = (c*e-b*f)//(a*e-b*d)
# y = (c*d-a*f)//(b*d-a*e)
# print(x, y)

# # 1018.체스판 다시 칠하기
# n,m = map(int,input().split())
# board = []
# result = []

# for _ in range(n) :
#     board.append(list(input()))

# for i in range(n-8+1) :
#     for j in range(m-8+1) :
#         black = 0
#         white = 0

# for x in range(i, i+8) :
#     for y in range(j, j+8) :
#         if (x+y)%2 == 0 :
#             if board[x][y] != "B" :
#                 black += 1
#             if board[x][y] != "W" :
#                 white += 1
#         else :
#             if board[x][y] != "W" :
#                 black += 1
#             if board[x][y] != "B" :
#                 white += 1

#         result.append(black)
#         result.append(white)

# print(min(result))

# # 1436.영화감독 숌
# n = int(input())

# cnt = 0
# num = 0

# while True :
#     cnt += 1
#     title = str(cnt)
#     if "666" in title :
#         num += 1
#         if n == num : 
#             break
# print(title)

# 2839.설탕 배달
n = int(input())
five = n // 5
answer = -1
while five >= 0 :
    remain = n - (five*5)
    if remain % 3 == 0 :
        three = remain // 3
        answer = five + three
        break
    else:
        five -= 1

print(answer)
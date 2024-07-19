# # 2738.행렬 덧셈
# n,m = map(int,input().split())
# a = []
# b = []
# for _ in range(n) :
#     a.append(list(map(int,input().split())))
# for _ in range(n) :
#     b.append(list(map(int,input().split())))

# result = []
# for i in range(n) :
#     row = []
#     for j in range(m) :
#         row.append(a[i][j]+b[i][j])
#     result.append(row)

# for row in result :
#     print(" ".join(map(str,row)))

# # 2566.최댓값
# max_num = 0
# row = 1
# column = 1
# for i in range(1, 10):
#     num_list = map(int, input().split())
#     for j, num in enumerate(num_list, 1):
#         if num > max_num:
#             max_num = num
#             row = i
#             column = j

# print(max_num)
# print(row, column)

# # 10798.세로읽기
# words = [input().strip() for _ in range(5)]

# max_length = max(len(word) for word in words)

# result = []
# for i in range(max_length) :
#     for word in words :
#         if i < len(word) :
#             result.append(word[i])
# print("".join(result))

# 2563.색종이
n = int(input())
bg = [[0 for i in range(100)] for j in range(100)]
for _ in range(n) :
    x, y = map(int, input().split())

    for i in range(10) :
        for j in range(10) :
            bg[i+x][j+y] = 1
result = 0
for i in range(100) :
    for j in range(100) :
        result += bg[i][j]

print(result)
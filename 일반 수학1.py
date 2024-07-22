# # 2745.진법 변환
# n, b = input().split()
# b = int(b)

# result = int(n,b)
# print(result)

# # 11005. 진법 변환 2
# n,b = map(int, input().split())
# digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# result = ""
# while n > 0:
#     result = digits[n%b] + result
#     n //= b
# print(result)

# # 2720. 세탁소 사장 동혁
# def change(c) :
#     q = c // 25
#     c %= 25

#     d = c // 10
#     c %= 10
    
#     n = c // 5
#     c %= 5

#     p = c // 1
#     c %= 1
#     return q,d,n,p

# t = int(input())
# for _ in range(t) :
#     c = int(input())
#     q,d,n,p = change(c)
#     print(q,d,n,p)

# # 2903.중앙 이동 알고리즘
# n = int(input())
# result = (2**n+1)**2
# print(result)

# # 2292.벌집
# n = int(input())
# count = 1
# floor = 1

# while n > count :
#     count += 6*floor
#     floor += 1
# print(floor)

# 1193.분수찾기
x = int(input())
line_num = 1
max_num = 1
while max_num < x :
    line_num += 1
    max_num += line_num

start_num = max_num - line_num + 1
n = x - start_num 
if line_num % 2 == 0 :
    numerator = n+1
    denominator = line_num-n
else :
    numerator = line_num-n
    denominator = n+1

print(f'{numerator}/{denominator}')


# # 2869.달팽이는 올라가고 싶다
# a,b,v = map(int,input().split())
# distance = v-b
# climb = a-b

# day = distance // climb
# if distance % climb != 0 :
#     day += 1
# print(day)
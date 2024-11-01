# # 27866.문자와 문자열
# s = str(input())
# i = int(input())
# print(s[i-1])

# # 2743.단어 길이 재기
# n = str(input())
# print(len(n))

# # 9086.문자열
# n = int(input())
# for _ in range(n) :
#     s = str(input())
#     answer = s[0]+s[-1]
#     print(answer)

# # 11654.아스키 코드
# n = input()
# print(ord(n))

# # 2675.문자열 반복
# t = int(input())
# for _ in range(t) :
#     r,s = input().split()
#     r = int(r)
#     answer = ''
#     for i in s :
#         answer += i*r
#     print(answer)

# # 11720.숫자의 합
# n = int(input())
# num = str(input())
# answer = 0
# for i in num :
#     answer += int(i)
# print(answer)

# # 1152.단어의 개수
# s = input().strip()
# answer = len(s.split())
# print(answer)

# # 2908.상수
# a,b = map(str,input().split())
# answer = max(int(a[::-1]),int(b[::-1]))
# print(answer)

# # 5622.다이얼
# dial = {
#     'A':3, 'B':3, 'C':3,
#     'D':4, 'E':4, 'F':4,
#     'G':5, 'H':5, 'I':5,
#     'J':6, 'K':6, 'L':6,
#     'M':7, 'N':7, 'O':7,
#     'P':8, 'Q':8, 'R':8, 'S':8,
#     'T':9, 'U':9, 'V':9,
#     'W':10, 'X':10, 'Y':10, 'Z' :10
# }
# s= input().strip()
# answer = sum(dial[i] for i in s)
# print(answer)

# 11718.그대로 출력하기
import sys
answer = sys.stdin.read()
print(answer, end = '')
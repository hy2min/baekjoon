# a = 5
# b = -1
# c = 2

# print(f"a, b, c 값은 각각 a는 {a}, b는 {b}, c는 {c} 입니다.")

# a = 7
# b = 2
# print(f"a+b={a+b}")
# print(f"a-b={a-b}")

# k = 8
# g = 4

# print(f"{k}*{g}={k*g}")
# print(f"{k}/{g}={k//g}")

# a = 3
# b = 5
# c = 3
# d = 4
# print(((a+b)*c)//d)

# a = 8
# print(a**5)

# a = 8
# a += 1
# a += 1
# a = a + 1
# a = a + 1
# print(a)

# a = 1
# b = 2
# c = 3
# d = 4
# sum = a + b + c + d

# print(sum)

# q = 1
# w = 2
# e = 3
# print(f"#q={q},{q},{q}")
# print(f"#w={w},{w},{w}")
# print(f"#e={e},{e},{e}")

# a = 10
# print(f"a의 값은 {a}입니다")

# bbq = 5
# print(f"bbq의 값은 {bbq}입니다")

# a = 40
# b = 60
# c = 10
# g = a + c
# h = b - c
# print(g)
# print(h)

# a = 10
# b = 3
# print(f"{a} * {b} = {a*b}")
# print(f"{a} / {b} = {a//b}")

# a = 3
# b = 2
# c = 6
# d = 2
# print((a+b)*(c//d))

# a = 3
# b = 3
# c = 8
# d = 3
# print((a*b)+(c*d))

# a, b, c = map(int, input().split())
# print(f"{a}{a}{a}")
# print(f"{b}{b}{b}")
# print(f"{c}{c}{c}")

# a, b = map(int, input().split())
# if a > b:
#     print(f"{a}{a}{a}{a}")
# elif a < b:
#     print(f"{b}{b}{b}{b}")

# a = int(input())
# print(f"{a} 입력함")
# a += 1
# print(f"a++을 수행하면 {a}이 됩니다")

# input = int(input())
# if input > 3:
#     input += 1
#     print(input)
# else:
#     input -= 1
#     print(input)

# num = int(input())
# if num > 0:
#     print("###")
#     print("###")
#     print("###")
# elif num < 0:
#     print("$$$")
#     print("$$$")

# a, b, c = map(int, input().split())
# if (a+b+c) >= (a*b*c):
#     print("행운의 수")
# else:
#     print("소소한 수")

# print("WWW.\"MIN\"CODING.CO.KR")

# a, b = map(int, input().split())
# if a == b:
#     print("같습니다")
# else:
#     print("다릅니다")

# a, b, c = map(int, input().split())
# print(f"첫번째 숫자는 {a} 입니다.")
# print(f"두번째 숫자는 {b} 입니다.")
# print(f"세번째 숫자는 {c} 입니다.")

# a, b, c, d = map(int, input().split())
# print(f"a + b = {a + b}")
# print(f"c + d = {c + d}")
# print(f"ALL SUM = {a + b + c + d}")

# a, b, c = map(int, input().split())
# if a == b == c:
#     print("만세")

# b = list(map(int, input().split()))
# if max(b) == b[0]:
#     print("b1이 가장 크다")

# nums = list(map(int, input().split()))
# avg = sum(nums)//len(nums)
# for n in nums:
#     if n > avg:
#         print(f"{n}>{avg}")
#     elif n < avg:
#         print(f"{n}<{avg}")
#     else:
#         print(f"{n}=={avg}")

# a, b = map(int, input().split())
# if abs(a-b) > 5:
#     print("멀다")
# else:
#     print("가깝다")

# a, b = map(int, input().split())
# if (a + b) > 10:
#     print("합만세")
# if (a * b) > 10:
#     print("곱만세")

# nums = list(map(int, input().split()))
# print(f"{nums[3]} {nums[4]} {nums[5]} {nums[6]}")

# for i in range(10):
#     print("#", end="")

# n = int(input())
# if n == 5 or n == 10:
#     print("만세")
# else:
#     print("재도전")

# a, b = map(int, input().split())
# if a == 7 and b == 9:
#     print("인증됨")
# else:
#     print("재시도")

# for i in range(3, 11):
#     print(i)

# a, b = map(int, input().split())
# for i in range(a, b+1):
#     print(i)

# for i in range(25):
#     print("PIZZAHOT")

# for i in range(10, 0, -1):
#     print(i, end=" ")

# n = int(input())
# if (n * 2 + 20) // 5 != 100:
#     print("Magic")

# a, b = map(int, input().split())
# for i in range(a, b + 1):
#     print(i, end="")

# n = int(input())

# for i in range(n+1):
#     print(i)

# a, b, c = map(int, input().split())

# if (a + b + c) > 10:
#     print(a * b * c)
# else:
#     print(0)

# n = int(input())
# for i in range(n, -1, -1):
#     print(i)
# print("발사")

# for i in range(-5, 6):
#     print(i, end=" ")

# n = int(input())
# for i in range(n, n+3):
#     print(str(i)*3)

# a, b, c = map(int, input().split())
# if a >= b and a >= c:
#     print("MAX발견")
# else:
#     print("MAX아님")

# a, b = map(int, input().split())
# if 30 < (a * b) < 50:
#     print("적당한 사이즈")
# elif (a * b) >= 50:
#     print("큰 사이즈")
# else:
#     print("작은 사이즈")
# a, x = map(int, input().split())
# for i in range(a-1, a - x - 1, -1):
#     print(i)

# a, b, c = map(int, input().split())

# for i in range(a, b+1):
#     print(i, end=" ")
# print("")
# for j in range(a, c+1):
#     print(j, end=" ")

# for i in range(6, 2, -1):
#     print(str(i+3) + " " + str(i))

# n = int(input())
# for i in range(1, 2 * n, 2):
#     print(i, end=" ")

# print("시작")
# for i in range(1,6):
#     print(i, end="")
# print("")
# print("종료")

# n = int(input())
# for i in range(n):
#     print("##\n@@")

# for i in range(1,6):
#     print(f"{i}번go!!")

# id, pw = map(int, input().split())
# if id == 1111 and pw ==2222:
#     print("로그인성공")
# elif id == 1111:
#     print("비밀번호가 틀렸습니다")
# elif pw == 2222:
#     print("아이디가 틀렸습니다")

# n = int(input())
# for i in range(n, -1, -1):
#     print(i, end="")

# nums = list(map(int, input().split()))

# for i in nums:
#     print(i, end=" ")

# arr = [4, 1, 3, 6, 9]
# n = int(input())
# print(f"{n}번index의값은{arr[n]}입니다")

# arr = list(map(int, input().split()))
# print(arr[0]+arr[-1])

# n = int(input())
# n += 5
# for i in range(5):
#     print(n, end=" ")

# arr = [3, 4, 1, 6, 7, 5]
# a, b = map(int, input().split())
# print(arr[a] + arr[b])

# arr = [3, 1, 2, 5]
# i = int(input())
# if arr[i] > 2:
#     print("우와")
# else:
#     print("ㅠㅠ")

# arr = [3, 9, 27, 81, 243]
# index = int(input())
# print(arr[index]-100)

# n = int(input())
# if n > 5:
#     for i in range(1, 11):
#         print(i)
# else:
#     for i in range(5, 0, -1):
#         print(i)

# arr = [5, 2, 3, 4, 7]
# for i in arr[::-1]:
#     print(i, end=" ")

# arr = [0] * 6
# num = int(input())
# for i in range(6):
#     arr[i] = num -i
# print(arr[2])

# arr = list(map(int, input().split()))
# answer = 0
# for i in arr:
#     answer += i
# print(answer)

# arr = [5, 25, 54, 2, -33, 57, 82, -8, 13, 1]
# index = int(input())
# for i in range(index,len(arr)):
#     print(arr[i])

# arr = [3, 2, 6, 7, 1, 8]
# index = int(input())
# print(arr[index])

# arr = [0] * 5
# n = int(input())
# for i in range(5):
#     arr[i] = n
# for i in arr:
#     print(i, end="")

# arr = [1, 7, 3, 2, 6]
# for i in arr:
#     print(i, end="")

# arr = [5, 7, 1, 8, -4, -73, 4, 2, 20, 84]
# n = int(input())
# for i in range(n, -1, -1):
#     print(arr[i])
# arr = [0] * 6
# n = int(input())
# for i in range(6):
#     arr[i] = n + i
# for i in arr:
#     print(i)

# arr = [0] * 4
# a, b = map(int, input().split())
# arr[0] = a
# arr[2] = b
# for i in arr:
#     print(i, end="")

# string = input()
# print(string*3)

# arr = []
# arr = list(map(int, input().split()))
# answer = 0
# for i in arr:
#     answer += i
# print(answer)

# arr = list(map(int, input().split()))
# index = 0
# while index < 6:
#     if arr[index] == 7:
#         break
#     print(arr[index], end=" ")
#     index += 1

# arr = list(map(int, input().split()))
# index = 5
# while index >= 0:
#     print(arr[index], end=" ")
#     if arr[index] == 7:
#         break
#     index -= 1

# arr = [3, 4, 1, 6, 7, 5]

# i = 0
# while i < len(arr):
#     print(arr[i], end=" ")
#     i += 1

# array = [[0] * 4 for _ in range(3)]

# def input1():
#     global array
#     n = int(input())
#     for i in range(3):
#         for j in range(4):
#             array[i][j] = n
#             n += 1

# def process():
#     global array
#     for i in range(3):
#         for j in range(4):
#             array[i][j] += 1

# def output():
#     global array
#     for i in array:
#         for j in i:
#             print(j, end=" ")
#         print("")

# input1()
# process()
# output()

# arr1 = ["B", "D", 5, "Q", "A"]
# arr2 = ["Q", "E", "R", "E", "F"]

# def input1():
#     global string
#     string = input()

# def output():
#     if string.islower():
#         for i in arr1:
#             print(i, end="")
#     elif string.isupper():
#         for i in arr2:
#             print(i, end="")
#     elif string.isdigit():
#         for i in range(72, 64, -1):
#             print(chr(i), end="")

# input1()
# output()

# arr = ["#", "_", "#", "_", "#", "#"]
# for i in arr:
#     if i == "#":
#         print("샵", end="")
#     elif i == "_":
#         print("무", end="")
# arr = [[0] * 3 for _ in range(2)]

# def input1():
#     nums = list(map(int, input().split()))
#     index = 0
#     for i in range(2):
#         for j in range(3):
#             arr[i][j] = nums[index]
#             index += 1

# def process():
#     global total
#     total = 0
#     for i in arr:
#         for j in i:
#             total += j

# def output():
#     print(total)

# input1()
# process()
# output()

# arr = [[4, 3, 1, 1], [3, 1, 2, 1], [0, 0, 1, 2]]
# n = int(input())
# cnt = 0
# for i in arr:
#     for j in i:
#         if j == n:
#             cnt += 1

# print(f"{cnt}개 존재합니다")


# price = int(input())

# def starBox():
#     for i in range(1,20,2):
#         print(i, end=" ")

# def macDoll():
#     for i in range(72, 64, -1):
#         print(chr(i), end=" ")

# def copyBean():
#     for i in range(-5, 6):
#         print(i, end=" ")

# if 3500 <= price <= 5000:
#     starBox()
# elif 2500 <= price < 3500:
#     macDoll()
# else:
#     copyBean()

# # 11-9
# arr = input().split()
# big = [""]*8
# small = [""]*8

# for i in arr:
#     if i.isupper():
#         big.append(i)
#     elif i.islower():
#         small.append(i)

# print(f'big={"".join(big)}')
# print(f'small={"".join(small)}')

# # 11-10
# arrays = [
#     [3, 2, 6, 2, 4],
#     [1, 4, 2, 6, 5],
# ]

# def KFC(n):
#     for arr in arrays:
#         if n in arr:
#             return 1
#         else:
#             return 0

# target = int(input())
# if KFC(target) == 1:
#     print("값이 존재합니다")
# elif KFC(target) == 0:
#     print("값이 없습니다")

# # 11-11
# arrays = [
#     [1, 3, 6, 2],
#     [4, 2, 4, 5],
#     [6, 3, 7, 3],
#     [1, 5, 4, 6],
# ]
# stack = []
# n = int(input())
# for i in arrays:
#     for j in i:
#         if n < j :
#             stack.append(j)
# print(" ".join(map(str,stack)))

# # 11.5-1
# arr = ["D", "F", "G", "D", "A", "Q"]
# ch1, ch2 = map(str, input().split())

# for i in arr:
#     if ch1 <= i <= ch2:
#         print("발견!!!")
#         break

# else: print("미발견!!!")

# # 11.5-2
# arr = [
#     [1, 1, 1],
#     [1, 2, 1],
#     [3, 6, 3],
# ]
# def Count(n):
#     cnt = 0
#     for i in arr:
#         for j in i:
#             if n == j:
#                 cnt += 1
#     return cnt


# n = int(input())
# cnt = Count(n)
# print(cnt)

# # 11.5-3
# arr = ["A", "1", "1", "1", "5", "A", "w", "z"]
# s  = input()
# cnt = 0
# for i in arr:
#     if s == i:
#         cnt+=1
# if cnt >= 3:
#     print("THREE")
# elif cnt == 2:
#     print("TWO")
# elif cnt == 1:
#     print("ONE")
# else:
#     print("NOTHING")

# # 11.5-4
# arr = [
#     ["a", "b", "a", "c", "z"],
#     ["c", "t", "a", "c", "d"],
#     ["c", "c", "c", "c", "a"],
# ]
# s = input()
# cnt = 0
# for i in arr:
#     for j in i:
#         if s == j:
#             cnt += 1
# if cnt >= 7:
#     print("세상에")
# elif cnt >= 5:
#     print("와우")
# elif cnt >= 3:
#     print("이야")
# else:
#     print("이런")

# # 11.5-5
# nums = list(map(int, input().split()))
# for i in range(2):
#     arr = []
#     for j in range(3):
#         num = nums[i*(2+1) +j]
#         arr.append("#" if num == 0 else str(num))
#     print("".join(arr))

# # 11.5-6
# arr = [
#     ["a","b","E"],
#     ["E","2","W"],
#     ["3","2","4"]
# ]
# for i in arr:
#     for j in i:
#         if j.isupper():
#             print(j.lower(), end=" ")
#         elif j.islower():
#             print(j.upper(), end=" ")
#         elif j.isdecimal():
#             print(int(j) + 5, end=" ")
#     print()

# # 11.5-7
# arr = [
#     ["a","b","d"],
#     ["e","w","z"],
#     ["q","v","a"],
# ]
# def input1():
#     s = input()
#     return s
# def Process(s):
#     if s.isupper():
#         s = s.lower()
#     for i in arr:
#         if s in i:
#             print("존재")
#             break
#     else:
#         print("없음")

# num = input1()
# Process(num)

# # 11.5-8
# a, b, c = map(int, input().split())
# arr = [
#     [3, 1, 6],
#     [7, 8, 4],
#     [9, 2, 3],
# ]
# arr[a][b] = c
# max_num = 0
# min_num = 2e18
# for i in arr:
#     if max_num < max(i):
#         max_num = max(i)
#     if min_num > min(i):
#         min_num = min(i)
# print(max_num + min_num)

# # 11.5-9
# arr = [[0]*3 for _ in range(2)]
# nums = list(map(int, input().split()))
# index = 0
# for i in range(2):
#     for j in range(3):
#         arr[1-i][2-j] = nums[index]
#         index += 1

# arr2 = []
# for i in arr:
#     for j in i:
#         arr2.append(j)
# temp = 0
# temp = arr2[0]
# arr2[0] = arr2[5]
# arr2[5] = temp

# print(" ".join(map(str,arr2)))

# # 12-1
# s = input()
# for _ in range(5):
#     print(s)

# # 12-2
# chr1 = input()
# chr2 = input()
# length1 = 0
# length2 = 0

# for char in chr1:
#     length1 += 1
# for char in chr2:
#     length2 += 1

# print(length1, length2)
# # print(len(chr1), len(chr2))

# # 12-3
# n = int(input())
# for _ in range(4):
#     for _ in range(4):
#         print(n, end="")
#     print()
#     n -= 1

# # 12-4
# n = int(input())
# for _ in range(n):
#     for i in range(3):
#         print(i+1, end="")
#     print()

# # 12-5
# n = int(input())
# arr = [[0]*4 for _ in range(3)]

# for i in range(3):
#     for j in range(2+i):
#         arr[i][2-i+j] = n
#         n += 1

# for i in arr:
#     for j in i:
#         if j == 0:
#             print(" ", end="")
#         else:
#             print(j, end="")
#     print()

# # 12-6
# arr = ['M', 'I', 'N', 'Q', 'U', 'E', 'S', 'T']
# def Length(s):
#     return arr.index(s)

# for _ in range(3):
#     s = input()
#     print(f'{s}={Length(s)}')

# # 12-7
# while True:
#     s = input()
#     if len(s) <= 10:
#         break
# for _ in range(3):
#     char = input()
#     cnt = s.count(char)
#     print(f'{char}={cnt}')

# # 12-8
# arr = ['D','A','T','A','P','O','W','E','R']
# a, b = map(int, input().split())
# arr2 = []
# arr2 = arr[a:b+1]
# print("".join(arr2))

# # 12-9
# arr = [[0] * 3 for _ in range(3)]
# s = input()
# n = 1

# if s.isdecimal():
#     for i in range(3):
#         for j in range(i+1):
#             arr[2-i][2-j] = n
#             n += 1
# elif s.isupper():
#     for i in range(3):
#         for j in range(3-i):
#             arr[2-i][j] = n
#             n += 1

# for i in arr:
#     for j in i:
#         if j == 0:
#             print(" ", end="")
#         else:
#             print(j, end="")
#     print()

# # 12-10
# n, s = map(str, input().split())
# char = ord(s)
# arr = [[0] *5 for _ in range(5)]
# for i in range(5):
#     arr[int(n)-1][4-i] = chr(char)
#     char += 1
# for i in arr:
#     for j in i:
#         print(j, end="")
#     print()

# # 12.5-3
# arr = [
#     ['D','A','D'],
#     ['Q','W','Q'],
#     ['A','S','D'],
#     ['A','S','D'],
# ]

# def find(s):
#     for i in arr:
#         for j in i:
#             if s == j:
#                 print("존재")
#                 return
#     print("없음")

# s = input()
# find(s)

# # 12.5-4
# arr = [[0] * 5 for _ in range(5)]
# n = int(input())
# for i in range(5):
#     for j in range(5):
#         if i == 0 or i == 4 or j == 0 or j == 4:
#             arr[i][j] = n
#         else:
#             arr[i][j] = '_'

# for i in arr:
#     for j in i:
#         print(j, end="")
#     print()

# # 12.5-5
# arr = [
#     [4, 5, 4, 5, 4],
#     [8, 9, 8, 9, 8],
#     [1, 2, 1, 2, 1],
#     [4, 5, 4, 5, 4],
#     [6, 7, 6, 7, 6],
# ]
# for _ in range(5):
#     y, x = map(int, input().split())
#     if arr[y][x] == 9:
#         arr[y][x] = 0
#     else:
#         arr[y][x] += 1

# for i in arr:
#     for j in i:
#         print(j, end="")
#     print()

# # 12.5-6
# s = input()
# print(len(s))
# cnt = 0
# for i in s:
#     if i == s[-1]:
#         cnt += 1
# print(cnt)

# # 12.5-7
# strings = []
# for _ in range(3):
#     s = input()
#     strings.append(s)

# lengths = [len(s) for s in strings]
# max_length = max(lengths)

# answer = strings[lengths.index(max_length)]
# print(answer)

# # 12.5-8
# arr = [[0] * 3 for _ in range(3)]
# n = int(input())
# if n == 1:
#     start = 1
#     for i in range(3):
#         for j in range(i+1):
#             arr[i][j+2-i] = start
#             start += 1
# else:
#     start = n
#     for i in range(3):
#         for j in range(i+1):
#             arr[i][j+2-i] = start
#             start += 1

# for i in arr:
#     for j in i:
#         print(j, end= "")
#     print()

# # 13-1
# str1, str2 = map(str, input().split())
# def getName(a, b):
#     if a < b:
#         print(a)
#     else:
#         print(b)
# getName(str1, str2)

# # 13-2
# def moom(n):
#     a = n - 4
#     b = n + 3
#     c = n * 2
#     return a, b, c

# age = int(input())
# answer = moom(age)
# print(" ".join(map(str,answer)))

# # 13-3
# def stringLen(lengths):
#     cnt = 0
#     for length in lengths:
#         cnt += 1
#     return cnt


# s = input()
# answer = stringLen(s)
# print(f'{answer}글자')

# # 13-4
# a, b = map(int, input().split())
# def ABC(a, b):
#     SUM = a + b
#     GOP = a * b
#     return SUM ,GOP

# SUM, GOP = ABC(a, b)

# print(SUM, GOP)

# # 13-5
# def KFC():
#     while True:
#         s = input()
#         if len(s) <= 10:
#             break
#     upper_count = 0
#     lower_count = 0
#     for i in s:
#         if i.isupper():
#             upper_count += 1
#         elif i.islower():
#             lower_count += 1
#     return upper_count, lower_count

# upper_count, lower_count = KFC()
# print(f'대문자{upper_count}개\n소문자{lower_count}개')

# # 13-6
# arr = [
#     [4, 5, 6, 1, 3, 1],
#     [2, 1, 3, 6, 3, 6],
# ]

# def Input():
#     a, b, c = map(int, input().split())
#     return a, b, c
# def Process(a, b, c):
#     cnt_a = 0
#     cnt_b = 0
#     cnt_c = 0
#     for i in arr:
#         for j in i:
#             if a == j:
#                 cnt_a += 1
#             if b == j:
#                 cnt_b += 1
#             if c == j:
#                 cnt_c += 1
#     return cnt_a, cnt_b, cnt_c
# def Output(a, b, c, cnt_a, cnt_b, cnt_c):
#     print(f'{a}={cnt_a}개')
#     print(f'{b}={cnt_b}개')
#     print(f'{c}={cnt_c}개')

# a, b, c = Input()
# cnt_a, cnt_b, cnt_c = Process(a, b, c)
# Output(a, b, c, cnt_a, cnt_b, cnt_c)

# # 13-7
# arr = [
#     ['A','D','F'],
#     ['Q','W','E'],
#     ['Z','X','C'],
# ]

# def find(s):
#     for i in range(3):
#         for j in range(3):
#             if arr[i][j] == s:
#                 return i, j

# s = input()
# i, j = find(s)
# print(f'{i},{j}')

# # 13-8
# arr = [3, 5, 1, 2, 7]
# arr2 = list(map(int, input().split()))

# def CompareGo(arr, arr2):
#     if arr == arr2:
#         print("두배열은완전같음")
#     else:
#         print("두배열은같지않음")

# CompareGo(arr, arr2)

# # 13.5-2
# distance = {
#     'A' : 4,
#     'B' : 2,
#     'C' : 5,
#     'D' : 1,
#     'E' : 6,
#     'F' : 7,
#     'G' : 3,
# }

# start, end = input().split()
# keys = list(distance.keys())
# start_index = keys.index(start)
# end_index = keys.index(end)

# if start_index > end_index:
#     start_index, end_index = end_index, start_index

# total = 0
# for i in range(start_index + 1, end_index):
#     total += distance[keys[i]]
# print(total)

# # 13.5-3
# arr1 = list(map(int, input().split()))
# arr2 = list(map(int, input().split()))
# arr3 = list(map(int, input().split()))
# for i in range(5):
#     mp = arr1[i] * arr2[i] + arr3[i]
#     print(mp, end=" ")

# # 13.5-4
# arr = [
#     [3, 4, 1, 6],
#     [3, 5, 3, 6],
#     [0, 0, 0, 0],
#     [5, 4, 6, 0],
# ]
# arr[2] = list(map(int, input().split()))
# max_num = 0
# min_num = 2e18
# max_index = (-1, -1)
# min_index = (-1, -1)

# for i in range(4):
#     for j in range(4):
#         if arr[i][j] > max_num:
#             max_num = arr[i][j]
#             max_index = (i, j)
#         if arr[i][j] < min_num:
#             min_num = arr[i][j]
#             min_index = (i,j)

# print(f'MAX={max_num}({max_index[0]},{max_index[1]})')
# print(f'MIN={min_num}({min_index[0]},{min_index[1]})')

# # 13.5-5
# arr = [
#     ['4','5','7','1','3','2'],
#     ['D','F','Q','W','G','Z'],
# ]
# n = int(input())
# for i in range(len(arr[0])):
#     if arr[0][i] == str(n):
#         print(arr[1][i])

# # 13.5-6
# str1 = input()
# str2 = input()
# def FindABC(str1, str2):
#     cnt_a = 0
#     cnt_b = 0
#     cnt_c = 0
#     for i in str1:
#         if i == "A":
#             cnt_a += 1
#         if i == "B":
#             cnt_b += 1
#         if i == "C":
#             cnt_c += 1
#     for i in str2:
#         if i == "A":
#             cnt_a += 1
#         if i == "B":
#             cnt_b += 1
#         if i == "C":
#             cnt_c += 1
#     return cnt_a, cnt_b, cnt_c

# a, b, c = FindABC(str1,str2)
# print(f'A:{a}\nB:{b}\nC:{c}')

# # 13.5-7
# arr = [
#     ['D','A','S'],
#     ['Q','W','V'],
#     ['R','T','Y'],
# ]
# y1, x1 = map(int, input().split())
# y2, x2 = map(int, input().split())
# def Find(y1, x1, y2, x2):
#     print(arr[y1][x1], arr[y2][x2])
# Find(y1, x1, y2, x2)

# # 13.5-8
# name_list = []
# for _ in range(3):
#     while True:
#         name = input()
#         if len(name) < 10:
#             name_list.append(name)
#             break

# if name_list[0] == name_list[1] == name_list[2]:
#     print("YES")
# else:
#     print("NO")

# a, b = map(int, input().split())
# n = a
# while a <= n <= b:
#     print(n, end=" ")
#     n += 1

# # 14-2
# apartment = []
# for _ in range(5):
#     row = list(map(int, input().split()))
#     apartment.append(row)

# for i in range(5):
#     total = 0
#     for j in range(4):
#         total += apartment[i][j]
#     print(total, end=" ")

# # 14-3
# a, b = map(int, input().split())
# cnt = 0
# while a <100 or b < 100:
#     if a < 100:
#         a += 1
#     if b < 100:
#         b += 1
#     cnt += 1
# print(cnt)

# # 14-4
# arr = list(input().split())
# for i in range(5):
#     for j in range(i,5):
#         print(arr[j], end=" ")
#     print()

# arr = []
# for _ in range(3):
#     row = list(map(int, input().split()))
#     arr.append(row)

# sauce = 0
# for i in range(3):
#     for j in range(i+1):
#         sauce += arr[i][j]
# print(sauce)

# # 14-6
# vect = [3, 5, 1, 1, 2, 3, 2]
# arr = list(map(int, input().split()))

# for i in arr:
#     cnt = 0
#     for j in vect:
#         if i ==j:
#             cnt += 1
#     print(f'{i}={cnt}개')

# # 14-7
# arr = list(map(int, input().split()))
# for i in range(6):
#     for j in range(i+1, 6):
#         if arr[i] < arr[j]:
#             arr[i], arr[j] = arr[j], arr[i]

# print("".join(map(str,arr)))

# # arr.sort(reverse=True)
# # print("".join(map(str,arr)))

# # 14-8
# s = input()
# s = list(s)
# for i in range(len(s)):
#     for j in range(i+1, len(s)):
#         if s[i] > s[j]:
#             s[i], s[j] = s[j], s[i]
# print("".join(s))

# # 14-9
# arr = [10, 50, 40, 20, 30, 40]
# arr2 = list(map(int, input().split()))
# for i in arr2:
#     cnt = 0
#     for j in arr:
#         if i < j :
#             cnt +=1
#     print(f'{i}={cnt}개')

# # 14.5-1
# char1, char2 = input().split()
# temp = 0
# temp = char1
# char1 = char2
# char2 = temp

# print(char1, char2)

# # 14.5-2
# n = int(input())
# arr = []
# for _ in range(5):
#     row = list(map(int, input().split()))
#     arr.append(row)

# if n == 1:
#     for i in range(5):
#         for j in range(i+1):
#             print(arr[i][j], end=" ")
#         print()
# if n == 2:
#     for i in range(5):
#         for j in range(5-i):
#             print(arr[i][j], end=" ")
#         print()

# n = int(input())
# i = 0
# while i < 3:
#     j = 0
#     while j < 5:
#         print(n, end="")
#         j += 1
#     print()
#     i += 1

# # 14.5-5
# all_char = []
# for _ in range(2):
#     s = input()
#     s = sorted(s)
#     all_char.extend(s)
# print("".join(all_char))

# # 14.5-6
# arr = [[0] * 3 for _ in range(3)]

# def magic():
#     start = 1
#     for i in range(3):
#         for j in range(i, 3):
#             arr[i][j] = start
#             start += 1
#     return arr

# def output(arr):
#     for i in arr:
#         for j in i:
#             if j == 0:
#                 print(" ", end="")
#             else:
#                 print(j, end="")
#         print()

# m = magic()
# output(m)


# # 15-1
# s1 = input()
# s2 = input()

# if len(s1) != len(s2):
#     print("다름")
# else:
#     for chr1, chr2 in zip(s1, s2):
#         if chr1 != chr2:
#             print("다름")
#             break
#     else:
#         print("같음")

# # 15-2
# while True:
#     n = int(input())
#     if 1000 <= n <= 9999:
#         break

# a = n // 1000
# b = (n % 1000) // 100
# c = (n % 100) // 10
# d = n % 10

# for i in (a, b, c, d):
#     print(f'숫자{i}')

# # 15-3
# scores = list(map(int, input().split()))
# i = 0
# while i < 5:
#     if abs(scores[i]-scores[i+1]) > 3:
#         print("재배치필요")
#         break
#     i += 1
# else:
#     print("완벽한배치")

# # 15-4
# while True:
#     s1 = input()
#     s2 = input()
#     if len(s1) <= 10 and len(s2) <= 10:
#         break

# t = len(s1) - 1
# for i in range(len(s1)):
#     if s1[i] != s2[t]:
#         print("거울문장아님")
#         break
#     t -= 1
# else:
#     print("거울문장")
# # if s1[::-1] == s2:
# #     print("거울문장")
# # else:
# #     print("거울문장아님")

# # 15-5
# length = []
# arr = []

# for _ in range(4):
#     row = input()
#     if len(row) > 6:
#         continue
#     arr.append(list(row))
#     # length.append(len(row))

# for i in arr:
#     cnt = 0
#     for j in i:
#         cnt += 1
#     length.append(cnt)
# length.sort()

# print(" ".join(map(str,length)))

# # 15-6
# while True:
#     s = input()
#     if len(s) <= 10:
#         break

# flag = True

# for i in range(1, len(s)):
#     if i % 2 == 0:
#         if not s[i].isupper():
#             flag = False
#             break
#     else:
#         if not s[i].islower():
#             flag = False
#             break

# if flag == True:
#     print("개구리문장")
# else:
#     print("일반문장")

# # 15-7
# arr = ['A', 'B', 'C', 'Z', 'E', 'T', 'Q']
# black_list = list(input())
# for i in black_list:
#     if i in arr:
#         print(f'{i}=마을사람')
#     else:
#         print(f'{i}=외부사람')

# # 15-8
# sentences = []

# for _ in range(5):
#     s = input()
#     if len(s) <= 10:
#         sentences.append(s)

# max_length = max(sentences, key=len)
# print(max_length)

# # 15-9
# sentence1 = "BBQWORLD"
# sentence2 = "KFCAPPLE"
# sentence3 = "LOT"

# s = input()
# cnt = sentence1.count(s) + sentence2.count(s) + sentence3.count(s)
# print(cnt)

# # 15-10
# def CountLine(s):
#     for i in s:
#         print(f'{len(i)}={"".join(i)}')

# arr = []
# for _ in range(3):
#     row = input()
#     if len(row) <=10:
#         arr.append(list(row))

# CountLine(arr)

# # 15-11
# arr = []
# for _ in range(4):
#     s = input()
#     if len(s) <= 5:
#         arr.append(list(s))

# check_a = False
# check_b = False
# for i in arr:
#     if 'A' in i:
#         check_a = True
#     if 'B' in i:
#         check_b = True

# if check_a and check_b:
#     print("대발견")
# elif check_a or check_b:
#     print("중발견")
# else:
#     print("미발견")

# # 15-12
# arr = []
# for _ in range(2):
#     s = input()
#     if len(s) <= 5:
#         arr.append(list(s))

# char_arr = [' '] * 12
# index = 0
# for i in arr:
#     for j in i:
#         char_arr[index] = j
#         index += 1

# print("".join(char_arr))

# # 15-13
# arr = [
#     ['D', 'A', 'T', 'A', 'W', ''],
#     ['B', 'B', 'Q', 'K', '', ''],
#     ]
# n = int(input())
# if n % 2 == 1:
#     arr[0].sort()
# else:
#     arr[1].sort()

# for i in arr:
#     for j in i:
#         print(j, end="")
#     print()

# # 15-14
# arr = [
#     ['P','O','T','I','O',''],
#     ['A','B','C','D','E',''],
#     ['Y','O','U','R','E',''],
# ]
# a, b = map(int, input().split())
# for i in range(len(arr)):
#     for j in range(a, b+1):
#         print(arr[i][j], end="")

# # 15-15
# arr = []
# for _ in range(2):
#     s = list(input())
#     if len(s) <= 8:
#         arr.append(s)

# min_length = min(len(arr[0]), len(arr[1]))
# cnt = abs(len(arr[0])-len(arr[1]))
# for i in range(min_length):
#     if arr[0][i] != arr[1][i]:
#         cnt += 1
# print(cnt)

# # 15-16
# s = input()
# arr =[[' '] * 3 for _ in range(3)]
# current_s = ord(s)
# i, j = 0, 0
# while i < 3:
#     while j < i +1:
#         arr[2-i][j] = chr(current_s)
#         current_s += 1
#         j += 1
#     i += 1
#     j = 0

# for i in arr:
#     for j in i:
#         print(j,end="")
#     print()

# # +1
# print("HELLO WORLD")

# # +2
# arr = [
#     [5, 1, 4, 2, 6],
#     [3, 5, 0, 0, 7],
#     [9, 9, 8, 3, 1],
# ]
# n = int(input())
# cnt = 0
# for i in arr:
#     for j in i:
#         if j > n:
#             cnt += 1
# print(f'{cnt}개')

# # +3
# arr = [[0] * 4 for _ in range(3)]
# index = 1
# for i in range(3):
#     for j in range(4):
#         arr[2-i][3-j] = index
#         index += 1

# n = int(input())
# for i in range(4):
#     if n == 1:
#         arr[0][i] = 7
#     elif n == 2:
#         arr[1][i] = 7
#     elif n == 3:
#         arr[2][i] = 7

# for i in arr:
#     for j in i:
#         print(j, end=" ")
#     print()

# # +4
# juso = [402, 401, 302, 301, 202, 201, 102, 101]
# name = [
#     ['K','I','M','',''],
#     ['T','E','A','',''],
#     ['S','O','M','',''],
#     ['O','P','P','O',''],
#     ['T','O','M','',''],
#     ['G','D','K','',''],
#     ['J','A','M','E',''],
#     ['M','I','N','',''],
# ]

# n = int(input())
# index = juso.index(n)
# find_name = name[index]
# print(''.join(find_name))

# # +5
# a, b, c = map(int, input().split())
# for _ in range(c):
#     for i in range(a, a+b):
#         print(i, end=" ")
#     print()

# # +6
# arr = [0] * 9
# for _ in range(3):
#     start_index, end_index = map(int,input().split())
#     for i in range(start_index, end_index + 1):
#         arr[i] += 1
# print(" ".join(map(str, arr)))

# # +8
# strings = list(input().split())
# print(max(strings))

# # +9
# arr = []
# for _ in range(2):
#     row = list(map(int, input().split()))
#     arr.append(row)
# sorted_arr = [num for row in arr for num in row]
# for i in range(6):
#     min_index = i
#     for j in range(i+1, 6):
#         if sorted_arr[j] < sorted_arr[min_index]:
#             min_index = j
#     sorted_arr[i], sorted_arr[min_index] = sorted_arr[min_index], sorted_arr[i]
# index = 0
# for i in range(2):
#     for j in range(3):
#         print(sorted_arr[index], end=" ")
#         index +=1
#     print()

# # +10
# arr = [
#     ['F','R','Q','W','T'],
#     ['G','A','S','Y','Q'],
#     ['A','S','A','D','B'],
# ]

# while True:
#     n = int(input())
#     if 0 <= n <= 4:
#         break
# for i in range(3):
#     print(arr[i][n], end="")

# # +11
# arr = ['A','P','P','L','E','T']
# alp_list = input().split()

# cnt = 0
# for alp in alp_list:
#     for i in arr:
#         if alp == i:
#             cnt += 1
# print(f'{cnt}개 맞추었습니다')

arr = [[0] * 4 for _ in range(4)]
n = int(input())

for i in range(4):
    for j in range(4):
        if i % 2 == 0:
            arr[i][j] = n
            n += 1
        else:
            arr[i][3-j] = n
            n += 1
            
for i in arr:
    for j in i:
        print(j, end=" ")
    print()
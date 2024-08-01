# # 2750.수 정렬하기
# n = int(input())
# numbers = []
# for _ in range(n) :
#     numbers.append(int(input()))

# for i in range(n) :
#     for j in range(n-i-1) :
#         if numbers[j] > numbers[j+1] :
#             numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
# for num in numbers :
#     print(num)

# # 2587.대표값2
# nums = []
# for _ in range(5) :
#     nums.append(int(input()))
# average = sum(nums)//5
# nums.sort()
# mid = nums[2]
# print(average, mid)

# # 25305.커트라인
# n,k = map(int,input().split())
# score = list(map(int,input().split()))
# score.sort(reverse=True)
# print(score[k-1])

# # 2751.수 정렬하기 2
# import sys

# n = int(input())
# numbers = []
# for _ in range(n) :
#     numbers.append(int(sys.stdin.readline()))
# numbers.sort()
# for i in numbers :
#     print(i)

# # 수 정렬하기 3
# import sys
# n = int(input())
# nums = []
# for _ in range(n) :
#     nums.append(int(sys.stdin.readline()))

# # 최대값 설정
# max_val = max(nums)

# # 카운트 배열 초기화
# count = [0] * (max_val + 1)

# # 각 숫자의 빈도 계산
# for num in nums:
#     count[num] += 1

# # 정렬된 결과 출력
# for num in range(max_val + 1):
#     for _ in range(count[num]):
#         print(num)

# # 1427.소트인사이드
# n = int(input())
# num = []
# for i in str(n) :
#     num.append(int(i))
# num.sort(reverse=True)
# answer = "".join(map(str,num))
# print(answer)

# # 11650.좌표 정렬하기
# import sys
# n = int(input())
# lists = []
# for _ in range(n) :
#     x, y = map(int,sys.stdin.readline().split())
#     lists.append((x,y))
# lists.sort()

# for i in lists:
#     print(i[0],i[1])

# # 11651.좌표 정렬하기 2
# import sys
# n = int(input())
# lists = []
# for _ in range(n) :
#     x,y = map(int,sys.stdin.readline().split())
#     lists.append((x,y))
# lists.sort(key=lambda i: (i[1], i[0]))
# for i in lists :
#     print(i[0],i[1])

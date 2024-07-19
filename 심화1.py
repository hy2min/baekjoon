# # 25083.새싹
# print("         ,r'\"7")
# print("r`-_   ,'  ,/")
# print(" \\. \". L_r'")
# print("   `~\\/")
# print("      |")
# print("      |")

# # 3003.킹,퀸,룩,비숍,나이트,폰
# pieces = list(map(int,input().split()))
# required_pieces = [1,1,2,2,2,8]
# answer = []
# for a, b in zip(pieces,required_pieces) :
#     answer.append(str(b-a))
# print(" ".join(answer))

# # 2444.별 찍기 - 7
# n = int(input())
# for i in range(n) :
#     print(" "*(n-i-1)+"*"*(2*i+1))
# for i in range(n-2,-1,-1) :
#     print(" "*(n-i-1)+"*"*(2*i+1))

# # 10988.팰린드롬인지 확인하기
# s = input().strip()
# if s == s[::-1] :
#     answer = 1
# else :
#     answer = 0
# print(answer)

# # 1157.단어 공부
# word = input().strip().upper()
# counts = {}
# for w in word :
#     if w in counts :
#         counts[w] += 1
#     else :
#         counts[w] = 1
# max_alp = [w for w,count in counts.items() if count == max(counts.values())]
# if len(max_alp) > 1 :
#     print("?")
# else : 
#     print(max_alp[0])

# # 2941.크로아티아 알파벳
# s = input().strip()
# cr_alp = ["dz=","c=","c-","d-","lj","nj","s=","z="]
# for alp in cr_alp:
#     s = s.replace(alp,"*")
# print(len(s))

# # 1316.그룹 단어 체커
# n = int(input())
# answer = 0

# for _ in range(n) :
#     word = input().strip()
#     existed_word = ''
#     overlap = set()
#     group_word = True

#     for i in word :
#         if i != existed_word :
#             if i in overlap :
#                 group_word = False
#                 break
#             overlap.add(i)
#         existed_word = i
#     if group_word :
#         answer += 1
# print(answer)

# 25206.너의 평점은
grade = {
    "A+" : 4.5,
    "A0" : 4.0,
    "B+" : 3.5,
    "B0" : 3.0,
    "C+" : 2.5,
    "C0" : 2.0,
    "D+" : 1.5,
    "D0" : 1.0,
    "F" : 0
}
total = 0
score_sum = 0
for _ in range(20) :
    n = input().split()
    
    if n[2] == "P" :
        continue
    total += float(n[1])*grade[n[2]]
    score_sum += float(n[1])
print(total/score_sum)
# # 10815.숫자 카드
# n = int(input())
# n_list = set(map(int, input().split()))
# m = int(input())
# m_list = list(map(int, input().split()))
# answer = []
# for i in m_list:
#     if i in n_list:
#         answer.append("1")
#     else:
#         answer.append("0")
# print(" ".join(map(str, answer)))

# # 14425.문자열 집합
# n,m = map(int,input().split())
# n_list = set(input() for _ in range(n))
# m_list = [input() for _ in range(m)]
# answer = 0
# for i in m_list :
#     if i in n_list :
#         answer += 1
# print(answer)

# # 7785.회사에 있는 사람
# n = int(input())
# answer = set()
# for _ in range(n) :
#     name,case = input().split()
#     if case == 'enter' :
#         answer.add(name)
#     elif case == 'leave' :
#         answer.discard(name)
# print('\n'.join(sorted(answer,reverse=True)))

# # 1620.나는야 포켓몬 마스터 이다솜
# n,m = map(int,input().split())
# pokemon = {}
# num = {}
# for i in range(1,n+1) :
#     name = input().strip()
#     pokemon[name] = i
#     num[i] = name
# for _ in range(m) :
#     q = input().strip()
#     if q.isdigit() :
#         print(num[int(q)])
#     else:
#         print(pokemon[q])

# # 10816.숫자 카드 2
# n = int(input())
# cards = list(map(int, input().split()))
# card_count = {}
# for card in cards :
#     if card in card_count :
#         card_count[card] += 1
#     else :
#         card_count[card] = 1
# m = int(input())
# check_cards = list(map(int, input().split()))
# answer = []
# for card in check_cards:
#     if card in card_count :
#         answer.append(str(card_count[card]))
#     else :
#         answer.append("0")
# print(" ".join(answer))


# # 1764.듣보잡
# n,m = map(int,input().split())
# group1 = {input() for _ in range(n)}
# group2 = {input() for _ in range(m)}
# answer = sorted(group1&group2)
# print(len(answer))
# for i in answer :
#     print(i)

# # 1269.대칭 차집합
# n,m = map(int,input().split())
# a = set(map(int,input().split()))
# b = set(map(int,input().split()))
# print(len(a-b)+len(b-a))

# 11478.서로 다른 부분 문자열의 개수
s = input()
answer = set()
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        answer.add(s[i:j])
print(len(answer))
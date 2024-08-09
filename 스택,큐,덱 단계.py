# # 28278.스택 2
# class Stack :
#     def __init__(self) :
#         self.stack = []
#     def push(self,x) :
#         self.stack.append(x)
#     def pop(self) :
#         if self.stack :
#             return self.stack.pop()
#         else :
#             return -1
#     def cnt(self) :
#         return len(self.stack)
#     def empty(self) :
#         if self.stack :
#             return 0
#         else :
#             return 1
#     def number(self) :
#         if self.stack :
#             return self.stack[-1]
#         else :
#             return -1
        
# def stack_command(commands) :
#     stack = Stack()
#     result = []

#     for command in commands :
#         if command.startswith("1 ") :
#             _,x = command.split()
#             stack.push(int(x))
#         elif command == "2" :
#             result.append(stack.pop())
#         elif command == "3" :
#             result.append(stack.cnt())
#         elif command == "4" :
#             result.append(stack.empty())
#         elif command == "5" :
#             result.append(stack.number())

#     return result
# import sys
# n = int(input())
# commands = [sys.stdin.readline().strip() for _ in range(n)]
# answers = stack_command(commands)
# for answer in answers:
#     print(answer)

# # 10773.제로
# def stack(nums) :
#     stack = []
#     for num in nums :
#         if num == '0' :
#             if stack :
#                 stack.pop()
#         else:
#             stack.append(int(num))
#     return sum(stack)
# import sys
# k = int(input())
# nums = [sys.stdin.readline().strip() for _ in range(k)]
# answer = stack(nums)
# print(answer)

# # 9012.괄호
# def ps(strings) :
#     stack = []
#     for string in strings :
#         if string == "(" :
#             stack.append(string)
#         else :
#             if not stack :
#                 return "NO"
#             stack.pop()
#     if not stack :
#         return "YES"
#     else :
#         return "NO"
# t = int(input())
# for _ in range(t) :
#     strings = input()
#     print(ps(strings))

# # 4949.균형잡힌 세상
# def parentheses(strings) :
#     stack = []
#     pair = {
#         ")" :"(",
#         "]" : "["
#     }
#     for string in strings :
#         if string in "([" :
#             stack.append(string)
#         elif string in ")]" :
#             if not stack :
#                 return "no"
#             top = stack.pop()
#             if  pair[string] != top :
#                 return "no"
#     if not stack :
#         return "yes"
#     else :
#         return "no"

# while True:
#     strings = input()
#     if strings == "." :
#         break
#     if strings[-1] =='.' :
#         strings = strings[:-1]
#     answer = parentheses(strings)
#     print(answer)

# # 12789.도키도키 간식드리미
# def snack_sequence(queue) :
#     stack = []
#     start_num = 1

#     while queue :
#         front = queue.pop(0)
#         if front == start_num :
#             start_num += 1
#         else :
#             stack.append(front)
        
#         while stack and stack[-1] == start_num :
#             stack.pop()
#             start_num += 1
        
#     while stack :
#         top = stack.pop()
#         if top != start_num :
#             return "Sad"
#         start_num += 1
#     return "Nice"

# n = int(input())
# queue = list(map(int,input().split()))
# print(snack_sequence(queue))


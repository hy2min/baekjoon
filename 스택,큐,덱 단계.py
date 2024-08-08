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

# 10773.제로
def stack(nums) :
    stack = []
    for num in nums :
        if num == '0' :
            if stack :
                stack.pop()
        else:
            stack.append(int(num))
    return sum(stack)
import sys
k = int(input())
nums = [sys.stdin.readline().strip() for _ in range(k)]
answer = stack(nums)
print(answer)
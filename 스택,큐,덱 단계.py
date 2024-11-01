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

# # 18258.큐 2
# import sys
# from collections import deque
# class Queue :
#     def __init__(self) :
#         self.queue = deque()
#     def push(self,x) :
#         self.queue.append(x)
#     def pop(self) :
#         if self.queue :
#             return self.queue.popleft()
#         else:
#             return -1
#     def size(self) :
#         return len(self.queue)
#     def empty(self) :
#         if self.queue :
#             return 0
#         else :
#             return 1
#     def front(self) :
#         if self.queue :
#             return self.queue[0]
#         else :
#             return -1
#     def back(self) :
#         if self.queue :
#             return self.queue[-1]
#         else :
#             return -1

# n = int(input())
# q = Queue()

# for _ in range(n) :
#     command = sys.stdin.readline().strip()
#     if command.startswith("push") :
#         _,x = command.split()
#         q.push(x)
#     elif command == "pop" :
#         print(q.pop())    
#     elif command == "size" :
#         print(q.size())    
#     elif command == "empty" :
#         print(q.empty())    
#     elif command == "front" :
#         print(q.front())    
#     elif command == "back" :
#         print(q.back())    

# # 11866.요세푸스 문제 0
# from collections import deque

# def josephus(n, k) :
#     queue = deque(range(1, n+1))
#     result = []

#     while queue :
#         queue.rotate(-k+1)
#         result.append(queue.popleft())
#     return result

# n, k = map(int,input().split())
# result = josephus(n, k)
# print("<" + ", ".join(map(str,result)) + ">")

# # 2164.카드2
# from collections import deque
# def card(n) :
#     queue = deque(range(1, n+1))
#     while len(queue) >1:
#         queue.popleft()
#         queue.rotate(-1)
#     return queue[0]

# n = int(input())
# print(card(n))

# # 28297.덱 2
# import sys
# from collections import deque

# class Deque :
#     def __init__(self) :
#         self.deque = deque()
#     def front_push(self,x) :
#         self.deque.appendleft(x)
#     def back_push(self,x) :
#         self.deque.append(x)
#     def left_pop(self) :
#         if self.deque :
#             return self.deque.popleft()
#         else :
#             return -1
#     def pop(self) :
#         if self.deque :
#             return self.deque.pop()
#         else :
#             return -1
#     def size(self) :
#         return len(self.deque)
#     def empty(self) :
#         if self.deque :
#             return 0
#         else :
#             return 1
#     def left_num(self) :
#         if self.deque :
#             return self.deque[0]
#         else :
#             return -1
#     def num(self) :
#         if self.deque :
#             return self.deque[-1]
#         else :
#             return -1

# n = int(input())
# d = Deque()
# for _ in range(n) :
#     command = sys.stdin.readline().strip()
#     if command.startswith("1 ") :
#         _,x = command.split()
#         d.front_push(x)
#     elif command.startswith("2 ") :
#         _,x = command.split()
#         d.back_push(x)
#     elif command == "3" :
#         print(d.left_pop())
#     elif command == "4" :
#         print(d.pop())
#     elif command == "5" :
#         print(d.size())
#     elif command == "6" :
#         print(d.empty())
#     elif command == "7" :
#         print(d.left_num())
#     elif command == "8" :
#         print(d.num())   

# # 1346.풍선 터뜨리기
# import sys
# from collections import deque

# n = int(sys.stdin.readline())
# q = deque(enumerate(map(int,input().split())))
# result = []

# while q :
#     balloon, num = q.popleft()
#     result.append(balloon + 1)

#     if num > 0 :
#         q.rotate(-num+1)
#     elif num < 0 :
#         q.rotate(-num)

# print(" ".join(map(str,result)))

# 24511. queuestack
from collections import deque

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
m = int(input())
c = list(map(int,input().split()))

queuestack = deque()
for i in range(n) :
    if a[i] == 0 :
        queuestack.append(b[i])

for j in range(m) :
    queuestack.appendleft(c[j])

for _ in range(m) :
    print(queuestack.pop(), end=" ")
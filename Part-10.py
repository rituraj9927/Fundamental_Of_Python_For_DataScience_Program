# Stack

# class Stack:
#     def __init__(self):
#         self.data = []
#
#     def push(self, val):
#         self.data.append(val)
#
#     def pop(self):
#         return self.data.pop()
#
#     def __str__(self):
#         return str(self.data)
#
#     # def getSize(self):
#     #     return len(self.data)
#
#     def isEmpty(self):
#         return len(self.data) == 0
#
#     def top(self):
#         return self.data[-1]
#
#     def __len__(self):                          # can be used in place of getSize method
#         return len(self.data)
#
#
# s1 = Stack()            # instantiation of object
# s1.push(2)
# s1.push(6)
# s1.push(7)
# s1.push(10)
# print(s1)
# s1.pop()
# print(s1)
# # print(s1.getSize())
# s2 = Stack()
# s2.push(10)
# s2.push(20)
# print(s2)


# Queue

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#
#
# class Queue:
#     def __init__(self):
#         self.start = None
#         self. end = None
#         self.count = 0
#
#     def enqueue(self, val):
#         newNode = Node(val)
#         if self.end is None:
#             self.start = newNode
#             self.end = newNode
#         else:
#             self.end.next = newNode
#             self.end = newNode
#         self.count +=1
#
#     def dequeue(self):
#         if self.end is None:
#             pass
#         elif self.start == self.end:
#             self.start = None
#             self.end = None
#             self.count -= 1
#         else:
#             self.start = self.start.next
#             self.count -= 1
#
#     def __str__(self):
#         s = ''
#         curr = self.start
#         while curr is not None:                 # while curr != None
#             s += str(curr.val)
#             s += ' -> '
#             curr = curr.next
#         s += 'Null'
#         return s
#
#     def getSize(self):
#         return self.count
#
#     def isEmpty(self):
#         return self.count == 0
#
#     def front(self):
#         return self.start.val
#
#
# q1 = Queue()
# q1.enqueue(10)
# q1.enqueue(20)
# q1.enqueue(30)
# print(q1)
# q1.dequeue()
# print(q1)
# print(q1.isEmpty())
# print(q1.front())


# Trees

# class Node:
#     def __init__(self):





























































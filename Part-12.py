# Trees
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#
#
# class BST:
#     def __init__(self):
#         self.root = None
#
#     def insert(self, val):
#         newNode = Node(val)
#         if self.root is None:
#             self.root = newNode
#         else:
#             self._insert(self.root, newNode)
#
#     def _insert(self, startNode, newNode):
#
#         if startNode.val == newNode.val:
#             return
#         if startNode.val < newNode.val:
#             if startNode.right is None:
#                 startNode.right = newNode
#             else:
#                 self._insert(startNode.right, newNode)
#         else:
#             if startNode.left is None:
#                 startNode.left = newNode
#             else:
#                 self._insert(startNode.left, newNode)
#
#     def printDF(self):
#         self._printDFIN(self.root)
#         print('-'*40)
#         self._printDFPR(self.root)
#         print('-'*40)
#         self._printDFPO(self.root)
#
#     def _printDFIN(self, startNode):
#         if startNode is None:
#             return
#         self._printDFIN(startNode.left)
#         print(startNode.val)
#         self._printDFIN(startNode.right)
#
#     def _printDFPR(self, startNode):
#         if startNode is None:
#             return
#         print(startNode.val)
#         self._printDFPR(startNode.left)
#         self._printDFPR(startNode.right)
#
#     def _printDFPO(self, startNode):
#         if startNode is None:
#             return
#         self._printDFPO(startNode.left)
#         self._printDFPO(startNode.right)
#         print(startNode.val)
#
#     def printBF(self):
#         q = []
#         q.append(self.root)
#         while len(q) > 0:
#             node = q.pop(0)
#             if node is not None:
#                 print(node.val)
#                 q.append(node.left)
#                 q.append(node.right)
#
#     def search(self, val):
#         return self._search(self.root, val)
#
#     def _search(self, startNode, val):
#         if startNode is None:
#             return False
#         if startNode.val == val:
#             return True
#         if val < startNode.val:
#             # if startNode.left is None:
#             #     return False
#             # else:
#             return self._search(startNode.left, val)
#         else:
#             # if startNode.right is None:
#             #     return False
#             # else:
#             return self._search(startNode.right, val)
#
#     def getSize(self):
#         return self._getSize(self.root)
#
#     def _getSize(self, startNode):
#         if startNode == None:
#             return 0
#         return 1 + self._getSize(startNode.left) + self._getSize(startNode.right)
#
#     def isEmpty(self):
#         return self.root is None
#
#
# tree1 = BST()
# tree1.insert(5)                  # complexity is n
# tree1.insert(7)
# tree1.insert(3)
# tree1.insert(1)
# tree1.insert(4)
# tree1.insert(6)
# tree1.insert(9)
# tree1.printDF()                 # complexity is n
# print('_'*40)
# tree1.printBF()
# print(tree1.search(1))            # complexity is log n
# tree1.getSize()
# print(tree1.isEmpty())













































































































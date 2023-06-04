# Complexity

# a=[1,2,3,5,6,7,10,15,20,50,100]
# def binarySearch(sortedList,num):
#     left=0
#     right=len(sortedList)-1
#     mid = (left + right) // 2
#     while left<=right:
#         if num==sortedList[mid]:
#             return mid
#         elif sortedList[mid]<num:
#             left=mid+1
#
#         else:
#             right=mid-1
#         mid = (left + right) // 2
#
# print(binarySearch([1,2,3,4,5,6,7,8,9,10],10))

# def reverse(a):
#     left=0
#     right=len(a)-1
#     while left<right:
#         a[left],a[right]=a[right],a[left]
#         left+=1
#         right-=1
#     print(a)
#
# reverse(a)

# Sorting

# def bubbleSort(a):
#     n = len(a)
#
#     for j in range(n-1):
#         for i in range(0, n-1-j):
#             if a[i] > a[i+1]:
#                 a[i], a[i+1] = a[i+1], a[i]
#
#
# a = [1,2,3,4,5]
# bubbleSort(a)
# print(a)

# List Comprehension
# a=[x**3 for x in range(1,5) if x%2==0]
# print(a)

# 2- Dimensional lists
# a=[1, 2, 3, [1,3,4,4], 4, 5, 6]
# print(a[3][2])

# a=[[1,2],[3,4],[5,6]]
# print(len(a))
# print(len(a[0]))


# def total(mat):
#     r=len(mat)
#     tot=0
#     for i in range(r):
#         c=len(mat[i])
#         for j in range(c):
#             tot+=mat[i][j]
#     return tot
# mat=[[1,2,4],[3,4],[5,6]]
# print(total(mat))

# def total(mat):
#     r=len(mat)
#     tot=0
#     for i in mat:
#
#         for j in i:
#             tot+=j
#     return tot
# mat=[[1,2],[3,4],[5,6,7]]
# print(total(mat))






































































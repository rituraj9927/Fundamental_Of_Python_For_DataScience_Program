# def hcf(a,b):
#     while a!=0 and b!=0:
#         if a>b:
#             a=a%b
#         else:
#             b=b%a
#     return a+b
# print(hcf(12,15))

# def sqrt(num):                    #Newton's method
#     l=0
#     u=num
#     h=(l + u) / 2
#     sq=h*h
#     while abs(sq-num)>1e-14:            # 1*10**-14
#
#         if (sq)<num:
#             l=h
#
#         else:
#             u=h
#
#
#         h= (l + u) / 2
#         sq = h*h
#     return h
# print(sqrt(102))



# def log(x,base):
#     l=0
#     u=x
#     mid=(l+u)/2
#     po=base**mid
#     while abs(po-x)>1e-14:
#         if po<x:
#             l=mid
#         else:
#             u=mid
#         mid=(l+u)/2
#         po=base**mid
#     return mid
# print(log(81,3))
# print(log(45,3))



# LISTS
# marks=[90,29,100,26,49,99]                        #positions are known as indexes here
# print(marks)
# print(marks[3])
# marks[-1]=9
#
# marks=marks[:-1]        # Splicing
# print(marks)
# print(marks[0:-1:1])
# marks[1:3]=[45]
# print(marks)
# marks.append(99)
# print(marks)
# marks.insert(0,99)
# print(marks)
# x=marks.pop(1)
# marks.remove(99)
# print(marks)
# print(x)
# print(marks)
# print(len(marks))
# print(marks.count(99))
# marks[2]=marks.index(99)            # marks.index() returns the index of the passed value
# print(marks)
# # print(marks.index(99,2))
# print(sum(marks))
# print(max(marks))
#
# print([1,2]+[10,20])                #Concatenation of lists

# for x in marks:                      #Enhanced for loop
#
#     print(x)
#
# for i in range(len(marks)):
#     print(str(i)+' = '+str(marks[i]))


# def total(arr):
#     sum=0
#     for x in arr:
#         sum+=x
#     return sum
# print(total([1,2,3,4]))

# def linearsearch(arr,num):
#     for i in range(len(arr)):
#         if arr[i]==num:
#             return i
#     return None
# print(linearsearch([1,2,3],2))
# print(linearsearch([1,2,3],200))



# a=[1,2,3]
# b=a
# print(a==b)
# print(a is b)
# print(id(a))
# print(id(b))
# d=list(a)                       # makes a new list from existing list......like copy constructor in c++
# print(a is d)
# c=a[:]
# print(a is c)


# a=4
# b=5
# print(a,b)
# a,b=b,a                         #multiple variable assignment
# print(a,b)


# def swap(x,y):
#     x,y=y,x


# def swap(arr,i,j):
#     arr[i],arr[j]=arr[j],arr[i]
#
# a=[1,2,3,4]
# swap(a,2,1)
# print(a)





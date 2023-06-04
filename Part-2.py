#
# cmd=input("Enter a command")
# while cmd!='quit':
#     print(cmd)
#     print("Enter new comaand")

#Functions
# def f(x):
#     y=2*x
#     print(y)
# f(6)        #function calling or function invoking
# f(3)
# f(10)

# def area(l,b):        #parameter
#     print(l*b)
# area(4,5)             #arguments
# area(7,9)

# def hello(name):
#     print("hello! "+str(name))
# hello(123)
# hello("bhumika")
# hello('bhumi')
# def area(l,b):
#     return l*b
# a1=area(2,7)
# a2=area(1,9)
# if a1+a2>=30:
#     print("enough area")
# else:
#     print("not enoough area")
# print(a1+a2>=30)
#
# def isEven(num):
#     return num%2==0
    # if num%2==0:
    #    return True
    # else:
    #     return False
    #

# print(isEven(2034))
# print(isEven(364467))

# def getpow(a,b):
#     p=1
#     for i in range(b):
#         p*=a
#     return p
#
# print(getpow(1,5))
#
# print(getpow(2,5))

# def isPrime(num):
#
#     for i in range(2,int(num**0.5+1)):
#         if num%i==0:
#             return False
#     print(num)
#     return True
# # print(isPrime(1))
#
# def printprimes(start,end):
#     for i in range(start,end+1):
#         isPrime(i)

# printprimes(20,100)

# Euclid's algorithm

# def hcf(a,b):
#     while a!=0 and b!=0:
#         if a>b:
#             a=a%b
#
#
#         else:
#             b=b%a
#     return a+b
#
# print(hcf(12,15))
# print(hcf(60,15))
# print(hcf(12,1285))
#
# def lcm(a,b):
#     return a*b/hcf(a,b)         #product of 2 nos= hcf*lcm
# print(lcm(12,15))


#
# def rev(num):
#     result=0
#     while num!=0:
#         d=num%10
#         num=num//10
#         result*=10
#         result+=d
#     return result
# print(rev(7143))



# Armstrong nos
# def isArmstrong(no):
#     num=no
#     sum=0
#     while num!=0:
#         d=num%10
#         sum+=d**3
#         num=num//10
#     if sum==no:
#         return True
#     else:
#         return False
# print(isArmstrong(371))

# import math
# print(math.e)
#
# def log(x,base):
#
#     count=0
#     while x!=1:
#
#         x=x/base
#         count+=1
#
#     return count
# print(log(8,2))
# print(log(16,2))
# print(log(100,10))























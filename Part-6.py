# Strings
# def isPalindrome(s):
#     return s==s[::-1]
#     left=0
#     right=len(s)-1
#     while left<right:
#         if s[left]!=s[right]:
#             return False
#
#         left+=1
#         right-=1
#     return True
#
# print(isPalindrome('level'))

# def Substring(s):
#     n=len(s)
#     for start in range(n):
#         for end in range(start,n):
#             print(s[start:end+1])

# printSubstring('hello hi')

# def getSubstring(s):
#     n=len(s)
#     result=[]
#     for start in range(n):
#         for end in range(start,n):
#             result.append(s[start:end+1])
#     return result
#
# def printPalindromicSubstring(s):
#     reList=getSubstring(s)
#     for ss in reList:
#         if isPalindrome(ss):
#             print(ss)
# printPalindromicSubstring('level')

# l=3
# b=5                                         # Formatting of strings
# s=f"Area {l} and {b} is {l*b}"
# print(s)

# Ternary Operator( Replacement of if else)
# light='Yellow'
# signal="stop" if light=='Red' else "go"
# print(signal)


# def toggleCase(s):
#     toggled=''
#     # toggled.append(s.swapcase())
#     for ch in s:
#         if ch.islower():
#             toggled+=ch.upper()
#         elif ch.isupper():
#             toggled+=ch.lower()
#         else:
#             toggled+=ch
#     return toggled
# print(toggleCase('Hello'))


# def toggleCase(s):                              # more efficient than previous code
#     toggled=[]
#     # toggled.append(s.swapcase())
#     for ch in s:
#         if ch.islower():
#             toggled.append(ch.upper())            #char(ord('C')+32)=c
#         elif ch.isupper():
#             toggled.append(ch.lower())
#         else:
#             toggled.append(ch)
#     return ''.join(toggled)
# print(toggleCase('Hello'))















































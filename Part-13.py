# Functional Programming

# x = 5
# x = 2 * x
# x += 10
# print(x)

# x = 5
# x2 = 2 * x          # x2 = double(x)
# x3 = x2 + 10
# print(x3)

# 1. Treat the data as immutable
# 2. Data and mutations/actions are stored seperately or are separate
# 3. Functions are first class citizens.(Functions are mostly used to mutate the data)


# def double(x):
#     return 2*x


# M A P P I N G

# a = [1, 2, 3, 4]
# m = list(map(lambda x: 2*x, a))             # Declarative programming as we are only declaring the output we want
# print(m)                                    # lambda ()'s are known as functions on the fly

# This is an example of functional programming as list in 'a' is preserved and is treated as immutable.
# Doing the same code using loops will come under imperative programming.


# F I L T E R I N G

# f = filter(lambda x: x % 2 == 0, a)
# f = list(f)
# print(f)


# R E D U C E

# from functools import reduce            # functools is a pre installed library from which we have to import reduce
# r = reduce(lambda x,y: x+y, a)
# print(r)                                   # we don't need to convert 'r' into list as it already contains a no.


# Practice
# from functools import reduce
# cms = [1, 2, 3, 4.5, 0, -1]
# cmsv = list(filter(lambda x : x > 0, cms))
# mms = list(map(lambda x: x*10, cmsv))
# mmss = reduce(lambda x, y: x+y, mms)
# print(mmss)

# cmsv = sum([c*10 for c in cms if c > 0])       # mapping & filtering using list comprehension and reduction using sum.
# a = [10, 20, 30, 40]
# maxx = reduce(lambda x, y: x if x > y else y, a)            # conditional expression of if else
# print(maxx)

# a = [1, 2, 3, 4, 6]
# b = [1, 1]
# c = [0, 1, 5, 15]
# r = list(map(lambda x,y,z: x+y+z, a, b, c))
# print(r)


# Z I P P I N G

# z = list(zip(a, b, c))
# print(z)
# z = dict(zip(a, b))
# print(z)


# T I M E

# import time
# ticks = time.time()     # no. of seconds...time from 1970, jan 1 # Time zone independent
# print(ticks)        # Epoc time ...This time is also called unix time

# localtime = time.localtime(ticks)
# print(localtime)

# localtimereadable = time.asctime(localtime)
# print(localtimereadable)
# time.sleep(5)           # to add delay in  program
# print(time.altzone)


# RANDOM

# import random
# random.seed(7)
# print(random.random())
# print(random.random())
# print(random.random())


# regular expressions are used for pattern matching...Like in a form you need to check the format of file , phn no. etc.


































































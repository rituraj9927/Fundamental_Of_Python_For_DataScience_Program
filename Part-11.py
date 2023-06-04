def fact(n):
    if n == 1:                # Base Case
        return 1
    elif n < 0:
        return None
    return n*fact(n-1)          # Recursive Case


# print(fact(4))
# print(fact(-3))
# print(fact(1))


def fib(i):
    if i == 0 or i == 1:
        return i
    return fib(i-1)+fib(i-2)


# print(fib(7))

memory = [None]*1000                        # Memoization


def fib(i):                                     # More optimized code than previous
    if memory[i] is not None:
        return memory[i]
    if i == 0 or i == 1:
        return i
    result = fib(i-1)+fib(i-2)
    memory[i] = result
    return result


# print(fib(7))


def pow(a, b):
    if b == 0:
        return 1
    return a*pow(a, b-1)


# print(pow(2, 110))


def hcf(a, b):
    if a == 0 or b == 0:
        return a+b
    if a > b:
        return hcf(a % b, b)
    else:
        return hcf(a, b % a)


# print(hcf(12, 15))

def pow(a, b):                              # more optimised code than above pow function
    if b == 0:
        return 1
    if b < 0:
        return 1/pow(a, -b)
    partial = pow(a, b // 2)
    if b % 2 == 0:
        return partial * partial
    else:
        return a * partial * partial


# print(pow(2, -5))

def num_paths(r, c):
    if r == 0 or c == 0:
        return 0
    if r == 1 and c == 1:
        return 1
    if r == 2 and c == 1:                  # Adding obstacle at (2,1)
        return 0
    return num_paths(r-1, c) + num_paths(r, c-1)


# print(num_paths(4, 4))

def getSubsets(arr):
    if len(arr) == 0:
        return [[]]
    elem = arr[0]
    result = []
    ssList = getSubsets(arr[1:])            # every subset is a list... data type is 2D list
    for ss in ssList:
        ss2 = list(ss)
        ss2.append(elem)
        result.append(ss)
        result.append(ss2)
    return result


# print(getSubsets([1, 2, 3, 4]))






































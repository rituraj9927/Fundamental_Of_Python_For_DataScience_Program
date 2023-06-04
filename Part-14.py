# Exception Handling

# result = None
# while result is None:
#     try:
#         a = float(input("Enter a no."))
#         b = float(input("Enter another no."))
#         result = a/b
#         print(result)
#     except:
#         print('Something went wrong')


# try:
#     a = float(input("Enter a no."))
#     b = float(input("Enter another no."))
#     result = a/b
#     print(result)
# # except ZeroDivisionError as e:
# #     print('Division by 0 is not possible', e)
# # except ValueError as e:
# #     print('Invalid input', e)
# except (ZeroDivisionError, ValueError) as e:
#     print('Invalid...Invalid...')
# except Exception:
#     print('Keyboard Interrupt')
# except:
#     print("Something went wrong")
# finally:
#     print("Always do this thing")

# print('Hellooooiiii')


# actual = 20
# expected = 5
# if actual != expected:
#     raise EnvironmentError('Actual was different from expected')
# used when we don't know how to handle the situation


# Packing and Unpackinng

# arr = [2, 3]
# arr2 = [1, arr, 4]
# print(arr2)
# arr2 = [1, *arr, 4]         # * is used for unpacking
# print(arr2)
#
# def foo(*args):
#     print(type(args))
#     for v in args:
#         print(v)
#     print('-'*20)
#
#
# foo(1, 2, 4, 221, 5, 2, 566, 5)
# foo((1, 2, 3), (1, 3, 4))
# foo([1, 2, 4], [11, 10])
# foo(1, 'hello', 4+5)

a = {'name': 'Anne', 'age': 20}
b = {'phone': 1292, 'age': 40}
# c = {**a, **b}        # unpacking of dictionary
# print(c)
# c = {**b, **a}
# print(c)


# def bar(**kwargs):
#     for x in kwargs.items():
#         print(x)
#
#
# bar(a=1, b=100)


# Function Annotations

# def fact(n: 'int') -> 'int':
#     if n == 0:
#         return 1
#     return n * fact(n-1)
#
#
# print(fact(5))
























































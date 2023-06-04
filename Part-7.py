# Tuple

# t1=(1,2,3,4)
# t1[0]                   # is not possible.....tuples are immutable
                        # main reason to use: space efficient and interning is possible

# t0=()
# print(t0)
#
# t1=(100,)               # if there is only one item , then we have to put a comma
# print(t1)
#
# t2=tuple([100])
# print(t2)


# t3=(1,2)+(3,4)
# print(t3)
# print(3 in t3)


# a=1,2,3                     # default data structure in python for comma separated values is tuple and not list
# print(a)

# b,c=(10,20)                   # unpacking of tuple
# print(b)



# a=[10,20,30]
# for i,v in enumerate(a):
#     print(i,v)
#     print(i)            # indexes
#     print(v)               # values


# Dictionary

# phonebook={
#     'Annne':1234,
#     'bill':2345,
#     'Catch':46567,
#     'Annne':3748
# }
# print(phonebook['Annne'])

# person={
#     'name':'Abdul',
#     'age': 20,
#     'Address':{
#         'city':'Delhi',
#         'zip':110085
#     },
#     'friends': [1,2,3,4,5]
# }


# print(person['Address']['city'])
# print(person['friends'][0])
# person['name']='Bhumika'
# print(person)
# person['height']=6
# print(person)


# person={}
# person['name']='Bhumika'
# person['address']={}
# person['address']['city']='Delhi'
# print(person)

# for k in person:
#     print(k,person[k])


# d={x : x**2 for x in range(1,5)}
# print(d)                                                        # Dictionary Comprehension


# Set
# s1={1,2,3}
# print(type(s1))
# print(s1)

# s2=set()
# print(type(s2))

# s3=set([10,12,10,12,3,4,3,5,1,4])
# print(s3)
# s3.add(50)
# print(s3)
# s3.remove(3)
# print(s3)
# s3.pop()                                # any random element can be deleted
# print(s3)
# print(50 in s3)


# a={1,2,3,4}
# b={1,2,3,4,5,6}
# print(a.issubset(b))
# print(a.issuperset(b))
# print(a.union(b))               # or
# print(a.intersection())         # and
# print(a.difference(b))          # -
# print(a.symmetric_difference(b)) # xor



















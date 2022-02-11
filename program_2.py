# 2. Write a program to extract string elements from a list based on below conditions, use
# in-built functions.
# a. First character must capitalize and consonant.
# b. String must not contain any number.


string = ['Aryan', 'kavish', 'Kavish', 'a12ryan']
# print(type(string2))
vowels = ['a','A','e','E','i','I','o','O','u','U']
lst = []

# for i in string:
#     if i.isalpha():
#         if i[0].isupper():
#             if i[0] not in vowels:
#                 lst.append(i)
elements = list(filter(lambda x: x.isalpha() and x[0].isupper() and x[0] not in vowels, string))

print(elements)


# 3. Write a program to create a list of numbers, extract integer numbers from a list based on
# below conditions.
# a. Number must be 4 digit long i.e (1000 to 9999)
# b. First digit of the number must be odd and the last digit must be even.
# c. Number must be divisible by either 3 or 7.


numbers = [3036, 1003, 1673, 1983, 1573, 1002, 1543, 3000]
div = list(filter(lambda x: x % 3 == 0 or x % 7 == 0, numbers))
n = list(map(str,div))
for j in range(len(n)):
    if int(n[j][0]) % 2 != 0 and int(n[j][3]) % 2 == 0:
        print(n[j])




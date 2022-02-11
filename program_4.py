employees = {
        'Proj_Man': {
                'Robert Downey': {
                        'Mark': ['Tl', 8, {'Leonardo': ['Jun_Dev', 1], 'Alexandra': ['Jun_Dev', 1]}],
                        'Samuel': ['TL', 8],
                        'Paul': ['TL', 8, {'Fergal': ['Sen_Dev', 4.5]}],
                        'Tom': ['TL', 8, {'Jerry': ['Jun_Dev', 1.5], 'John': ['Jun_Dev',1.6]}]
                },

                'Anne Hathaway': {
                        'Chris': ['Tl', 5, {'James': ['TL', 0, {'Jennifer': ['Sen_Dev', 3.8], 'Scott': ['Sen_Dev', 3.8],
                                                                'Sophie': ['Sen_Dev', 3.8]}]}],
                        'Pratt': ['TL', 5],
                        'Emma': ['TL', 5],
                        'Will': ['Tl', 5, {'Edge': ['Sen_Dev', 3], 'Ryan': ['Sen_Dev', 3.5]}],
                        'Smith': ['TL', 5, {'Walker': ['Sen_Dev', 2.7], 'Diana': ['Sen_Dev', 2.7]}]
                }
        }
}




# a. Display all employees' names for the given project manager name.


# lst = []
# def names(x):
#         for k, v in x.items():
#                 if type(v) == dict:
#                         names(v)
#                         lst.append(k)
#                 if type(v) == list:
#                         lst.append(k)
#                         for i in v:
#                                 if type(i) == dict:
#                                         names(i)
#                                         lst.append(k)
#                                 if type(i) == list:
#                                         lst.append(k)
# names(employees['Proj_Man']['Robert Downey'])
# print(set(lst))
# names(employees['Proj_Man']['Anne Hathaway']
# print(set(lst))


# b. Display name of only those employees’ whose experience is more than 4 years.

# lst = []
# def experience(x):
#         for k, v in x.items():
#                 if type(v) == dict:
#                         experience(v)
#                         # lst.append(k)
#                 if type(v) == list:
#                         if v[1] > 4:
#                                 lst.append(k)
#                         for i in v:
#                                 if type(i) == dict:
#                                         experience(i)
#
#                                 if type(i) == list:
#                                         if v[1] > 4:
#                                                 lst.append(k)
# experience(employees['Proj_Man'])
# print(set(lst))

# c. Update years of experience with 4.6 whose experience is greater than 3.5 and
# less than 4.5 year.





# d. Display TL with their year of experience, if has no experience then display N/A.


# f. Check company has any employee who has less than 2 years of experience.

lst = []
def experience(x):
        for k, v in x.items():
                if type(v) == dict:
                        experience(v)
                        # lst.append(k)
                if type(v) == list:
                        if v[1] < 2:
                                lst.append(k)
                        for i in v:
                                if type(i) == dict:
                                        experience(i)

                                if type(i) == list:
                                        if v[1] < 2:
                                                lst.append(k)
experience(employees['Proj_Man'])
print(set(lst))

# g. Check Edge is TL or not if not make him TL.


# 1. Write a function to extract words from the sentence that are repeated multiple times, the
# function must return value(s). Display those words with ‘#’ separator (use join function).
# For example : WORD1 # WORD2 # WORD3


lst = []


def repeat(x):
    # for i in x:
    #     if x.count(i) > 1 and i not in lst:
    #         lst.append(i)

    return {i for i in x if x.count(i) > 1}


string = "Hello Hello my my".split()


print(" # ".join(repeat(string)))

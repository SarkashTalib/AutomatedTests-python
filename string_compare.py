'''
Given two sets of string data of equal length, 
calculate the positional difference between them
eg:

GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
^ ^ ^  ^ ^    ^^

differemces = 7
'''

def diff_count(string_a, string_b):
    validate(string_a, string_b)
    return len([[x,y] for x,y in zip(string_a, string_b) if x!=y])

def validate(string_a, string_b):
        if len(string_a) != len(string_b):
            raise ValueError('Length of both string_a and string_b must be equal')


    # we just use list comprehention
    # result = []
    # for x, y in zip(string_a, string_b):
    #     if x != y:
    #         result.append((x,y))

    # return len(result)
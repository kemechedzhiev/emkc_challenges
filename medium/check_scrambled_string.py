import sys
import itertools


# TODO Your input variable will contain two strings of equal length, separated by a comma.
#  You have to check whether the second string is a permutation of the first string.
#  Print "Yes" if it is, "No" if not.

def check_if_scrambled(str_raw):
    str_list = str_raw.split(',')
    str1 = str_list[0]
    str1_permutations = itertools.permutations(str1, len(str1))
    str2 = str_list[1]
    for i in str1_permutations:
        result = ''.join(j for j in i)
        if result == str2:
            return "Yes"
    return "No"


if __name__ == '__main__':
    print("Mission started!")
    strings = sys.argv[1]
    print(check_if_scrambled(strings))

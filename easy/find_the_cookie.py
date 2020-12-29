import sys


# TODO You'll get one input string formatted as '[cookie],[cookie jar]'.
#  Return the sum of the starting index number of the cookie in the cookie jar
#  and the ending index number of the cookie in the cookie jar.

def find_indexes_of_cookie_in_the_jar(raw_str):
    strs = raw_str.split(',')
    first_index_of_cookie = strs[1].index(strs[0])
    return first_index_of_cookie + (len(strs[0]) - 1 + first_index_of_cookie)


if __name__ == '__main__':
    print(find_indexes_of_cookie_in_the_jar(sys.argv[1]))

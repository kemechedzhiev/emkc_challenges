import sys

# TODO Your input variable could contain a variety of string values. Regardless of value,
#  you'll need to reverse the string and print it out.


if __name__ == '__main__':
    value1 = sys.argv[1]
    value1_reversed = value1[::-1]
    print(value1_reversed)
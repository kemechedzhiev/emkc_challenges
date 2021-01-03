import sys


# TODO You will be given an integer and your job is to determine the sum made up by each individual digit.
#  Once you have the sum, determine if the sum is even or odd and then print out either "even" or "odd".

def even_or_odd_str(given_number):
    if given_number % 2 == 0:
        return 'even'
    return 'odd'


def sum_of_digits(given_number):
    result = 0
    for i in str(given_number):
        result += int(i)
    return result


if __name__ == '__main__':
    print("Mission started!")
    number = sys.argv[1]
    print(even_or_odd_str(sum_of_digits(number)))

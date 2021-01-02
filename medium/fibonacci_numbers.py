import sys
import math


# TODO Your input variable will contain a fibonacci sequence number. Your job is to calculate the next n digits.

def find_the_fibonacci_by_index(index):
    fib1 = fib2 = 1
    if index <= 2:
        return fib1
    for i in range(2, int(index)):
        fib1, fib2 = fib2, fib1 + fib2
    return fib2


def find_index_of_the_fibonacci_number(given_number):
    return round(2.078087 + math.log(int(given_number)) + 1.672276) + 2


def find_the_fibonacci_sequence_starting_from(starting_num, seq_length):
    result = ""
    starting_index = int(find_index_of_the_fibonacci_number(starting_num)) + 1
    for i in range(starting_index, starting_index + int(seq_length)):
        result += str(find_the_fibonacci_by_index(i)) + ","
    print(result[:-1])


if __name__ == '__main__':
    print("Mission started!")
    val1 = sys.argv[1]
    val2 = sys.argv[2]
    find_the_fibonacci_sequence_starting_from(val1, val2)

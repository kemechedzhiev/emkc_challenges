import sys


# TODO Your input variable will contain a fibonacci sequence number. Your job is to calculate the next n digits.

def find_the_fibonacci_by_index(index):
    if index == 0:
        return 0
    fib1 = fib2 = 1
    if index <= 2:
        return fib1
    for i in range(2, index):
        fib1, fib2 = fib2, fib1 + fib2
    return fib2


def find_index_of_the_fibonacci_number(given_number):
    # QUESTION Then the formula-driven algorithm is in use, the answer is wrong (smaller by 2). Possibly it's about
    # the indexation.
    for i in range(given_number):
        if find_the_fibonacci_by_index(i) == given_number:
            return i
    return 0
    # return round(2.078087 + math.log(int(given_number)) + 1.672276)


def find_the_fibonacci_sequence_starting_from(starting_num, seq_length):
    result = ""
    starting_index = find_index_of_the_fibonacci_number(starting_num)
    for i in range(starting_index + 1, starting_index + seq_length + 1):
        result += str(find_the_fibonacci_by_index(i)) + ","
    print(result[:-1])


if __name__ == '__main__':
    print("Mission started!")
    val1 = int(sys.argv[1])
    val2 = int(sys.argv[2])
    find_the_fibonacci_sequence_starting_from(val1, val2)

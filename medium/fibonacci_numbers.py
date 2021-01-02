import sys


# TODO Your input variable will contain a fibonacci sequence number. Your job is to calculate the next n digits.

def find_the_fibonacci_by_index(index):
    fib1 = fib2 = 1
    for i in range(2, int(index) + 1):
        fib1, fib2 = fib2, fib1 + fib2
    return fib2


def find_the_fibonacci_sequence_from_index(index, seq_length):
    int_index = int(index)
    result = list()
    answer = ''
    for i in range(int(seq_length)):
        result.append(find_the_fibonacci_by_index(int_index))
        int_index += 1
    for j in result:
        answer += str(j) + ','
    print(answer[:-1])


if __name__ == '__main__':
    print("Mission started!")
    val1 = sys.argv[1]
    val2 = sys.argv[2]
    find_the_fibonacci_sequence_from_index(val1, val2)

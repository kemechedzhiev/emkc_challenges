import sys
# TODO Given a size for a number spiral, you count clockwise with numbers. A 3x3 is 3 columns by 3 rows.
#         2x2  3x3    4x4
#         1 2  7 8 9   7  8  9 10
#         4 3  6 1 2   6  1  2 11
#              5 4 3   5  4  3 12
#                     16 15 14 13
#  The input gives you the size of the spiral that you need to create.
#  The goal is to sum the corners. If you look at the 3x3 grid, the numbers at the corners are
#  7, 9, 3, and 5. If you sum these, you get 24, which is the answer.
#  Write a program that will provide the sum of the corners for any sized spiral up to 100x100.


def count_sum(raw_text):
    size = int(raw_text.split('x')[0])
    result = 0
    for i in range(4):
        result += size * size - i * (size - 1)
    return result


if __name__ == '__main__':
    print("Mission started!")
    size_of_spiral_raw = sys.argv[1]
    print(count_sum(size_of_spiral_raw))
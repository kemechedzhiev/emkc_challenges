import sys


# TODO Take a string of comma separated numbers and print out the sum
#  You'll be getting the list from the standard input

def sum_counter(raw_list_of_data):
    result = 0
    list_of_data = raw_list_of_data.split(',')
    for i in list_of_data:
        result += int(i)
    return result


if __name__ == '__main__':
    print('Mission started')
    print(sum_counter(sys.argv[1]))

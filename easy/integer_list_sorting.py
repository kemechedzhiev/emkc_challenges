import sys


# TODO Take a list of integers and print it after sorting it in descending order.
#  Your input variable will contain a list of integers, you have to sort the list in descending order and print it.

def sort_list_descending(raw_list):
    list_to_sort = raw_list.split(',')
    list_of_ints = []
    for i in list_to_sort:
        list_of_ints.append(int(i))
    list_of_ints.sort(reverse=True)
    print(','.join(str(i) for i in list_of_ints))


if __name__ == '__main__':
    sort_list_descending(sys.argv[1])

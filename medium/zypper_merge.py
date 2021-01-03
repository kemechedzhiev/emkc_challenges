import sys


# TODO You'll get two inputs, each will be a comma separated list of numbers.
#  Each input will contain the same amount of numbers. You'll need to merge the two lists
#  by inserting numbers from value2 into value1. Each number from value2 should be inserted
#  every other number starting after the first number in value 1.

def zyp_merger(val_raw1, val_raw2):
    list1 = val_raw1.split(',')
    list2 = val_raw2.split(',')
    result = ''
    result_list = list()
    for i in range(len(list1)):
        result_list.append(list1[i])
        result_list.append(list2[i])
    for i in result_list:
        result += str(i) + ','
    return result[:-1]


if __name__ == '__main__':
    print('Mission started!')
    val1, val2 = sys.argv[1], sys.argv[2]
    print(zyp_merger(val1, val2))

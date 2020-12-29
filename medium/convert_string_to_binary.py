import sys


# TODO Your input variable will contain a string of three lowercase letters.
#  From this, you'll need to convert it to binary and
#  print out the 24 number representation of those letters in binary.

def convert_to_binary(raw_text):
    binary = ''
    for i in raw_text:
        prefix = ''
        letter_binary = format(ord(i), 'b')
        if len(letter_binary) < 8:
            prefix = '0' * (8 - len(letter_binary))
        binary += prefix + str(letter_binary)
    return binary


if __name__ == '__main__':
    print("Mission started!")
    str_to_convert = sys.argv[1]
    print(convert_to_binary(str_to_convert))

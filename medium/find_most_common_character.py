import sys

# TODO You will be given a string and your job is to find the most common character in that string.
#  If there are two characters which appear the same amount of times and are the largest amount,
#  you should output both separated by a comma in the order they first appeared.


def common_letters_in_the_text(text_raw):
    result = ''
    letters_map = dict()
    for letter in text_raw:
        if letter in letters_map.keys():
            letters_map[letter] += 1
        else:
            letters_map[letter] = 1
    if ' ' in letters_map.keys():
        letters_map.pop(' ')
    max_val = max(letters_map.values())
    for letter in letters_map.keys():
        if letters_map[letter] == max_val:
            result += letter + ','
    return result[:-1]


if __name__ == '__main__':
    print("Mission started!")
    input_str = sys.argv[1]
    print(common_letters_in_the_text(input_str))

import sys


# TODO Given a string with multiple words, return the longest word.

def longest_word(raw_str):
    words = raw_str.split(',')
    words_stripped = []
    for i in words:
        words_stripped.append(i.replace(" ", ""))
    max_length = 0
    words = words_stripped
    result = ""
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
            result = word
        else:
            if len(word) == max_length:
                result += ',' + word
    return result.lower().strip()


if __name__ == '__main__':
    print(longest_word(sys.argv[1]))

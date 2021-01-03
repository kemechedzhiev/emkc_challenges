import sys

# TODO Your input variable will contain a string of invalid JSON.
#  However, each invalid JSON string received can be fixed by making one or more single character changes.
#  Only three possible things may be wrong with the JSON string:
#  1) missing leading or trailing brace,
#  2) unquoted JSON string value,
#  3) missing comma between properties.


def fix_json(invalid_json):
    word = ''
    result = list()
    for symbol in invalid_json:
        if symbol != '{' and symbol != '}':
            if symbol == ':' or symbol == ',':
                result.append(word)
                word = ''
            else:
                word += symbol
    return result


if __name__ == '__main__':
    print('Mission started!')
    str_raw = sys.argv[1]
    print(fix_json(str_raw))

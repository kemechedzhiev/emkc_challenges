import sys


# TODO Your input variable will contain a string of invalid JSON.
#  However, each invalid JSON string received can be fixed by making one or more single character changes.
#  Only three possible things may be wrong with the JSON string:
#  1) missing leading or trailing brace,
#  2) unquoted JSON string value,
#  3) missing comma between properties.


def fix_json(invalid_json):
    content_of_invalid_json = list()
    word_from_json = ''
    for symbol in invalid_json.lower():
        if symbol.isalpha() or symbol.isnumeric():
            word_from_json += symbol
        else:
            if word_from_json != '':
                content_of_invalid_json.append(word_from_json)
                word_from_json = ''
    if word_from_json != '' and word_from_json not in content_of_invalid_json:
        content_of_invalid_json.append(word_from_json)
    if not len(content_of_invalid_json) % 2 == 0:
        return f"There's an error here: {content_of_invalid_json}"
    return make_json_from_list(content_of_invalid_json)


def make_json_from_list(content_to_pack):
    result = ''
    for i in range(0, len(content_to_pack), 2):
        result += '"' + content_to_pack[i] + '":"' + content_to_pack[i+1] + '"'
    return '{' + result + '}'


if __name__ == '__main__':
    str_raw = sys.argv[1]
    print(fix_json(str_raw))

import sys
import re


# TODO Your input variable will contain a string of invalid JSON.
#  However, each invalid JSON string received can be fixed by making one or more single character changes.
#  Only three possible things may be wrong with the JSON string:
#  1) missing leading or trailing brace,
#  2) unquoted JSON string value,
#  3) missing comma between properties.


def fix_json(invalid_json):
    if not invalid_json.startswith('{'):
        invalid_json = '{' + invalid_json
    if not invalid_json.endswith('}'):
        invalid_json = invalid_json + '}'
    if '":' in invalid_json:
        invalid_json.replace('":', '":"')
    if ':"' in invalid_json:
        invalid_json.replace(':"', '":"')
    if '""' in invalid_json:
        invalid_json.replace('""', '","')
    return invalid_json


if __name__ == '__main__':
    str_raw = sys.argv[1]
    print(fix_json(str_raw))

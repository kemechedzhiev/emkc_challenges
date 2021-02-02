import sys

# TODO Your input variable will contain a roman numeral less than 1000 in value.
#  Print the corresponding value of the roman numeral in the decimal system of numbers.


def convert_number_from_roman_to_arabic(roman_number):
    # I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000
    symbol_values = dict()
    symbol_values['I'] = 1
    symbol_values['V'] = 5
    symbol_values['X'] = 10
    symbol_values['L'] = 50
    symbol_values['C'] = 100
    symbol_values['D'] = 500
    symbol_values['M'] = 1000
    result, temp_result, previous_symbol = 0, 0, 'I'
    for symbol in roman_number:
        if symbol_values[symbol] > symbol_values[previous_symbol]:
            result += symbol_values[symbol]
            result -= temp_result
            temp_result = 0
        else:
            temp_result += symbol_values[symbol]
        previous_symbol = symbol
    return result


if __name__ == '__main__':
    roman_number_to_convert = sys.argv[1]
    print(f'{convert_number_from_roman_to_arabic(roman_number_to_convert)}')
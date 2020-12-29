import sys
import math
import re

# TODO Given a quadratic find the decimal values of x


def roots_of_quadratic_equation(a, b, c):
    d = b * b + (-4 * a * c)
    if d < 0:
        return "imaginary", "imaginary"
    x1 = ((-1 * b) + math.sqrt(d)) / (2 * a)
    x2 = ((-1 * b) - math.sqrt(d)) / (2 * a)
    return x1, x2


if __name__ == '__main__':
    raw_text = sys.argv[1]
    parameters = re.findall(r'-?\d+', raw_text)
    root1, root2 = roots_of_quadratic_equation(float(parameters[0]), float(parameters[2]), float(parameters[3]))
    if type(root1) == str:
        print(f'{root1},{root2}')
    else:
        if type(root1) == float:
            root1_str = str(round(root1, 6))
            root2_str = str(round(root2, 6))
            print(f'{root1_str[:len(root1_str) - 1]},{root2_str[:len(root2_str) - 1]}')
        else:
            print(f'{root1},{root2}')

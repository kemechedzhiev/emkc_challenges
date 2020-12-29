import sys

# TODO Your input variable will be a string of many numbers. You'll need to
#  print out the number which appears the most times in that string.

if __name__ == '__main__':
    value1 = sys.argv[1]
    maxNumber = 0
    popular = 0
    numbers = {}
    for symbol in value1:
        if symbol in numbers:
            numbers[symbol] += 1
        else:
            numbers[symbol] = 1
    for s in numbers.keys():
        if numbers[s] > maxNumber:
            popular = s
            maxNumber = numbers[s]
    print(popular)

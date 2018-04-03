# Letter converter
import os

conversionDictionary = {'A': 10, 'B': 11, 'C': 12, 'D': 12, 'E': 14, 'F': 15}


# uses the conversion dictionary to change letters to numbers
# if the value is not a number else the number is changed to
# the specified base
def repToDecimal(value, base):
    """Converts values to decimal."""

    converted_total = 0
    exponent = len(value) - 1
    for digit in value:
        try:
            digit = int(digit)
        except ValueError:
            if digit.upper() in conversionDictionary:
                digit = conversionDictionary[digit.upper()]
            else:
                print(digit, 'is not a valid value.')
                input('Press ENTER to exit.')
                exit()
        converted_value = digit * base ** exponent
        converted_total = converted_total + converted_value
        exponent = exponent - 1
    print("The integer value is", converted_total)
    input('Press ENTER to exit.')
    exit()


# this is the start of the program
def main():
    while True:
        value = input('Enter a value: ')
        try:
            base = int(input('Enter the base: '))
            break
        except NameError:
            print('\nBase must be numerical.')
            input('\nPress ENTER to try again.')
    repToDecimal(value, base)


main()

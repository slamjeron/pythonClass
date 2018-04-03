import math


def getWords(file_name):
    text_file = open('files/' + file_name + '.txt')
    return [xt.strip('\n') for xt in text_file.readlines()]


num = getWords('numbers')
num = list(map(float, num))
print(float(sum(num)) / len(num))

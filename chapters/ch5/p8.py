def deleat(array, word):
    narr = set()
    for a in array:
        if a != word:
            narr.add(word)

    return array


def getWords(file_name):
    text_file = open('files/' + file_name + '.txt')
    return [xt.strip('\n') for xt in text_file.readlines()]


newList = set()
words = getWords("wordFile")
count = 0
for x in words:
    count = 0
    for x1 in words:
        if x1 == x:
            count += 1

    words = deleat(words, x)
    newList.add(x + ' ' + str(count))

newList = sorted(newList)

for x in newList:
    print(x)

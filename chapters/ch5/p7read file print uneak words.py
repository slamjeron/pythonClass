def getWords(file_name):
    text_file = open('files/' + file_name + '.txt')
    return [xt.strip('\n') for xt in text_file.readlines()]


newList = set()

for x in getWords("wordFile"):
    newList.add(x)

newList = sorted(newList)

for x in newList:
    print(x)

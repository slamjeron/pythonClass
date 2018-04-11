import random

variable = 0
def getWords(file_name):
    text_file = open('files/' + file_name + '.txt')
    return [x.strip('\n') for x in text_file.readlines()]


def sentence():
    return nounPhrase() + " " + verbPhrase()


def nounPhrase():
    return random.choice(articles) + ' ' + random.choice(nouns)


def verbPhrase():
    return random.choice(verbs) + ' ' + nounPhrase() + ' ' + prepositionalPhrase()


def prepositionalPhrase():
    return random.choice(prepositions) + ' ' + nounPhrase()


def main():
    number = int(input('Enter the number of sentences:'))
    for count in range(number):  # type: int
        print(sentence())


articles = tuple(getWords('articles'))
nouns = tuple(getWords('nouns'))
prepositions = tuple(getWords('preposition'))
verbs = tuple(getWords('verbs'))
main()

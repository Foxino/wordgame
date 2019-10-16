import json
import string
import random

with open('./words_dictionary.json', 'r') as f:
    words = json.load(f)

atoZ = "abcdefghijklmnopqrstuvwxyz"

def generateGame(minLength, letters):
    c = getRandomChars(letters)
    result = {
        "must_include" : c[0],
        "can_include" : c,
        "words" : getWordList(c[0], c, minLength)
    }
    return result

def getRandomChars(x):
    result = []
    result.append(random.choice(atoZ))
    while len(result) != x:
        y = random.choice(atoZ)
        if y not in result:
            result.append(y)
    return result


def getWordList(mustInclude, canInclude, minLength):
    result = []
    for word in words:
        if mustInclude in word and len(word) >= minLength:
            includesAll = True
            for w in word:
                if w not in canInclude:
                    includesAll = False
            if(includesAll):
                result.append(word)
    return result

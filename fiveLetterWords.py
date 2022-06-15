# %%
def getFiveLetterWords(fileName):
    words = list()
    with open(fileName, 'r') as f:
        for line in f.readlines():
            word = line.strip()
            if(len(word) == 5):
                words.append(word)
    return words

def writeToFile(fileName, words):
    with open(fileName, 'w') as f:
        for word in words:
            f.writelines(word + "\n")

def sortAccordingToFreq(words):
    wordFreqList = dict()
    letterFreq = {
        'a' : 8.4966,
        'b' : 2.072,
        'c' : 4.5388,
        'd' : 3.3844,
        'e' : 11.1607,
        'f' : 1.8121,
        'g' : 2.4705,
        'h' : 3.0034,
        'i' : 7.5448,
        'j' : 0.1965,
        'k' : 1.1016,
        'l' : 5.4893,
        'm' : 3.0129,
        'n' : 6.6544,
        'o' : 7.1635,
        'p' : 3.1671,
        'q' : 0.1962,
        'r' : 7.5809,
        's' : 5.7351,
        't' : 6.9509,
        'u' : 3.6308,
        'v' : 1.0074,
        'w' : 1.2899,
        'x' : 0.2902,
        'y' : 1.7779,
        'z' : 0.2722
    }

    for word in words:
        wordFreqList[word] = 0
        for c in word:
            wordFreqList[word] = wordFreqList[word] + letterFreq[c]

    ret = {k: v for k, v in sorted(wordFreqList.items(), key=lambda item: item[1], reverse=True)}

    return [*ret]


# Get the words with 5 letters
fiveLetterWords = getFiveLetterWords("wordlist.txt")
commonFiveLetterWords = getFiveLetterWords("commonWords.txt")


wordleList = [*sortAccordingToFreq(commonFiveLetterWords), *sortAccordingToFreq(fiveLetterWords)]
writeToFile("wordleList.txt", wordleList)



# %%

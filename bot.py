# %%
def guess(guessNo, word):
    # Guess the word
    game.send_keys(word)
    game.send_keys(Keys.ENTER)
    # Get response
    evaluation = gameRows[guessNo].get_property("_evaluation")

    if (evaluation[0] == evaluation[1] == evaluation[2] == evaluation[3] == evaluation[4] == 'correct'):
        return True
    else: 
        updatePossibilities(evaluation,word)
        return False

def canBeWordle(word):
    for i in range(len(word)):
        if word[i] not in possibilities[i]:
            return False
    for c in exists:
        if c not in word:
            return False
    return True

def updatePossibilities(evaluation, word):
    # evaluate the response
    for j in range(len(word)):
        item = evaluation[j]
        
        if item == 'correct':
            possibilities[j] = word[j]
            exists.append(word[j])

        elif item == 'absent':
            for k in range(len(word)):
                if word[j] in exists:
                    continue
                elif word[j] in possibilities[k]:
                    possibilities[k].remove(word[j])

        elif item == 'present':
            if word[j] in possibilities[j]:
                possibilities[j].remove(word[j])
            if word[j] not in exists:
                exists.append(word[j])


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Get chrome driver
driver = webdriver.Chrome("C:\Users\Deniz\.wdm\drivers\chromedriver\win32\chromedriver_win32\\chromedriver.exe")

# Open the Website
driver.get("https://www.powerlanguage.co.uk/wordle/")

# Close help page
game = driver.find_element(By.CLASS_NAME, "nightmode")
game.click()

# Find the game element
gameApp = driver.execute_script(
    "return document.querySelector('game-app').shadowRoot.querySelector('game-theme-manager').querySelector('[id=\"game\"]')")
gameRows = gameApp.get_property("children")[1].get_property("children")[0].get_property("children")


# Get the words with 5 letters
wordlist = "wordleList.txt"
words = list()
with open(wordlist, 'r') as f:
    for line in f.readlines():
        word = line.strip()
        if(len(word) == 5):
            words.append(word)

# Letters 
alphabet = "abcdefghijklmnopqrstuvwxyz"
allLetters = list()
for c in alphabet:
    allLetters.append(c)

# initial possibilities
possibilities = {
    0 : allLetters.copy(),
    1 : allLetters.copy(),
    2 : allLetters.copy(),
    3 : allLetters.copy(),
    4 : allLetters.copy(),
}
exists = list()

# initial guess
# wordle = "arise"
# wordle = "weary"
# wordle = "pilot"
# wordle = "vague"
# wordle = "enter"
# wordle = "roate"
# wordle = "carse"

wordle = "arise"
guess(0, wordle)
time.sleep(3)

wordle = "clout"
guess(1, wordle)

numberOfGuesses = 5
for i in range(2,numberOfGuesses):
    time.sleep(3)

    for word in words:
        if canBeWordle(word):
            wordle = word
            break
    
    if(guess(i, wordle)):
        print("We have found the wordle with " + str(i+1) + " guesses.")
        break
    

# %%

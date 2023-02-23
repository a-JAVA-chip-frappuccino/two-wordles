#
# header
#
import random

#
# choice of word dictionary
#

print("Would you like to use the official Wordle dictionary or the one made for this version of the game?")
dictToUse = input("Type 'official' or 'this version', respectively: ")
while dictToUse.lower() != "official" and dictToUse.lower() != "this version":
  dictToUse = input("Please type either 'official' or 'this version' without quotes: ")

#
# choose correct word from dictionary
#

# DIY word dictionary route
if dictToUse.lower() == "this version":
  import possibleWords as pw # DIY word dictionary
  
  randIndexKey = chr(random.randint(97, 122))
  listWords = pw.wordsDict[randIndexKey]
  randIndexValue = random.randint(0, len(listWords) - 1)
  correctWord = listWords[randIndexValue]
  correctWordLetters = set(correctWord)
  usingDIY = True

# official word dictionary route
else:
  import officialPossibleWords as opw # official word dictionary

  randIndex = random.randint(0, len(opw.listWords) - 1)
  correctWord = opw.listWords[randIndex]
  correctWordLetters = set(correctWord)
  usingDIY = False

# color variable storage
greenStart = "\033[1;32;40m"
greenEnd = "\033[0m"

yellowStart = "\033[1;33;40m"
yellowEnd = "\033[0m"

whiteStart = "\033[1;37;40m"
whiteEnd = "\033[0m"

#
# introduction to gameplay mechanics
#

print("\nWelcome to Wordle!")
print("You will have six tries to correctly guess a 5-letter word!")

print("\nIf you guess a letter correctly in the correct space, it will turn " + greenStart + "green" + greenEnd + ".")
print("If you guess a letter correctly in the wrong space, it will turn " + yellowStart + "yellow" + yellowEnd + ".")
print("If you guess a letter incorrectly, it will turn " + whiteStart + "white" + whiteEnd + ".")

print("\nLet's get started!")

blankSpaces = ""
for i in range(5):
  blankSpaces += whiteStart + "_" + whiteEnd + " "
print(blankSpaces + "\n")

#
# start gameplay
#

continueGuessing = True
counter = 0

while continueGuessing:
  # stop gameplay and end loop if more than 5 guesses
  if counter > 5:
    continueGuessing = False
    print("The correct word was " + correctWord + "!")
  
  # play game
  else:
    # guess allowable word
    guessedWord = input("Type in a 5-letter word: ")

    if usingDIY:
      while guessedWord not in pw.wordsSet:
        print("Not a valid word!")
        guessedWord = input("Type in a 5-letter word: ")
    else:
      while guessedWord not in opw.listWords:
        print("Not a valid word!")
        guessedWord = input("Type in a 5-letter word: ")

    # print word with changed letter colors
    guessedWordColors = ""
    for i in range(5):
      if guessedWord[i] == correctWord[i]:
        guessedWordColors += greenStart + guessedWord[i] + greenEnd + " "
      elif guessedWord[i] in correctWordLetters:
        guessedWordColors += yellowStart + guessedWord[i] + yellowEnd + " "
      else:
        guessedWordColors += whiteStart + guessedWord[i] + whiteEnd + " "
    print(guessedWordColors)

    # print how user did with guessing word
    if guessedWord == correctWord:
      continueGuessing = False
      if counter == 0:
        print("Lucky guess! Wow!")
      elif counter > 0 and counter < 3:
        print("Superb guessing!")
      elif counter > 2 and counter < 5:
        print("Great job!")
      else:
        print("Phew!")
      
  counter += 1

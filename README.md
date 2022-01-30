This is an offshoot of the popular Wordle game using dictionaries, sets, and lists in Python. There is no object-oriented programming and no functions, making it an appropriate programming level for someone learning basic data structures in Python.

The user has the option to choose between the official Wordle dictionary (https://bert.org/assets/posts/wordle/main-beautified.js) or to make their own. These can be adjusted in the officialPossibleWords.py and possibleWords.py files, respectively. The latter is broken up into a series of lists organized by the first letter in each 5-letter word.

The code follows the format of a true Wordle game, allowing the user to guess a 5-letter word 6 times, adjusting the color based on if a letter is correctly located and guessed (green), correctly guessed (yellow), or incorrect (white). If the user guesses the word, an encouraging phrase is displayed on the screen, though if they cannot in 6 guesses, the word is given instead.

Some limitations of this project are that there is no test that the words in either officialPossibleWords.py or possibleWords.py are 5 letters long or valid words in English and that not every word is represented in either version.

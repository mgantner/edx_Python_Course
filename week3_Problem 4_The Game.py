"""Now you will implement the function hangman, which takes one parameter - the secretWord the user is to guess. This starts up an interactive game of Hangman between the user and the computer. Be sure you take advantage of the three helper functions, isWordGuessed, getGuessedWord, and getAvailableLetters, that you've defined in the previous part.

Hints:
You should start by noticing where we're using the provided functions (at the top of ps3_hangman.py) to load the words and pick a random one. Note that the functions loadWords and chooseWord should only be used on your local machine, not in the tutor. When you enter in your solution in the tutor, you only need to give your hangman function.

Consider using lower() to convert user input to lower case. For example:

guess = 'A'
guessInLowerCase = guess.lower()

- Consider writing additional helper functions if you need them!

There are four important pieces of information you may wish to store:

- secretWord: The word to guess.
- lettersGuessed: The letters that have been guessed so far.
- mistakesMade: The number of incorrect guesses made so far.
- availableLetters: The letters that may still be guessed. Every time a player guesses a letter, the guessed letter must be removed from availableLetters (and if they guess a letter that is not in availableLetters, you should print a message telling them they've already guessed that - so try again!).

Note that if you choose to use the helper functions isWordGuessed, getGuessedWord, or getAvailableLetters, you do not need to paste your definitions in the box. We have supplied our implementations of these functions for your use in this part of the problem. If you use additional helper functions, you will need to paste those definitions here.

Your function should include calls to input to get the user's guess.
"""

def AvailableLetters(lettersGuessed):
    import string
    alphabet = [i for i in string.ascii_lowercase]
    for i in lettersGuessed:
        if i in alphabet:
            alphabet.remove(i)
    return ''.join(alphabet)

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is",len(secretWord),"letters long")
    print('-----------')
    lettersGuessed = []
    correctLettersGuessed = []
    guesses = 8
    while guesses > 0:
        correctWordNow = [letter if letter in correctLettersGuessed else "_ " for letter in secretWord]
        if ''.join(correctWordNow) == secretWord:
            return print ("Congratulations, you won!")
            break
        else:
            print ("You have",guesses,"guesses left")
            print ("Available Letters:",AvailableLetters(lettersGuessed))
            guess = input ("Please guess a letter: ")
            while guess not in AvailableLetters(lettersGuessed):
                print ("Oops! You've already guessed that letter: ",''.join(correctWordNow))
                print('-----------')
                print ("You have",guesses,"guesses left")
                print ("Available Letters:",AvailableLetters(lettersGuessed))
                guess = input ("Please guess a letter: ")
            else:
                letter = guess.lower()
                correctWordNow = [letter if letter in correctLettersGuessed else "_ " for letter in secretWord]
                lettersGuessed.append(letter)    
                if letter in secretWord:
                    correctLettersGuessed.append(letter)
                    correctWordNow = [letter if letter in correctLettersGuessed else "_ " for letter in secretWord]
                    print ("Good guess:", ''.join(correctWordNow))
                    guesses += 0
                else:    
                    correctWordNow = [letter if letter in correctLettersGuessed else "_ " for letter in secretWord]
                    guesses -= 1
                    print ("Oops! That letter is not in my word:", ''.join(correctWordNow))
                if guesses == 0:
                    print('-----------')
                    return print ("Sorry, you ran out of guesses. The word was", secretWord + ".")
            print('-----------')
            correctWordNow = [letter if letter in correctLettersGuessed else "_" for letter in secretWord]
    return secretWord

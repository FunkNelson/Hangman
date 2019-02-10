# FUNCTIONS
def printWelcome():
	print '*************************'
	print '*  Welcome to Hangman!  *'
	print '*************************'
	print ''


def selectWord(word):
	return word

def maskWord(word, guessedLetters):
	currentWordState = ''
	for i in word:
		if i in guessedLetters:
			currentWordState = currentWordState + i + ' '
		else:
			currentWordState = currentWordState + '_ '
	return currentWordState

def isWordSolved(word):
	for i in word:
		if i == '_':
			return False
	# if no masked letters are found
	return True
			


def userGuess(guessedLetters):
	guess = raw_input("Guess a letter: ")
	#print "Your guess is: ", guess
	guessedLetters.append(guess)

# GLOBAL
guessedLetters = []
uncoveredWord = ''
solved = False


# FLOW
printWelcome()
word = selectWord('ALICE')
print maskWord(word, guessedLetters)

while (isWordSolved(maskWord(word, guessedLetters)) == False):
	userGuess(guessedLetters)
	print maskWord(word, guessedLetters)

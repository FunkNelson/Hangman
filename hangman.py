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
	print 'Congratulations, the word has been solved!'
	return True
			


def userGuess(guessedLetters):
	guess = raw_input("Guess a letter: ")
	#print "Your guess is: ", guess
	guessedLetters.append(guess)


def printHangman():
	line1 = '  __________'
	line2 = '  //      |'
	line3 = ' //       O'
	line4 = '/||      /|\\ '
	line5 = ' ||      / \\'
	line6 = ' ||'
	line7 = '----'
	line8 = ''

	print line1
	print line2
	print line3
	print line4
	print line5
	print line6
	print line7
	print line8

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
	print ''
	print maskWord(word, guessedLetters)
	print ''
	printHangman()


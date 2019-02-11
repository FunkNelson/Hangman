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
	#print 'Guessed Letters: ' + str(guessedLetters)
	return currentWordState

def isWordSolved(word):
	for i in word:
		if i == '_':
			return False
	# if no masked letters are found
	print 'Congratulations, the word has been solved!'
	return True
			


def userGuess(word, guessedLetters):
	guess = raw_input("Guess a letter: ")
	#print "Your guess is: ", guess
	guessedLetters.append(guess)
	return isGuessCorrect(word, guess)


def isGuessCorrect(word, guessedLetter):
	return guessedLetter in word

	
def printHangman(wrongGuessCount):
	line1 = '  __________'
	line2 = '  //      |'
	
	if wrongGuessCount > 0:
		line3 = ' //       O'
	else:
		line3 = ' //       '
	
	if wrongGuessCount == 2:
		line4 = '/||       |  '
	elif wrongGuessCount == 3:
		line4 = '/||      /|  '
	elif wrongGuessCount > 3:
		line4 = '/||      /|\\ '
	else:
		line4 = '/||     '
	
	if wrongGuessCount == 4:
		line5 = ' ||      / '
	elif wrongGuessCount > 4:	
		line5 = ' ||      / \\'
	else:
		line5 = ' ||'
	
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
wrongGuessCount = 0


# FLOW
printWelcome()
word = selectWord('ALICE')
print maskWord(word, guessedLetters)

while (isWordSolved(maskWord(word, guessedLetters)) == False):

	#prompt user for guess and check if it is correct
	if (userGuess(word, guessedLetters) == False):
		wrongGuessCount = wrongGuessCount + 1 

	print ''
	print maskWord(word, guessedLetters)
	print '' 
	print 'Guessed Letters: ' + str(guessedLetters)
	print ''
	printHangman(wrongGuessCount)

	#lose if there are six incorrect guesses
	if wrongGuessCount == 5:
		print 'Sorry, you didn\'t guess the phrase and are dead now'
		quit() 


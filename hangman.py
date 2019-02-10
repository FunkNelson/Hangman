def printWelcome():
	print '*************************'
	print '*  Welcome to Hangman!  *'
	print '*************************'
	print ''


def selectWord():
	return 'ALICE'

def printWordStatus(word):
	for i in word:
		print('_'),
	print ''

printWelcome()
word = selectWord()
printWordStatus(word)
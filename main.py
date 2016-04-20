import time
import progressbar

def Main():
	print('##########Scrackle##########')

	f = open('slowa.txt', 'r')
	words = f.readlines()
	f.close()	
	print('Database contains ' + str(len(words)) + ' words.')
	letters = input('Gimme letterz: ')
	letters = list(letters)
	available_words = []

	with progressbar.ProgressBar(max_value=len(words)) as bar:
		for i, word in enumerate(words):
			#print(str(i) + '/' + str(len(words)) + ' words checked.')
			word = word.replace('\n', '').replace('\r', '')
			count = 0
			if len(word) <= len(letters):
				l = len(word)
				word_test = word

				for j, letter in enumerate(letters):
					if letter in word_test:
						count += 1
						word_test = word_test.replace(letter, '')
				if count == l:
					available_words.append(word)
			if i % 10000 == 0:
				bar.update(i)

	print('I found ' + str(len(available_words)) + ' words you can build: ')
	for i, word in enumerate(available_words):
		print(str(i + 1) + '. ' + word)

Main()
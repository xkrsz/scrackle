def Main():
	print('=====Scrackle=====')

	f = open('slowa.txt', 'r')
	words = f.readlines()
	f.close()
	#words = ['kupa', 'dupa']	
	#print(words[1:25])
	print('Database contains ' + str(len(words)) + ' words.')
	letters = raw_input('Gimme letterz: ')
	letters = list(letters)

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
				print(word + ' can be build from ' + str(letters))

Main()
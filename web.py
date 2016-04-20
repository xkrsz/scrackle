import os

from flask import Flask
app = Flask(__name__)

def Main():
	print('##########Scrackle##########')

	f = open('slowa.txt', 'r')
	words = f.readlines()
	f.close()	
	print('Database contains ' + str(len(words)) + ' words.')
	return words

@app.route('/<letters>')
def FindWords(letters='', words=Main()):
	print('Got letters: ' + letters)
	letters = list(letters)
	available_words = []

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
	return str(available_words)

Main()

if os.environ.get('MODE', 'development') == 'production':
	print('Running in production mode...')
	app.run(host=('0.0.0.0'))
else:
	print('Running in development mode...')
	app.debug = True
	if __name__ == '__main__':
		app.run()
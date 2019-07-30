import requests
import random


import config

class Hangman():

	def __init__(self):
	    self.used_letters = []
	    self.lives = 5
	    self.hidden_word = []

	def import_words(self):
		#word_site = config.word_site
		#response = requests.get(word_site)
		#WORDS = response.content.splitlines()
		#return WORDS
		return ['parmesan', 'poker', 'baguette', 'bottle', 'table', 'keyboard', 'internship', 'friend']
		
	def get_word(self, word_list):
		word_to_guess = random.choice(word_list)
		return word_to_guess

	def get_guess(self):
		letter_guessed = input('What is your guess : ')
		if letter_guessed in self.used_letters:
			print('Letter already used')
			letter_to_return = self.get_guess()
			return letter_to_return
		elif letter_guessed.isalpha() and len(letter_guessed) == 1:
			self.used_letters.append(letter_guessed)
			return letter_guessed
		else:
			print('Please enter a letter.')
			letter_to_return = self.get_guess()
			return letter_to_return

	def compare(self, letter_guessed, word_to_guess):
		if letter_guessed in word_to_guess:
			for index, letter in enumerate(word_to_guess):
				if letter == letter_guessed:
					self.hidden_word[index] = letter
			print('You were right !')
			print('word : ', self.hidden_word)
			print('lives : ', self.lives)
			print('Used letters : ', self.used_letters)

		else:
			print('Wrong, you lost a life !')
			self.lives -= 1
			print('word : ', self.hidden_word)
			print('lives : ', self.lives)
			print('Used letters : ', self.used_letters)

	def game(self):
		word_list = self.import_words()
		word_to_guess = self.get_word(word_list)
		for i in range(len(word_to_guess)):
			self.hidden_word.append('*')
		while self.lives != 0:
			print('----------------------------------')
			letter_guessed = self.get_guess()
			self.compare(letter_guessed, word_to_guess)
			if ''.join(self.hidden_word) == word_to_guess:
				print('You won !')
				break
			if self.lives == 0:
				print('You lost !')

g = Hangman()
g.game()
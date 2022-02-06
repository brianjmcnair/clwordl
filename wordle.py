#!/usr/bin/python

import sys
import random

valid_words = []
words_file = open('words.txt', 'r')
valid_words = words_file.read().split()

def get_word():
    ''' Retrieves word to be guessed for game. '''
    return random.choice(valid_words)

def split(word):
    ''' Splits word into list of characters. '''
    return [char for char in word]

class MyWordle:
    def __init__(self, word):
        ''' 
        Constructor for game class.
        :param string word: the correct word for the game.
        '''
        self.wordle = {}
        self.guesses = []
        self.guesses_results = []
        self.word = word
        self.has_won = False
        self.count = 0
    
    def __increment_count(self):
        ''' Increments count of guesses made. '''
        self.count += 1
    
    def __evaluate_guess(self, word):
        ''' 
        Given valid guess, returns string denoting 
        accuracy of guess. If word matches correct word,
        self.has_won is set to true.
        :param string word: the latest guess from the player.
        '''
        if self.word == word:
            self.has_won = True
            return "🟩🟩🟩🟩🟩"
        
        accuracy_list = ['⬜️','⬜️','⬜️','⬜️','⬜️']
        word_split = split(word)
        for index in range(0, len(self.word)):
            letter = self.word[index]
            if word[index] == letter:
                accuracy_list[index] = '🟩'
                word_split[index] = '.'
            elif letter in word_split:
                spot = word_split.index(letter)
                accuracy_list[spot] = '🟨'

        response_string = "".join(accuracy_list)
        return response_string

    def __make_guess(self):
        '''
        Prompts the user for a word guess until a valid entry
        is received. 
        '''
        is_valid = False
        while not is_valid:
            print("")
            guess = input("Guess #" + str(self.get_round_count() + 1) + ": ").lower()
            if len(guess) == 5:
                is_valid = True
            else:
                print("")
                print("Invalid word. All guesses must be exactly 5 letters long.")
                continue
            if guess in self.guesses:
                is_valid = False
                print("")
                print(guess + " has already been guessed. You might want to try a different word :)")
            if guess not in valid_words:
                is_valid = False
                print(guess + " is not in the list of possible words. Please try a different guess.")
        self.guesses.append(guess)
        self.__increment_count()
        return self.__evaluate_guess(guess)

    def __print_guesses(self):
        ''' 
        After a guess has been evaluated, the response string 
        from each guess is printed.
        '''
        for guess in range(0,len(self.guesses)):
            print("          " + self.guesses_results[guess] + "  (" + self.guesses[guess] + ")")
    
    def get_round_count(self):
        return self.count
    
    def play_game(self):
        while self.get_round_count() < 6 and not self.has_won:
            guess = self.__make_guess()
            self.guesses_results.append(guess)
            print("")
            self.__print_guesses()
        print("")
        if self.has_won:
            print("Congratulations! You have correctly guessed the word!")
        else:
            print ("The correct word was " + self.word)
            print("Better luck next time :(")
        print("")
        
            
def print_intro_message():
    ''' Prints intro message at start of game. ''' 
    print("")
    print("Rules of the game:")
    print("- You have 6 attempts to guess the 5 letter word")
    print("- For each guess, '-' means that the letter in that spot ")
    print("  is not in the word. '*' means that the letter is in the")
    print("  word, but in a different spot. 'X' means the letter is in")
    print("  the word, and in that exact spot.")
    print("")
    print("Good luck!")

def play_wordle():
    ''' Creates game object, commences game. '''
    word = get_word()
    print_intro_message()
    game = MyWordle(word)
    game.play_game()
    
if __name__ == '__main__':
    ''' When called from command line, calls play_wordle() function. '''
    play_wordle()

#!/usr/bin/python

import sys

def get_word():
    return "wordl"

class MyWordle:
    def __init__(self, word):
        self.wordle = {}
        self.guesses = []
        self.guesses_results = []
        self.word = word
        self.__set_hash(word)
        self.has_won = False
        self.count = 0
    
    def __set_hash(self,word):
        # Put word in hash table
        # Each key is a character,
        # and the corresponding value is the position
        # within the word
        for letter in range(0,len(word)):
            self.wordle[word[letter]]=letter
    
    def __increment_count(self):
        self.count += 1
    
    def __evaluate_guess(self, word):
        accuracy_list = ['-','-','-','-','-']
        if self.word == word:
            self.has_won = True
            return "XXXXX"
    
        for index in range(0, len(word)):
            character = word[index]
            if character in self.wordle:
                position = self.wordle[character]
                if index == position:
                    accuracy_list[index]="X"
                else:
                    accuracy_list[index]="*"

        response_string = ""
        for value in accuracy_list:
            response_string += value
        
        return response_string

    def make_guess(self):
        is_valid = False
        while not is_valid:
            print("")
            guess = input("Guess #" + str(self.get_round_count() + 1) + ": ")
            if len(guess) == 5:
                is_valid = True
            else:
                print("")
                print("Invalid word. All guesses must be exactly 5 letters long")
        self.guesses.append(guess)
        self.__increment_count()
        return self.__evaluate_guess(guess)

    def __print_guesses(self):
        for guess in range(0,len(self.guesses)):
            print("          " + self.guesses_results[guess] + "  (" + self.guesses[guess] + ")")
    
    def get_round_count(self):
        return self.count
    
    def play_game(self):
        while self.get_round_count() < 6 and not self.has_won:
            guess = self.make_guess()
            self.guesses_results.append(guess)
            print("")
            self.__print_guesses()
        print("")
        if self.has_won:
            print("Congratulations! You have correctly guessed the word!")
        else:
            print("Better luck next time :(")
        print("")
        
            
def play_wordle():
    word = get_word()
    game = MyWordle(word)
    game.play_game()
    

if __name__ == '__main__':
    play_wordle()
    # TODO - get list of words - check on each guess that word is valid
    # for validity check: first, ensure word is 6 letters long.
    # then, check dictionary, and verify word is in there

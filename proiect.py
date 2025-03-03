# Modules
import random

class Hangman:
     __hearts = 6
     __word_list = []
     __congrats_sentences = [
          "Awesome!",
          "You nailed it!",
          "Sweet!",
          "Good Job!",
          "Great!",
          "Incredible!",
          "Outrageous!",
          "Wow!",
          "Spectaculous!",
          "You rock!",
          "On fire!"
     ]
     magic_word = ""
     
     # Constructor (reading the word_list file and add all words into a list).
     # The word_list file must be in the script dir.
     def __init__(self):
          with open("word_list.txt", "r") as f:
               for word in f.read().split('\n'):
                    self.__word_list.append(word)
     
     # Get the number of lives left.
     @property
     def lives(cls):
          return cls.__hearts
     
     # Setting up the game -> Get yourself a nickname in it :)
     def NewGame(self, nickname):
          self._nickname = nickname
          __hearts = 6
          # Select a random word from the list and mark it as magic_word.
          self.magic_word = random.choice(self.__word_list)
          # Preparation ready, starting.
          self.StartGame()
          
     # Game start.
     def StartGame(self):
          print(f"Good luck {self._nickname} guessing this word!")
          gameOver = False
          ch = [] # player's character list.

          # The game runs 'til game over (word guessed or lives = 0).
          while not gameOver:
               # Firstly, we assume that the player has guessed the magic_word.
               word_found = True # word guessed.
               # If a character is found in the magic_word.
               word_occurence_found = False # if finds a match.
               
               # Printing the word building.
               for c in self.magic_word:
                    if c in ch: # If match found.
                         print(c, end='')
                    else: # empty spaces.
                         print('_', end='')
                         word_found = False # If there's found even one blank space, it means the word hasn't been found yet.
               print('\n')
               
               # Checks if the player guessed a character or not and then check if the player guessed the word entirely.
               if len(ch) > 0 and ch[-1] in self.magic_word: # if player-input character match found in magic_word.
                    print(random.choice(self.__congrats_sentences)) # cheer the player.
                    word_occurence_found = True # mark match found.
               if word_occurence_found == False and len(ch) > 0: # if incorrect guess.
                    self.__hearts -= 1
               if self.lives == 0 or word_found == True: # if game over.
                    gameOver = True
                    break
               
               # Inform the player how many lives he has left.
               print(f"You have {self.lives} lives left!")
               # Ask and wait for input.
               ch.append(input("Your desired character is: "))
               # Infinite while-loop prevents bugs if the player gives an already existent character.
               while True:
                    # check if last added character is not in the entire list.
                    if ch[-1] not in ch[:-1] and len(ch) > 0: # if user input character is a new one (OK).
                         break
                    else: # is already used then remove and try again (BAD).
                         ch.pop(-1) # remove last input from list.
                         ch.append(input("Character used before! Try a new one: "))

          # Game Over.
          self.CheckWin(self.lives) # parsing the lives left
     
     # Checking the win
     def CheckWin(self, winner):
          # according the lives left, if there are more than 0 lives is a winner, otherwise the player lost.
          if winner == 0:
               print(f"You lost! The word was: {self.magic_word}")
          if winner > 0:
               print(f"CONGRATS {self._nickname}!! You won with {self.lives} lives left! The word was: {self.magic_word}")
        
          
# MAIN Entry.
if __name__ == '__main__':
     hInstance = Hangman() # Create a new instance of the class
     hInstance.NewGame("Your_Name_Here") # Set your name as parameter.
# list of words to be used
words = ["bat", "cat", "dogs", "mouse", "donkey"]

# select a random word from the list
import random
word = random.choice(words)

# create a list of underscores the same length as the word to represent the 
# letters that have not been guessed yet
guesses = ["_" for letter in word]

# set the number of remaining chances to 6
chances = 6

# start the game loop
while chances > 0:
  # print the current state of the word
  print(" ".join(guesses))
  
  # prompt the user to guess a letter
  letter = input("Guess a letter: ")
  
  # check if the letter is in the word
  if letter in word:
    # if it is, update the list of guesses with the correct letter
    for i in range(len(word)):
      if word[i] == letter:
        guesses[i] = letter
  else:
    # if it is not, decrease the number of chances
    chances -= 1
  
  # check if the word has been guessed
  if "_" not in guesses:
    print("You won! The word was", word)
    break

# if the loop has exited, the player has run out of chances
if "_" in guesses:
  print("You lost! The word was", word)
import random # a library to implement randomess

# ask the user for his or her name
name = input("What is your name? ")

print("Good Luck!", name)

# word bank
words = ['rainbow', 'color', 'skittles', 'cat', 'dog', 'keyboard']

# choose a random word from bank
word = random.choice(words)

print("Guess the characters")

# the guesses that the user has guessed
guesses = ''
# number of turns
turns = 12

# # output length of the random word
# for char in word:
#     print("_")

# logic for the game
while turns > 0:
     # count the number of times the user fails
     failed = 0

     # go through every char in the chosen word
     for char in word:
         if char in guesses:
             print(char)
         else:
             print("_")
             failed += 1

     if failed == 0:
         print("You Win!")

         print("The word is: ", word)
         break

     guess = input("guess a character: ")

     # each guess is stored in a string, guesses
     guesses += guess

     # check input with the characters in random word
     if guess not in word:
         turns -= 1
         print("Wrong!")
         # print number of turns left
         print("You have " + str(turns) + " more guesses")

         if turns == 0:
             print("You lost!")

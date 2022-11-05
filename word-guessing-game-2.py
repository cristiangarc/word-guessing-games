import random

words = ['which', 'paint', 'table', 'lense', 'glass', 'piano', 'mouse']

# define a function that checks if each character in a given word is present in
# a second word. print a green character if the char is in the same position in both words,
# print yellow if character is in second word but in a different position, and print black
# otherwise
def wordsMatch(givenW, guessW):
    # iterate through each index of the given word
    for i in range(len(givenW)):
        # green character
        if givenW[i] == guessW[i]:
            print('green')
        # yellow
        elif givenW[i] in guessW:
            print('yellow')
        # black
        else:
            print("black")

    if givenW == guessW:
        return 1
    else:
        return 0

# main class
random_word = random.choice(words)
print("Let's Play Wordle!")
message, i = {0:"Marvellous", 1:"Excellent", 2:"Very good",
3:"Nice", 4:"Good", 5:"Ok"}, 6

while i > 0:
    input_word = input('Enter a 5-letter word: ')
    i -= 1
    if (len(input_word) == 5 and input_word.isalpha()):
        if wordsMatch(input_word, random_word):
            print(message[i])
    else:
        print("Please enter a valid word")

print("End of game, the correct word is: " + random_word)

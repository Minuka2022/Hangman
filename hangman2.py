
import random

word_list = ["aardvark" , "baboon","camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f"psst, the solution is {chosen_word}")



#Create an empty list called display
#For each letter in chosen_word, add a "_" to "display"
#So if the chosen_word was "apple", display should be ["_","_","_","_","_"] with 5 "_" represnting each letter to guess

display = []

word_length =  len(chosen_word)

for letter  in range (word_length):
    display += "_"


guess = input("Guess a letter: ").lower()

#TO-2 Loop through each position in the chosen_word
#If the letter at that position matches "guess" then reveal that letter in the display at the position.
#e.g If the user guessed "P" and the chose_word was "apple", then display should be ["_", "p", "p", "_", "_"].


for position in range(word_length):
    letter = chosen_word[position]

    print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")

    #TO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

print(display)

word_list  = ["advaark" ,"baboon","camel"]

import random

chosen_word = random.choice(word_list)


guess = input("enter letter: ")


for letter in chosen_word:
    if letter == guess:
        print("correct")
    else:
        print("wrong")

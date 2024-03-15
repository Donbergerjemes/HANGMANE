import random
stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]

import word

chosen_word=random.choice(word.word_list)

lives=6

from art import logo
print(logo)

print(f"psst word is {chosen_word}")

display=[]

word_length=len(chosen_word)

for _ in range(word_length):
    display+="_"
print(display)

End=False
while not End:
    guess=input("gess a letter :").lower()
    if guess in display:
        print(f"you've already guessed this letter {guess}")
    for positon in range(word_length):
        letter=chosen_word[positon]
        
        if letter==guess:
          display[positon]=letter
    print(display)
    if guess not in chosen_word:
        print("you've guessed {guess} that's not in the word you lose a life")
        lives-=1
        if lives==0:
            End=True
            print("you loose")
    if "_"  not in display:
        end=True
        print("you won ")
    from art import stages
    print(stages[lives])

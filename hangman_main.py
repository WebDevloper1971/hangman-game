import random
from hangman_stages import stages
from hangman_words import words_list

word = random.choice(words_list)

wordlist = []
blank_list = []

for letter in word:
    wordlist.append(letter)

for letter in wordlist:
    blank_list.append("_")

# print(wordlist)
# print(blank_list)

lives = 10
end_game = False


def winner(letter_list):
    count = 0
    for character in letter_list:
        if character == "_":
            count += 1

    if count == len(letter_list):
        return True
    else:
        return False


# def find_letter(letter_list, character):
#     found = False
#     for i in range(0, len(letter_list)):
#         if letter_list[i] == character:
#             found = True
#             break
#     return found


print(f"your given word is : {blank_list} .")
while not end_game:

    if winner(wordlist):
        print("You Win !!")
        print(f"your given word is : {word} .")
        break
    elif lives == 0:
        print("You Lose !!")
        print(f"your given word is : {word} .")
        break
    else:
        guess = input("guess a letter : ")

        if guess == "exit":
            print("\nYou exited. You Lose. You are dead \n")
            print(stages[-1])
            break

        if wordlist.__contains__(guess):
            blank_list[wordlist.index(guess)] = guess
            wordlist[wordlist.index(guess)] = "_"
            print("\nYou guessed correct. Keep it up !! \n\n\n")
            print(f"{blank_list}\n")
        else:
            lives -= 1
            print(f"{blank_list}\n")
            print("You guessed wrong. You lose a life !! ")
            print(stages[len(stages) - lives - 1])




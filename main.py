#Step 5 
from tkinter import *
from tkinter import messagebox
import random

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
from hangman_words import word_list
window = Tk()
def playgame():
    window.destroy()
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)

    end_of_game = False
    lives = 6

    #TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
    #from hangman_art import logo
    #print(logo)

    #Testing code
    #print(f'Pssst, the solution is {chosen_word}.')

    #Create blanks
    display = []
    for _ in range(word_length):
        display += "_"

    while not end_of_game:
        print("the wordlength is ",word_length)
        guess = input("Guess a letter: ").lower()

        #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
        if guess in display:
            print("You've already guessed "+ guess)

        #Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
            if letter == guess:
                display[position] = letter

        #Check if user is wrong.
        if guess not in chosen_word:
            #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose. The word was "+chosen_word)
                

        #Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")

        #Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("You win.")
# ---------------------------- UI SETUP ------------------------------- #



def gui():
    
    window.title("Password Manager")
    window.config(padx=50, pady=50)

    canvas = Canvas(height=200, width=200)
    logo_img = PhotoImage(file="download.png")
    canvas.create_image(100, 100, image=logo_img)
    canvas.grid(row=0, column=1)

    #Labels

    email_label = Label(text="Enter your name:")
    email_label.grid(row=2, column=0)


    #Entries

    email_entry = Entry(width=35)
    email_entry.grid(row=2, column=1, columnspan=2)
    email_entry.focus()


    # Buttons

    add_button = Button(text="Play", width=26, command=playgame)
    add_button.grid(row=4, column=1, columnspan=2)

    window.mainloop()

gui()
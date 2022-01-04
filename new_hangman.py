from tkinter import messagebox
from tkinter import *
import random


window = Tk()
window.title("Hangman")
window.resizable(0, 0)

word_list = ['UNIVERSITY','COUNTRY','FREELANCING','POSITIVITY','NATURAL','COMEDY',
             'EXCELLENT','OUTSTANDING',"CROCODILE","STRAWBERRY"]

photos = [PhotoImage(file="1.png"),PhotoImage(file="2.png"),PhotoImage(file="3.png"),
          PhotoImage(file="4.png"),PhotoImage(file="5.png"),PhotoImage(file="6.png"),PhotoImage(file="7.png")]


def play():
    global spaced_word
    global tries
    tries = 0
    imgLabel.config(image=photos[0])
    random_word = random.choice(word_list)
    spaced_word = " ".join(random_word)
    lblWord.set(" ".join("_" * len(random_word)))
def guess(event):
    letter_to_guess = txtWord.get().upper()
    txtWord.set("")
    global tries
    if tries < 6:
        txt = list(spaced_word)
        print(txt)
        guessed = list(lblWord.get())
        if spaced_word.count(letter_to_guess) > 0:
            for c in range(len(txt)):
                if txt[c] == letter_to_guess:
                    guessed[c] = letter_to_guess
                lblWord.set("".join(guessed))
                if lblWord.get() == spaced_word:
                    messagebox.showinfo("Hangman", "You guessed it!")
                    play()

        else:
            tries += 1
            print(tries)
            imgLabel.config(image=photos[tries])
            if tries == 6:
                messagebox.showwarning("Hangman", "Game over")
imgLabel = Label(window)
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady= 40)
imgLabel.config(image=photos[0])

lblWord=StringVar()
Label(window, textvariable=lblWord, font=("Consolas 24 bold")).grid(row=0, column=3, columnspan=6, padx=10)

txtWord=StringVar()
Entry(window, textvariable=txtWord, font=("Consolas 24 bold")).grid(row=1, column=6, columnspan=2, padx=10)
window.bind('<Return>', guess)


Button(window, text="New\nGame", command=lambda:play(), font=("Helvetica 10 bold")).grid(row=3, column=8, sticky="NSWE")

play()
window.mainloop()
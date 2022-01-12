from tkinter import messagebox
from tkinter import *
import random

#creating window
window = Tk()
window.title("Food Hangman Game!")
#window.config(bg="#C64B86")

#This is the word list for all the potential words in the game
word_list = ["PASTA","CHOCOLATE","ICECREAM","PIZZA","APPLE","BEANS","POPCORN",
             "GRAPES","BREAD","CHEESE","BANANA","CRACKERS","PANCAKES",
             "GINGER","CARROT","CHEESCAKE","SALAD","WATERMELLON","BAGEL",
             "PUDDING","NOODLES","CASHEW"]

#A list to load all the images
photos = [PhotoImage(file="1.png"),PhotoImage(file="2.png"),PhotoImage(file="3.png"),
          PhotoImage(file="4.png"),PhotoImage(file="5.png"),PhotoImage(file="6.png"),
          PhotoImage(file="7.png")]


#when you click run or new game, the play function gets called to start the game

def play():
    
    #this variable holds the letters for the answer word for underscores
    global spaced_word   #we want to keep it global so it can be used at any time
    global tries     
    tries = 0
    #this is there to show the stand of hangman at the beginning 
    img_label.config(image=photos[0])
    #chooses a random word from the list
    chosen_word = random.choice(word_list) 
    #join is a predefined function that helps you to join all the elements in list to give a string and 
    #creates space between the random word that the computer has chosen (question)
    spaced_word = " ".join(chosen_word)
    #displaying as many blanks with the # of letters in the chosen word and creates space between so doesnt look like an underline (answer)
    label_word.set(" ".join("_" * len(chosen_word)))
    

#this function checks if your guess is correct or wrong
def guess(event): #on the event of pressing the enter key it calls tyhe function
    #use upper pre-defined function to change all letters guessed into upper because world list is in upper case
    letter_guessed = text_word.get().upper()  #get retrieves the data from text input
    text_word.set("") #this clears the text input
    global tries
    if tries < 6:
        text = list(spaced_word) #will convert the spaced word into a list so can be used to examine each letter
        
        guessed = list(label_word.get()) #will convert the label word into a list so can be used to examine each letter
        
        cnt = 0 #this is a counter
        for each_letter in spaced_word:
            if each_letter == letter_guessed:
                cnt = cnt+1
        #print("count from counter ",cnt)
        if cnt > 0:
            
            c = 0
            while( c <len(text)): # we are checking in which position we should put the letter that we guessed correctly
                if text[c] == letter_guessed:
                    guessed[c] = letter_guessed
                label_word.set("".join(guessed)) 
                
                if label_word.get() == spaced_word:
                    messagebox.showinfo("Food Hangman", "You guessed it!")
                    play()
                c = c+1

        else:
            tries = tries + 1
            img_label.config(image=photos[tries])
            if tries == 6:
                messagebox.showwarning("Food Hangman", "Game over")
            return tries
        
#gui tkinter

game_title=Label(window,text="Welcome to Food Hangman! ",font=("Arial 24 bold")).grid(row=0,column=0,columnspan=2)

img_label = Label(window)
img_label.grid(row=1, column=0, pady= 10)
img_label.config(image=photos[0])


#Displays the blank spaces for the word
label_word=StringVar()
Label(window, textvariable=label_word, font=("Arial 24 bold")).grid(row=1, column=1, columnspan=1)


entry_letter_title=Label(window,text="Enter a letter: ",font=("Arial 18 bold")).grid(row=2,column=0) 

#This is to get the users guess
text_word=StringVar()
Entry(window, textvariable=text_word, font=("Arial 20 bold")).grid(row=2, column=1,pady=10,padx=10)



#game_title.place(anchor="center")

#NumOfWrongGuessesLabel=Label(window,text="Number of wrong guesses: "+ str(tries)).grid(row=1,column=2)

#We are binding the return (enter) key and the guess function
window.bind('<Return>', guess)
messagebox.showinfo('Hangman Game Rules', 'game deatils')
window.focus_force()
#To start off the new game
Button(window, text="New\nGame", command=lambda:play(), bg="#C64B86",font=("Arial 12 bold")).grid(row=4, column=1,columnspan=1)

play()
window.mainloop()

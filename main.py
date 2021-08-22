from tkinter import *
from dictionary import dictinary
import random

RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


wpm=0
word=random.choice(dictinary)
words=[]
words.append(word)

#Resets timer, score
def start_timer():
    wpm=0
    words_count.config(text=f"{wpm}")
    new_word = random.choice(dictinary)
    words.append(new_word)
    canvas.itemconfig(word_text, text=new_word, font=(FONT_NAME, 25, "bold"))
    count_down(60)

#Timer function
def count_down(count):
    global game_on
    game_on=True
    timer_count.config(text=f"{count}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        game_on=False
        canvas.itemconfig(word_text, text=f"Final score {wpm}/minute", font=(FONT_NAME, 17, "bold"))

window = Tk()
window.title("Typing speed test")
window.config(padx=25, pady=25, bg=YELLOW)

#Function bind on 'Enter' key
def func(event):
    global wpm
    #Score function
    if game_on:
        new_word = random.choice(dictinary)
        words.append(new_word)
        #Compare entry content with the word generated after last key press
        if input.get() == words[-2]:
            wpm +=1
            words_count.config(text=f"{wpm}")
        #Delete content in entry
        input.delete(0, 'end')
        canvas.itemconfig(word_text, text=new_word, font=(FONT_NAME, 25, "bold"))

window.bind('<Return>', func)

#----------GUI config----------
canvas = Canvas(width=320, height=223, bg=RED, highlightthickness=0)
word_text=canvas.create_text(160, 112, text=words[-1], fill=GREEN, font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=0, columnspan=6)

words_label = Label(text="Words:", fg=RED, bg=YELLOW, font=(FONT_NAME, 14, "bold"))
words_label.grid(row=0, column=0, sticky='w')

words_count = Label(text="0", fg=RED, bg=YELLOW, font=(FONT_NAME, 14, "bold"))
words_count.grid(row=0, column=0, sticky='e')

timer_label = Label(text="Time:", fg=RED, bg=YELLOW, font=(FONT_NAME, 14, "bold"))
timer_label.grid(row=0, column=2, sticky='e')

timer_count = Label(text="00", fg=RED, bg=YELLOW, font=(FONT_NAME, 14, "bold"))
timer_count.grid(row=0, column=3,  sticky='w')

start_buton = Button(text="Start", fg=RED, bg=YELLOW, font=(FONT_NAME, 10, "bold"), command=start_timer)
start_buton.grid(row=0, column=5, sticky='e')

input = Entry(width=53, justify="center")
input.grid(row=2, column=0, columnspan=6)




window.mainloop()
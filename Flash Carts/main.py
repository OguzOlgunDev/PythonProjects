from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
print(to_learn)

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text = "French",fill="black")
    canvas.itemconfig(card_word,text = current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=cardfront_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text =current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=cardback_image)








# -------------------GUI-------------------------
window = Tk()
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
window.title("Flash Card")
canvas = Canvas(width=800,height=526,bg="bisque")
flip_timer = window.after(3000, func=flip_card)
cardfront_image = PhotoImage(file="images/card_front.png")
cardback_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400,263,image=cardfront_image)
card_title = canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)



rigth_image = PhotoImage(file="images/right.png")
right_button = Button(image=rigth_image ,highlightthickness=0,command=next_card)
right_button.config(bg=BACKGROUND_COLOR,highlightthickness=0)
right_button.grid(row=1,column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image,highlightthickness=0,command=next_card)
wrong_button.config(bg=BACKGROUND_COLOR,highlightthickness=0)
wrong_button.grid(row=1,column=0)

next_card()



window.mainloop()
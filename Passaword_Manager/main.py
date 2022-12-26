from tkinter import *
import random
from tkinter import messagebox
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']




def password_generator():
    letter_num = int(pas_let_entry.get())
    number_num = int(pas_num_entry.get())
    symbol_num = int(pas_sym_entry.get())
    passaword = ""

    #generating a random letter passaword
    for number in range(0,letter_num):
        rand_int = random.randint(0, len(letters) - 1)
        passaword += letters[rand_int]

    #generating a random symbol passaword
    for number in range(0, symbol_num):
        rand_int = random.randint(0, len(symbols) - 1)
        passaword += symbols[rand_int]

    #generating a random number passaword
    for number in range(0, number_num):
        rand_int = random.randint(0, len(numbers) - 1)
        passaword += numbers[rand_int]

    # Mixing the letter number and symbol part of passaword,
    # e.g   123asd%&     1a2%&sd3
    passowerd_mix = ""
    listed_passowerd = list(passaword)
    last_idx = len(passaword) - 1
    for number in range(0, len(passaword)):
        rand_int = random.randint(0, last_idx)
        last_idx = last_idx - 1
        passowerd_mix += listed_passowerd[rand_int]
        listed_passowerd.pop(rand_int)

    entery_text = StringVar()
    passoword_entery.config(textvariable=entery_text)
    entery_text.set(passowerd_mix)




# ---------------------------- SAVE PASSWORD ------------------------------- #




def save_file():
    website_info = website_entery.get()
    email_info = eml_usr_entery.get()
    pass_info = passoword_entery.get()
    new_data = {website_info:{
        "email": email_info,
        "passaword": pass_info
    }}

    if len(email_info) == 0 or len(pass_info) == 0:
        messagebox.showinfo(message="You must enter e-mail and passowerd")

    else:
        is_ok = messagebox.askokcancel(message=f"These are the details entered: \nEmail: {email_info}"
                                       f"\nPassaword: {pass_info}")

        if is_ok:

            with open(file="Saved Passowerds.json", mode="r") as passjson:
                data = json.load(passjson)
                data.update(new_data)

            with open(file="Saved Passowerds.json", mode="w") as passjson:
                json.dump(data, passjson, indent=4)


# ---------------------------- Read Passaword ------------------------------- #

def read_file():
    with open(file="Saved Passowerds.json", mode="r") as passtxt:
        a = json.load(passtxt)
        print(a)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
canvas = Canvas(height=200,width=200,background="white",highlightthickness=0)
window.config(padx=50,pady=50,background="white")
window.title("Passoword Manager")
my_image = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=my_image)
canvas.grid(row=2,column=1)

# labels

website_lab = Label(text="Website:",background="white",width=30,height=2)
website_lab.grid(row=3,column=0)

eml_usr_lab = Label(text="Email/Usurname:",background="white",width=30,height=2)
eml_usr_lab.grid(row=4,column=0)

passoword_lab = Label(text="Password:",background="white",width=30,height=2)
passoword_lab.grid(row=5,column=0)


pas_let_lab = Label(text="Letter",background="antique white")
pas_let_lab.place(x=0,y=0)


pas_num_lab = Label(text="Number",background="antique white")
pas_num_lab.place(x=0,y=50)

pas_sym_lab = Label(text="Symbol",background="antique white")
pas_sym_lab.place(x=0,y=100)


# Entiries

website_entery = Entry(width=31,bg="yellow")
website_entery.grid(row=3,column=1)


eml_usr_entery = Entry(width=50,bg="yellow")
eml_usr_entery.grid(row=4,column=1,columnspan=2)

passoword_entery = Entry(width=31,bg="yellow")
passoword_entery.grid(row=5,column=1)



pas_let_entry = Entry(width=3,bg="azure")
pas_let_entry.place(x=70,y=0)
pas_let_entry.insert(0,"6")


pas_num_entry = Entry(width=3,bg="azure")
pas_num_entry.place(x=70,y=50)
pas_num_entry.insert(0,"3")


pas_sym_entry = Entry(width=3,bg="azure")
pas_sym_entry.place(x=70,y=100)
pas_sym_entry.insert(0,"1")


# Buttons
pass_generate_button = Button(text="Generate Passoword",background="white",command=password_generator,width=15)
pass_generate_button.grid(row=5,column=2)

add_button = Button(text="Add",background="white",width=43,command=save_file)
add_button.grid(row=6,column=1,columnspan=2)

search_button = Button(text="Search",background="white",command= read_file,width=15)
search_button.grid(row=3,column=2)






window.mainloop()
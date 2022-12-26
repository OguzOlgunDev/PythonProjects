import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

reps = 0
timer = None



# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global reps
    reps = 0
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg="red")
    canvas.itemconfig(timer_text, text=f"00:00")



# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
   global reps
   WORK_MIN = float(work_min_entery.get())
   SHORT_BREAK_MIN = float(short_break_entery.get())
   LONG_BREAK_MIN = float(long_break_entery.get())

   work = WORK_MIN*60
   work_sec = int(work)

   short_break= SHORT_BREAK_MIN* 60
   short_break_sec = int(short_break)

   long_break = LONG_BREAK_MIN * 60
   long_break_sec = int(long_break)

   if reps%2 ==0 :
        count_down(work_sec)
        timer_label.config(text="Work", fg="red")
        canvas.config(bg="pink")
        window.config(bg="pink")
        timer_label.config(bg="pink")
        work_min_label.config(bg="pink")
        short_break_label.config(bg="pink")
        long_break_label.config(bg="pink")
        check_label.config(text="", bg="pink", font=(FONT_NAME))

   if reps%2 ==1 and reps != 7 :
        count_down(short_break_sec)
        timer_label.config(text="Break", fg="red")
        canvas.config(bg="blue")
        window.config(bg="blue")
        timer_label.config(bg="blue")
        work_min_label.config(bg="blue")
        short_break_label.config(bg="blue")
        long_break_label.config(bg="blue")
        check_label.config(text="", bg="pink", font=(FONT_NAME))

   if reps  == 7 :
        reps = 0
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg="red")
        check_label.config( bg="pink", font=(FONT_NAME))

   reps += 1
   print(reps)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(sec):

    count_min = math.floor(sec/60)
    count_sec = sec % 60
    if sec != 0:
        for seg in range(0,10):
            if count_sec == seg:
                count_sec = f"0{count_sec}"




    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if sec>0:
        global timer
        timer = window.after(100,count_down,sec-1)
    if sec ==0:
        start_timer()
        work_session = math.floor(reps/2)
        check_mark =""
        for i in range (work_session):
            check_mark += " ✔ "
        check_label.config(text =check_mark, bg=GREEN, font=(FONT_NAME))
        if check_mark =="":
            check_label.config(text=check_mark, bg="pink", font=(FONT_NAME))



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro App")
window.config(pady=100,padx=50,bg="pink")

canvas = Canvas(height=224,width=200,bg="pink",highlightthickness=0)


work_min_label = Label(text="Work Time Min",bg="pink",font=("italic",10))
work_min_label.grid(column=0,row=0)

short_break_label = Label(text="Short Break Min",bg="pink",font=("italic",10))
short_break_label.grid(column=0,row=1)

long_break_label = Label(text="Long Break Min",bg="pink",font=("italic",10))
long_break_label.grid(column=0,row=2)

work_min_entery = Entry(width=10)
work_min_entery.grid(column=1,row=0)

short_break_entery = Entry(width=10)
short_break_entery.grid(column=1,row=1)

long_break_entery = Entry(width=10)
long_break_entery.grid(column=1,row=2)





check_label = Label(bg="pink",font=(FONT_NAME))
check_label.grid(row=7,column=2)

timer_label = Label(text="Timer",bg="pink",fg="red",font=(FONT_NAME,35,"bold"))
timer_label.grid(column=2,row=4)


tomata_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112 ,image = tomata_img)
timer_text =canvas.create_text(100,130,text="",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=5,column=2)



start = Button(text="Start",bg=YELLOW,width=(10),command = start_timer)
start.grid(row=6,column=1)

reset = Button(text="Reset",bg=YELLOW,width=(10), command = reset)
reset.grid(row=6,column=3)

window.mainloop()
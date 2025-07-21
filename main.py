from tkinter import*
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    
    if WORK_MIN == 0:
        pass
    count_down(1 * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
        
            
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        root.after(1000, count_down,count -1)
# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Pomodoro")
root.config(padx=100,pady=50,bg=YELLOW)

label = Label(text="Timer",fg="#0EB072",bg=YELLOW,font=("",50))
label.grid(column=1,row=0)

tomato_img = PhotoImage(file="tomato.png")

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(100,112, image = tomato_img)
timer_text = canvas.create_text(102,130,text="00:00",fill="white",font=(FONT_NAME, 35,"bold"))
canvas.grid(column=1,row=1)


tik_mark = Label(text="✓",fg="#0EB072",bg=YELLOW)
tik_mark.grid(row=4,column=1)

start = Button(text="Start",bd=2,command=start_timer)
start.grid(row=2,column=0)

reset = Button(text="Reset",bd=2,fg="red")
reset.grid(row=2,column=3)


root.mainloop()
from tkinter import*
import math
# ---------------------------- CONSTANTS ------------------------------- #
BLUE = "#130bed"
RED = "#d90429"
GREEN = "#386641"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    root.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    tik_mark.config(text="")
    global reps
    reps = 0
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text= "Break", fg= RED)
    elif reps % 2 == 0:   
        count_down(short_break_sec)
        label.config(text= "Break",fg=BLUE)
    else:
        count_down(work_sec)
        label.config(text="Work",fg= GREEN)
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    
        
            
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = root.after(1000, count_down,count -1)
    else:
        start_timer()
        mark = ""
        work_sessions = (math.floor(reps/2))
        for _ in range(work_sessions):
            mark += "✔"
        tik_mark.config(text=mark)
            
# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
# root.minsize(480,600)
root.title("Pomodoro")
root.config(padx=100,pady=50,bg=YELLOW)

label = Label(text="Time",fg="#0EB072",bg=YELLOW,font=("",50))
label.grid(column=1,row=0)

tomato_img = PhotoImage(file="tomato.png")

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(100,112, image = tomato_img)
timer_text = canvas.create_text(102,130,text="00:00",fill="white",font=(FONT_NAME, 35,"bold"))
canvas.grid(column=1,row=1)


tik_mark = Label(fg=GREEN,bg=YELLOW)
tik_mark.grid(row=4,column=1)

start = Button(text="Start",bd=2,command=start_timer)
start.grid(row=2,column=0)

reset = Button(text="Reset",bd=2,fg="red",command=reset_timer)
reset.grid(row=2,column=3)


root.mainloop()
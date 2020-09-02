from tkinter import *
import random
import time
import keyboard
from tkinter import messagebox
from ball import *
from paddle import *

score = 0
tk = None
score_now = 1
canvas = None

tk = Tk()
tk.title("Bounce the Ball..")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

paddle = Paddle(canvas, 'cyan')
ball = Ball(canvas, paddle, 'red', 'red')
# global score_now
score_now = canvas.create_text(430, 20, text="Your score: " + str(score), fill = "red", font=("Arial", 14))

while 1:          
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
        canvas.itemconfig(score_now, text="Your score: " + str(score))
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)


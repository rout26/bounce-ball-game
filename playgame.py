from tkinter import *
import random
import time
import keyboard
from tkinter import messagebox
from ball import *
from paddle import *
import score

tk = Tk()
tk.title("Bounce the Ball..")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

paddle = Paddle(canvas, 'cyan')
ball = Ball(canvas, paddle, 'red', 'red')

def print_score():
    # global count
    canvas.itemconfig(score_board_id, text="Your score: " + str(score.count))

def game_over():
    canvas.itemconfig(game_over_id, text="Game over!")


score_board_id = canvas.create_text(430, 20, text="Your score: " + str(score.count), fill = "red", font=("Arial", 14))
game_over_id = canvas.create_text(250, 150, text=" ", fill="red", font=("Arial", 40))

while 1:          
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
        print_score()              
    else:
        game_over()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

# if __name__=="__main__":
#     main()


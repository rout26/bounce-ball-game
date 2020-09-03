from tkinter import *
import random
import time
import keyboard
from tkinter import messagebox
from ball import *
from paddle import *
import config

def main():
    tk = Tk()
    tk.title("Bounce the Ball..")
    tk.resizable(0, 0)
    tk.wm_attributes("-topmost", 1)
    canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
    canvas.pack()
    tk.update()

    paddle = Paddle(canvas, 'cyan')
    # ball = Ball(canvas, paddle, 'red', 'red')

    def print_score():
        # global count
        canvas.itemconfig(score_board_id, text="Your score: " + str(config.count))

    def game_over():
        canvas.itemconfig(game_over_id, text="GAME OVER!!!", font=("Helvatika", 40))
        canvas.itemconfig(restart_msg_id, text="Press 'Up Arrow Key' to restart...")
        config.lost = False

        # ball.hit_bottom = True
        # canvas.bind_all("<KeyPress-Up>", start_game) 
        # tk.mainloop()

    score_board_id = canvas.create_text(430, 20, text="Your score: " + str(config.count), fill = "red", font=("Arial", 14))
    game_over_id = canvas.create_text(250, 150, text="Press Up Arrow to Start the Game.", fill="blue", font=("Arial", 16))
    restart_msg_id = canvas.create_text(250, 200, text=" ", fill="blue", font=("Helvatika", 16))
    def start_game(event):
        if(event.keysym == 'Up'and config.lost == False):
            config.lost = True
            config.count = 0
            print_score()  
            ball = Ball(canvas, paddle, 'red', 'red')
            canvas.itemconfig(game_over_id, text=" ")
            canvas.itemconfig(restart_msg_id, text=" ")
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


    canvas.bind_all("<KeyPress-Up>", start_game) 

    tk.mainloop()


if __name__=="__main__":
    main()


# Packaging to exe
# python -m pip install pyinstaller
#pyinstaller --onefile 
    # optional
    # pyinstaller --onefile --windowed myscript.py
    # pip install --default-timeout=100 future
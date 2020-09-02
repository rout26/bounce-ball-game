from tkinter import *
import random
import time
import keyboard
from tkinter import messagebox
from ball import *
from paddle import *
import score

def main():
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
        canvas.itemconfig(game_over_id, text="GAME OVER!!!", font=("Helvatika", 40))


    score_board_id = canvas.create_text(430, 20, text="Your score: " + str(score.count), fill = "red", font=("Arial", 14))
    game_over_id = canvas.create_text(250, 150, text="Press 'Up Arrow Key' to Start... ", fill="red", font=("Helvatika", 16))

    def start_game(event):
        if(event.keysym == 'Up'):
            score.count = 0
            print_score()
            canvas.itemconfig(game_over_id, text=" ")
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


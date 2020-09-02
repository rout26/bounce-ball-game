from tkinter import *
import random
import time
import keyboard
from tkinter import messagebox
#from playgame import *


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
    
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        # print(pos)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0    


    def turn_left(self, evt):
        self.x = -5
    def turn_right(self, evt):
        self.x = 5 


    
# def exitmenu():
#     global tk
#     res = messagebox.askquestion("Gave Over","Do you wanrt to play again?", icon = 'warning') 
#     if res == 'yes':
#         main()   
#     else:
#         tk.destroy()
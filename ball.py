from tkinter import *
import random
import time
import keyboard
from tkinter import messagebox
import config


class Ball:
    
    def __init__(self, canvas, paddle, color, outline_color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 30, 30, fill=color, outline=outline_color)
        self.canvas.move(self.id, 245, 100) #move the ball to middle of the canvas. 
        # self.x = 0
        # self.y = -1
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False
        
        
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        # print(pos)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            # Ball dont bounce if hit the bottom
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:               
            self.y = -4
            config.count = config.count + 1
            print(config.count)
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

    
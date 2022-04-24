from tkinter import Button
import random
import settings

class Cell:
    all = []

    def __init__(self, x, y, is_mine = False):
        self.is_mine = is_mine
        self.x = x
        self.y = y
        self.btn_object = None

        Cell.all.append(self)
    
    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4
        )
        btn.bind('<Button-1>', self.onLeftClick) # Left Button Click
        btn.bind('<Button-3>', self.onRightClick) # Right Button Click
        self.btn_object = btn
    
    def onLeftClick(self, event):
        if self.is_mine:
            self.show_mine()

    def show_mine(self):
        # A logic to show mine and interrupt the game
        self.btn_object.configure(bg='red')

    def onRightClick(self, event):
        print(event)
        print('Right')

    @staticmethod
    def generate_mines():
        picked_cell = random.sample(
            Cell.all, 
            settings.MINES_COUNT
        )
        for cell in picked_cell:
            cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x},{self.y})"


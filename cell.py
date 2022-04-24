from tkinter import Button

class Cell:
    def __init__(self, is_mine = False):
        self.is_mine = is_mine
        self.btn_object = None
    
    def create_btn_object(self, location):
        btn = Button(
            location,
            text='Text'
        )
        btn.bind('<Button-1>', self.onLeftClick)
        btn.bind('<Button-3>', self.onRightClick)
        self.btn_object = btn
    
    def onLeftClick(self, event):
        print(event)
        print('Left')

    def onRightClick(self, event):
        print(event)
        print('Right')



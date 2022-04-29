from tkinter import Button, Label
import random
import settings

class Cell:
    all = []
    cell_count = settings.CELLS_COUNT
    counter_object = None

    def __init__(self, x, y, is_mine = False):
        self.is_mine = is_mine
        self.x = x
        self.y = y
        self.btn_object = None
        self.is_shown = False
        self.is_marked = False

        Cell.all.append(self)
    
    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            font=("", 10)
        )
        btn.bind('<Button-1>', self.onLeftClick) # Left Button Click
        btn.bind('<Button-3>', self.onRightClick) # Right Button Click
        self.btn_object = btn

    @staticmethod
    def create_cell_counter(location):
        lbl = Label(
            location,
            bg='black',
            fg='white',
            width=12,
            height=4,
            text=f"Cells Left: {Cell.cell_count}",
            font=("", 16)
        )
        Cell.counter_object = lbl
    
    def onLeftClick(self, event):
        if not self.is_marked:
            if self.is_mine:
                self.show_mine()
            else:
                if self.surrounding_mines_count == 0:
                    self.show_surrounding()
                self.show_cell()
        else:
            pass

    def show_surrounding(self):
        for cell in self.surrounding_cells:
            if cell.is_shown == False:
                cell.show_cell()
                if(cell.surrounding_mines_count == 0):
                    cell.show_surrounding()

    def show_mine(self):
        # A logic to show mine and interrupt the game
        self.btn_object.configure(bg='red')
        self.btn_object.configure(state='disabled')

    def get_cell_by_axes(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounding_cells(self):
        cells = []
        for x in range(self.x - 1, self.x + 2):
            for y in range(self.y - 1, self.y + 2):
                if x != self.x or y != self.y:
                    cells.append(self.get_cell_by_axes(x, y))

        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounding_mines_count(self):
        count = len(
            [cell for cell in self.surrounding_cells if cell.is_mine == True])
        return count

    def show_cell(self):
        Cell.cell_count -= 1
        self.is_shown = True
        self.btn_object.configure(text=self.surrounding_mines_count)
        if Cell.counter_object:
            Cell.counter_object.configure(
                text=f"Cells Left: {Cell.cell_count}")

    def onRightClick(self, event):
        if not self.is_marked:
            self.btn_object.configure(
                bg='orange'
            )
            self.btn_object.configure(state='disabled')
            self.is_marked = True
        else:            
            self.btn_object.configure(
                bg='SystemButtonFace'
            )
            self.btn_object.configure(state='active')
            self.is_marked = False

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


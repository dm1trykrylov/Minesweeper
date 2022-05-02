from tkinter import *
from cell import Cell
import settings
import utils

root = Tk()
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper")
#root.resizable(False, False)


top_frame = Frame(
    root,
    bg='black',
    width=settings.WIDTH,
    height=utils.height_prct(25)
)
top_frame.place(x=0,y=0)

game_title = Label(
    top_frame,
    bg = 'black',
    fg='white',
    text='Minesweeper Game',
    font=('', 36)
)

game_title.place(x=utils.width_prct(25), y=0)

left_frame = Frame(
    root,
    bg='black',
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)
left_frame.place(x=0,y=utils.height_prct(25))


center_frame = Frame(
    root,
    bg='black',
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)
center_frame.place(x=utils.height_prct(25), y=utils.height_prct(25))


#generate field
for row in range(settings.GRID_SIZE):
    for col in range(settings.GRID_SIZE):
        c = Cell(col, row)
        c.create_btn_object(center_frame)
        c.btn_object.grid(
            column=col, row=row
        )

Cell.generate_mines()

Cell.create_cell_counter(left_frame)

Cell.counter_object.place(
    x=0, y=0
)
#Run the window
root.mainloop()
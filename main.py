from tkinter import *
import settings

root = Tk()
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper")
#root.resizable(False, False)


top_frame = Frame(
    root,
    bg='red',
    width=settings.WIDTH,
    height=settings.HEIGHT
)
top_frame.place(x=0,y=188)

left_frame = Frame(
    root,
    bg='blue',
    width=settings.WIDTH,
    height=settings.HEIGHT
)
top_frame.place(x=0,y=188)

#Run the window
root.mainloop()
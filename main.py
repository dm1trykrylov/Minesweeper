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
    width=1440,
    height=180
)
top_frame.place(x=0,y=188)

left_frame = Frame(
    root,
    bg='blue',
    width=1440,
    height=180
)
top_frame.place(x=0,y=188)

#Run the window
root.mainloop()
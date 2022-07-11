from tkinter import *
from PIL import Image,ImageTk
import pyautogui
wn = Tk()


def start_rape():
    for _ in range(9):
        pyautogui.press("r")
        print("raped")




icon = PhotoImage(file="img.png")
wn.geometry("349x345")
wn.title("Discord Raper")
wn.iconphoto(True,icon)
wn.config(
    background="black"
)

img = Image.open("img.png")
resize_image= img.resize((250,150), Image.ANTIALIAS)
newimg = ImageTk.PhotoImage(resize_image)





hi = Label(wn,
           text="Discord ScreenShare Raper",
           font=("Arial",15),
           fg='#8f1810',
           bg='black',
           image=newimg,
           compound='top'
           ).pack()

but = Button(wn,
            text="Start ✔",
            command=start_rape,
            font=('Comic Sans',15),
            fg='#006903',
            bg='black'
            ).pack(side=LEFT)


wn.mainloop()

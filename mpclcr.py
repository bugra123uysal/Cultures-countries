import tkinter as tk
from PIL import Image, ImageTk

tt=tk.Tk()

tt.geometry("900x1200")

rsm=Image.open(r"c:\Users\buğra\Desktop\512px-_Political_World__CIA_World_Factbook_map_2005.svg.png")

üi=ImageTk.PhotoImage(rsm)

llbl=tk.Label(tt,image=üi)
llbl.place(x=20, y=80)





tt.mainloop()


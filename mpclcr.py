import tkinter as tk
from PIL import Image, ImageTk

def page_ss(page):  
    pagea.pack_forget()
    pageb.pack_forget()

    page.pack()





tt=tk.Tk()

tt.geometry("900x1200")

tr=tk.Label(tt, text="türkiye")
tr.place(y=1, x=1200)
almr=tk.Label(tt, text="almanya")
almr.place(y=22, x=1200)

""" sayfalar """

""" sayfa 1 """
pagea=tk.Frame(tt)
syfpage=tk.Label(pagea, text="1. sayfa")
syfpage.pack()
abutton=tk.Button(pagea, text="2. sayfaya geç", command=lambda:page_ss(pageb))
abutton.pack()


""" sayfa 2 """
pageb=tk.Frame(tt)
syfpage=tk.Label(pageb, text="2. sayfa")
syfpage.pack()


bbutton=tk.Button(pageb, text="1. sayfaya git", command=lambda: page_ss(pagea))
bbutton.pack()


rsm=Image.open(r"c:\Users\buğra\Desktop\Ekran görüntüsü 2024-08-11 024141.png")

üi=ImageTk.PhotoImage(rsm)

llbl=tk.Label(tt,image=üi)
llbl.place(x=20, y=80)

pagea.pack()



tt.mainloop()


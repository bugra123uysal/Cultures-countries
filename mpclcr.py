import requests
from bs4 import BeautifulSoup
import tkinter as tk

tt=tk.Tk()

tt.geometry("500x800")
llbl=tk.Label(tt)
llbl.place(x=20, y=80)

urll="https://ufukavrupa.org.tr/tr/interactive-world-map"
a=requests.get(urll)
b=a.content
c=BeautifulSoup(b,"html.parser")

d=c.find_all('div', class_="jvectormap-container" )

ıımg=[xxx['src']for xxx in d if 'src' in xxx.attrs]
print(ıımg)
   




tt.mainloop()


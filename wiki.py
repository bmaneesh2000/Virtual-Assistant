import wikipedia
from tkinter import *
from tkinter.messagebox import showinfo
win=Tk()
win.title("wiki")
win.geometry('200x70')

def search_wiki():
    search=entry.get()
    answer=wikipedia.summary(search)
    showinfo("Wikipedia Answer",answer)

lable=Label(win,text="wiki search :")
lable.grid(row=4,column=0)

entry=Entry(win)
entry.grid(row=3,column=0)

button=Button(win,text="Search",command=search_wiki)
button.grid(row=1,column=1,padx=10)

win.mainloop()
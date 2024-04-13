from tkinter import *
import sqlite3 as sql

con = sql.connect('chipi.db')
cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS fullname(id INTEGER PRIMARY KEY, lastname TEXT, firstname TEXT, age INT)')
con.commit()


def sudo_heck_write():
    cur.execute('INSERT INTO fullname(lastname, firstname, age) VALUES(?,?,?)', (strF.get(), strF2.get(), strF3.get()))
    con.commit()


'кот-программа'

root = Tk()
root.geometry('400x300+300+300')
labelF = Label(text='Lastname')
labelF.grid(column=0, row=0)

strF = StringVar()
editF = Entry(textvariable=strF)
editF.grid(column=1, row=0)

labelF2 = Label(text='Firstname')
labelF2.grid(column=2, row=0)

strF2 = StringVar()
editF2 = Entry(textvariable=strF2)
editF2.grid(column=3, row=0)

labelF3 = Label(text='Age')
labelF3.grid(column=4, row=0)

strF3 = IntVar()
editF3 = Entry(textvariable=strF3)
editF2.grid(column=5, row=0)

bts = Button(text='Write', command=sudo_heck_write)
bts.bind('<Button-1>')
bts.grid(column=6, row=int(0/2))

root.mainloop()


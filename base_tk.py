from tkinter import *
import sqlite3 as sql

con = sql.connect('chipi.db')
cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS fullname(id INTEGER PRIMARY KEY, lastname TEXT, firstname TEXT)')
con.commit()


def sudo_heck_write():
    cur.execute('INSERT INTO fullname(id, lastname, firstname) VALUES(?,?,?, ', (strF, strF2))
    con.commit()

'''  
 $ sudo heck beluga
 $ sudo heck beluga
 $ sudo heck beluga
 $ sudo heck beluga
 $ sudo heck beluga
 $ sudo heck beluga
 $ sudo heck beluga
 $ sudo heck beluga
 $ sudo heck beluga
'''

frame = Frame()
labelF = Label(text='Фамилия')
labelF.grid(column=0, row=0)

strF = StringVar()
editF = Entry(textvariable=strF)
editF.grid(column=0, row=1)

labelF2 = Label(text='Имя')
labelF2.grid(column=0, row=2)

strF2 = StringVar()
editF2 = Entry(textvariable=strF2)
editF2.grid(column=0, row=3)

bts = Button(text='Записать')
bts.bind('<Button-1>', )
bts.grid(column=0, row=9)

frame.mainloop()

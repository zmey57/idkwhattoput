from tkinter import *
import sqlite3 as sql


def kit_write():
    kit.execute('INSERT INTO store(name, mfg_date ,exp_date, price, amount) VALUES(?,?,?,?)', (name_var.get(), mfgdate_var.get(), expdate_var.get(), price_var.get(), amount_var.get()))
    cat.commit()


def kit_update_price():
    for i in kit.execute('SELECT name,price FROM store'):
        kit.execute(f'UPDATE store SET price = "{price_var}" WHERE name = "{name_var}"')
        cat.commit()


cat = sql.connect('dubi.db')
kit = cat.cursor()

kit.execute('CREATE TABLE IF NOT EXISTS store(id INTEGER PRIMARY KEY, name TEXT, mfg_date TEXT, exp_date TEXT, price REAL, amount INTEGER )')
cat.commit()

root = Tk()
root.geometry('500x300+100+100')

name_var = StringVar()
name_label = Label(text='Name of the product:')
name_edit = Entry(textvariable=name_var)

price_var = IntVar()
price_label = Label(text='Price:')
dollar_label = Label(text='$')
price_edit = Entry(textvariable=price_var)

mfgdate_var = StringVar()
mfgdate_label = Label(text='Mfg date:')
mfgdate_edit = Entry(textvariable=mfgdate_var)

expdate_var = StringVar()
expdate_label = Label(text='Exp date:')
expdate_edit = Entry(textvariable=expdate_var)

amount_var = IntVar()
amount_label = Label(text='Amount:')
pieces_label = Label(text='pieces')
amount_edit = Entry(textvariable=amount_var)


kitwritebutton = Button(text='Write', command=kit_write)
kitwritebutton.bind('<Button-1>')

kitupdatebutton = Button(text='Update', command=kit_update_price)
kitupdatebutton.bind('<Button-1>')

name_label.grid(row=0, column=0)
name_edit.grid(row=0, column=1)
mfgdate_label.grid(row=1, column=0)
mfgdate_edit.grid(row=1, column=1)
expdate_label.grid(row=2, column=0)
expdate_edit.grid(row=2, column=1)
price_label.grid(row=3, column=0)
price_edit.grid(row=3, column=1)
dollar_label.grid(row=3, column=2)
amount_label.grid(row=4, column=0)
amount_edit.grid(row=4, column=1)
pieces_label.grid(row=4, column=2)
kitwritebutton.grid(row=5, column=0)
kitupdatebutton.grid(row=5, column=1)

root.mainloop()
kit.close()
cat.close()

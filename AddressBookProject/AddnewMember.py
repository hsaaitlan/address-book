from tkinter import *
import Loggedin as Li


def add_new_member(master, namee):
    master.destroy()
    addwin = Tk()
    name = StringVar()
    cellnum = IntVar()
    cellnum.set('')
    addwin.title('Add Members')
    addwin.geometry('400x400+%d+%d' % (addwin.winfo_screenwidth()/2-200, addwin.winfo_screenheight()/2-200))
    addback = PhotoImage(file='add_back.png')
    addimg = PhotoImage(file='addbutton.png')
    canvas = Canvas(addwin, width=400, height=400)
    canvas.create_image(0, 0, anchor=NW, image=addback)
    canvas.pack()
    namelabel = Label(canvas, text='Name', bg='sky blue')
    namelabel.config(font=('Segoe Print', 14))
    namelabel.place(x=20, y=30, width=80, height=30)
    nameentry = Entry(canvas, textvariable=name)
    nameentry.config(font=('Segoe Print', 14))
    nameentry.place(x=120, y=25, height=40, width=250)
    addrlabel = Label(canvas, text='Address', bg='sky blue')
    addrlabel.config(font=('Segoe Print', 14))
    addrlabel.place(x=20, y=80, width=80, height=30)
    addrentry = Text(canvas)
    addrentry.config(font=('Segoe Print', 14))
    addrentry.place(x=120, y=70, width=250, height=60)
    celllabel = Label(canvas, text='Mobile \nNumber', bg='sky blue')
    celllabel.place(x=20, y=140, width=80, height=60)
    celllabel.config(font=('Segoe Print', 14))
    cellentry = Entry(canvas, textvariable=cellnum)
    cellentry.config(font=('Segoe Print', 14))
    cellentry.place(x=120, y=155, width=250, height=30)

    def add_into_data():
        if len(str(cellnum.get())) != 10:
            addwin.title('Enter valid Mobile Number')
        else:
            with open('C:\\Users\\Pankaj Bhardwaj\\PycharmProjects\\AddressBookProject\\.idea\\dictionaries\\Data\\'
                      'address' + namee.get() + '.txt', 'a') as f:
                f.write('\n')
                f.write(name.get())
                f.write('\n')
                f.write(str(cellnum.get()))
                f.write('\n')
                f.write(addrentry.get('1.0', 'end -1c'))
                f.write('\n&&&')
                f.close()
            Li.logged_in(addwin, namee)
    addbutton = Button(canvas, image=addimg, command=add_into_data)
    addbutton.place(x=170, y=350, width=60, height=30)
    addwin.mainloop()

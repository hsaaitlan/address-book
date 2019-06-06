from tkinter import *
import Loggedin as Li


def show_members(master, namee):
    master.destroy()
    show = Tk()
    show.title(namee.get()+"'s Data")
    frame = Frame(show, width=600, height=600)
    frame.pack()
    scrollbar = Scrollbar(frame, orient=VERTICAL)
    scrollbar.pack(side=RIGHT, fill=Y)
    showimg = PhotoImage(file='show_back.png')
    quitimg = PhotoImage(file='exit.png')
    show.geometry('600x600+%d+%d' % (show.winfo_screenwidth()/2-300, show.winfo_screenheight()/2-300))
    canvas = Canvas(frame, height=600, width=600)
    canvas.create_image(0, 0, anchor=NW, image=showimg)
    canvas.pack()
    label1 = Label(canvas, text='Name', bg='#1b3e7a', fg='white')
    label2 = Label(canvas, text='Address', bg='#1b3e7a', fg='white')
    label3 = Label(canvas, text='Phone Number', bg='#1b3e7a', fg='white')
    label1.place(x=70, y=20, width=50, height=20)
    label2.place(x=270, y=20, width=80, height=20)
    label3.place(x=445, y=20, width=130, height=20)
    try:
        f = open('C:\\Users\\Pankaj Bhardwaj\\PycharmProjects\\AddressBookProject\\.idea\\dictionaries\\Data\\'
                 'address' + namee.get() + '.txt', 'r')
        data = f.readlines()
        length = len(data)
        listboxname = Listbox(canvas)
        listboxname.config(font=('Segoe Print', 12))
        listboxaddr = Listbox(canvas, font=('Segoe Print', 12))
        listboxcell = Listbox(canvas, font=('Segoe Print', 12))
        j = 0
        count = 0
        for i in range(0, length):
            if j == 0:
                j = j+1
            elif j == 1:
                listboxname.insert(END, data[i])
                j = j + 1
            elif j == 3:
                if data[i] == "&&&\n" or data[i] == '&&&':
                    for j in range(0, count-1):
                        listboxname.insert(END, '\n')
                        listboxcell.insert(END, '\n')
                    listboxname.insert(END, '----------------')
                    listboxaddr.insert(END, '-------------------------')
                    listboxcell.insert(END, '-------------')
                    j = 1
                    count = 0
                else:
                    listboxaddr.insert(END, data[i])
                    count = count+1
            elif j == 2:
                listboxcell.insert(END, data[i])
                j = j+1
            else:
                j = 1
                pass
        listboxname.place(x=15, y=50, width=160, height=450)
        listboxaddr.place(x=185, y=50, width=250, height=450)
        listboxcell.place(x=445, y=50, width=130, height=450)
        scrollbar.config(command=listboxname.yview)
        scrollbar.config(command=listboxaddr.yview)
        scrollbar.config(command=listboxcell.yview)

        def yscrollname(*args):
            if listboxaddr.yview() != listboxname.yview() or listboxcell.yview() != listboxname.yview():
                listboxaddr.yview_moveto(args[0])
                listboxcell.yview_moveto(args[0])
            scrollbar.set(*args)

        def yscrolladdr(*args):
            if listboxname.yview() != listboxaddr.yview() or listboxcell.yview() != listboxaddr.yview():
                listboxname.yview_moveto(args[0])
                listboxcell.yview_moveto(args[0])
            scrollbar.set(*args)

        def yscrollcell(*args):
            if listboxname.yview() != listboxcell.yview() or listboxaddr.yview() != listboxcell.yview():
                listboxname.yview_moveto(args[0])
                listboxaddr.yview_moveto(args[0])
            scrollbar.set(*args)

        listboxaddr.config(yscrollcommand=yscrolladdr)
        listboxname.config(yscrollcommand=yscrollname)
        listboxcell.config(yscrollcommand=yscrollcell)
    except FileNotFoundError:
        show.title('No members yet')

    def go_back():
        Li.logged_in(show, namee)

    closebutton = Button(canvas, image=quitimg, command=go_back)
    closebutton.place(x=275, y=550, width=50, height=30)
    show.mainloop()

from tkinter import *
import AddnewMember as anm
import ShowMembers as sm


def logged_in(master, namee):
    master.destroy()
    loggedin = Tk()
    pic = PhotoImage(file='show_members.png')
    img = PhotoImage(file='addmember.png')
    qimg = PhotoImage(file='exit_button.png')
    loggedin.geometry('400x400+%d+%d' % (loggedin.winfo_screenwidth()/2-200, loggedin.winfo_screenheight()/2-200))
    loggedin.title('Logged in as: '+namee.get())
    canvas = Canvas(loggedin, width=400, height=400, bg='black')
    canvas.pack()
    label = Label(canvas, text='Welcome to your \n Address Book '+namee.get())
    label.config(font=('Segoe Print', 14), bg='black', fg='red')
    label.place(x=30, y=30, width=340, height=100)

    def add_mem():
        anm.add_new_member(loggedin, namee)

    def show_mem():
        sm.show_members(loggedin, namee)

    addbutton = Button(canvas, image=img, command=add_mem)
    addbutton.place(x=125, y=150, width=130, height=40)
    showbutton = Button(canvas, image=pic, command=show_mem)
    showbutton.place(x=140, y=210, width=100, height=45)
    quitbutton = Button(canvas, image=qimg, command=quit)
    quitbutton.place(x=280, y=330, width=80, height=39)
    loggedin.mainloop()

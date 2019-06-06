from tkinter import *
import Loggedin as Li
import DeCode as Dc


def log_in(master):
    master.destroy()
    login = Tk()
    login.title('Log In')
    loginname = StringVar()
    loginpasswrd = StringVar()
    pic = PhotoImage(file='contacts.png')
    img = PhotoImage(file='login_button.png')
    canvas = Canvas(login, width=400, height=400)
    canvas.create_image(0, 0, anchor=NW, image=pic)
    canvas.pack()
    winwidth = login.winfo_screenwidth()
    winheight = login.winfo_screenheight()
    login.geometry('400x400+%d+%d' % (winwidth / 2 - 200, winheight / 2 - 200))
    namelabell = Label(canvas, text='Enter your username', font=('Segoe Print', 14))
    namelabell.place(x=80, y=20, width=240, height=40)
    nameentryy = Entry(canvas, textvariable=loginname, fg='green', font=('Segoe Print',14, 'bold italic'))
    nameentryy.place(x=100, y=70, width=180, height=40)
    passlabell = Label(canvas, text='Enter Password', font=('Segoe Print', 14))
    passlabell.place(x=80, y=130, width=240, height=40)
    passentryy = Entry(canvas, textvariable=loginpasswrd, fg='green', show='*', font=('Segoe Print', 14, 'bold italic'))
    passentryy.place(x=100, y=180, width=180, height=40)

    def log_in():
        try:
            with open('logindetails' + loginname.get() + '.txt', 'r') as f:
                data = f.readlines()
                f.close()
            uname = ''
            unamee = data[0].rsplit()
            length = len(unamee)
            uname = unamee[0]
            for i in range(1, length):
                uname = uname + ' ' + unamee[i]
            upass = ''
            unamee = data[1].rsplit()
            length = len(unamee)
            upass = unamee[0]
            for i in range(1, length):
                upass = upass + ' ' + unamee[i]
            if loginname.get() == Dc.de_code(uname):
                if loginpasswrd.get() == Dc.de_code(upass):
                    Li.logged_in(login, loginname)
                else:
                    login.title('Wrong password. Try Again')
        except FileNotFoundError:
            login.title('Invalid Username')
    loginbutton = Button(canvas, image=img, command=log_in)
    loginbutton.place(x=160, y=330, width=80, height=48)
    login.mainloop()

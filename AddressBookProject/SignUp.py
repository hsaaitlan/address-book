from tkinter import *
import LogIn as Li
import EnCode as Ec


def sign_up(master):
    master.destroy()   # Closes the previous window
    signup = Tk()
    signup.title('Sign Up')  # Title of Sign Up Window
    pic = PhotoImage(file='signup_win.png')
    img = PhotoImage(file='signup_button.png')
    canvas = Canvas(signup, width=400, height=400)
    canvas.create_image(0, 0, anchor=NW, image=pic)
    canvas.pack()
    signupname = StringVar()
    signuppasswrd = StringVar()
    signup.geometry('400x400+%d+%d' % (signup.winfo_screenwidth()/2-200, signup.winfo_screenheight()/2-200))
    namelabel = Label(canvas, text='Enter your username', font=('Segoe Print', 14, 'bold'))
    nameentry = Entry(canvas, fg='navy blue', textvariable=signupname, font=('Segoe Print', 12))
    namelabel.place(x=80, y=50, width=240, height=40)
    nameentry.place(x=100, y=100, width=200, height=40)
    passlabel = Label(canvas, text='Enter desired password', font=('Segoe Print', 14, 'bold'))
    passentry = Entry(canvas, show='*', fg='navy blue', textvariable=signuppasswrd, font=('Segoe Print', 12))
    passlabel.place(x=80, y=160, width=240, height=40)
    passentry.place(x=100, y=210, width=200, height=40)

    def sign_up_click():
        with open('logindetails' + signupname.get() + '.txt', 'w') as f:
            s = Ec.en_code(signupname.get())
            f.write(s)
            f.write('\n')
            s = Ec.en_code(signuppasswrd.get())
            f.write(s)
            f.write('\n')
            f.close()
        Li.log_in(signup)
    signupbutton = Button(canvas, image=img, command=sign_up_click)
    signupbutton.place(x=300, y=340, width=80, height=48)
    signup.mainloop()

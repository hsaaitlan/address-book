from tkinter import *
import SignUp as Su
import LogIn as Li


win = Tk()
# Title of the main window
win.title('Address Book')
loginpic = PhotoImage(file="login_button.png")   # Login Button Image
signuppic = PhotoImage(file="signup_button.png")  # Signup Button Image
addrpic = PhotoImage(file="addr_book.png")  # Background Image
exitpic = PhotoImage(file='exit_button.png')  # Exit Button Image
canvas = Canvas(win, width=400, height=400)
canvas.create_image(0, 0, anchor=NW, image=addrpic)
canvas.pack()
winwidth = win.winfo_screenwidth()  # Width of the Screen
winheight = win.winfo_screenheight()  # Height of the Screen
win.geometry('400x400+%d+%d' % (winwidth/2-200, winheight/2-200))


def on_sign_up():   # When Singup Button is Clicked
    Su.sign_up(win)  # Calls sign_up Method of SignUp Module


def on_log_in():   # When Login Button is Clicked
    Li.log_in(win)  # Calls log_in Method of LogIn Module


signup = Button(win, image=signuppic, command=on_sign_up)
login = Button(win, image=loginpic, command=on_log_in)
signup.place(x=160, y=120, width=80, height=48)
login.place(x=160, y=180, width=80, height=48)
button = Button(win, image=exitpic, command=quit)
button.place(x=300, y=350, width=80, height=48)
win.mainloop()

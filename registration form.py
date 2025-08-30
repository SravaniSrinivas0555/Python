import tkinter

root=tkinter.Tk()
root.title('Login form')
root.geometry("500x550")
#root.configure(bg="#C4C7BA")

frame=tkinter.Frame()

#creating widgets
login_label=tkinter.Label(frame, text="Facebook", fg="#0D8BBD",font="arial 30")
username_label=tkinter.Label(frame, text="Username:",font="arial 15")
username_entry=tkinter.Entry(frame,font='arial 15')
password_label=tkinter.Label(frame, text="Password:",font="arial 15")
password_entry=tkinter.Entry(frame, show="*",font="arial 15")
Login_button_label=tkinter.Button(frame, text="Login", bg="#0D8BBD",fg="#110303",font="arial 15")
label_forgot=tkinter.Label(frame,text="Forgotten Password?",font='arial 15')
create_account=tkinter.Button(frame, text="Create a new account",font='arial 15',fg='#0D8BBD')

#placing widgets on screen
login_label.grid(row=0, column=0, columnspan=2,sticky="news",pady='30')
username_label.grid(row=1, column=0,pady="15")
username_entry.grid(row=1, column=1)
password_label.grid(row=2, column=0,pady="15")
password_entry.grid(row=2, column=1)
Login_button_label.grid(row=3, column=0, columnspan=2,pady="20")
label_forgot.grid(row=4,column=0,columnspan=2,pady="15")
create_account.grid(row=5,column=0,columnspan=2,pady="50")

frame.pack()


root.mainloop()

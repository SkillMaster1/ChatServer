"""
Jamil Busari
CS50AP
Period 4
MASTER PROJECT
SCHENK
APRIL 8 2019
"""
from tkinter import*
import socket
from connections import Database
from threading import Thread

def receive(s, messages):
    try:
        data = s.recv(1024)
        messages.insert(END, repr(data))
    except Exception as e:
        print(e)
    
#Function for calling sending method in class
def send(s,e1, messages,e):
    info = e1.get()
    s.send(info.encode('ascii'))
    messages.insert(END, "You: "+info)
    e.set("")
#Function for connecting to Server/ Calling class
def connect(root,user,passw):
    usr = user.get()
    psw = passw.get()
    work = Database(usr, psw)
    work.welcome()
    
    host ='localhost'
    port = 5000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    Newwin = Toplevel(root)

    text = Label(Newwin, text="Connected", fg="green")
    text.grid(row=1, column=1)
    
    windows = Frame(Newwin)
    windows.grid(row=1, column=0)

    #Holds Messages sent
    messages = Listbox(windows)
    messages.grid(row=1, column=1)
    
    e = StringVar()

    e1 = Entry(windows, textvariable=e)
    e1.grid(row=2, column=1)
    e1.bind('<Return>', lambda event:send(s,e1,messages,e))

    b1 = Button(windows, text="Send", bg="green", fg="white", command=lambda:send(s,e1, messages,e))
    b1.grid(row=2, column=2)

    rec_thread = Thread(target=receive, args=(s,messages,))
    rec_thread.start()
    

#Main Function
def main():
    root = Tk()
    root.configure(background='orange')
    root.title('Chat Server')

    #Creating title
    title = Label(root, text="CHAT SERVER", bg='orange', font=10)
    title.grid(row=0, column=5)

    #Sub Title
    sub_title = Label(root, text="VOLUME 1!", bg='orange', font=8)
    sub_title.grid(row=1, column=5)

    #Login Form
    nick = Label(root, text="Nickname:", bg="orange", font=4)
    nick.grid(row=2, column=5)
    user = Entry(root)
    user.grid(row=2, column=6)

    password = Label(root, text="Password", bg="orange", font=4)
    password.grid(row=3, column=5)
    passw = Entry(root)
    passw.grid(row=3, column=6)

    cre = Button(root, text="Create Account", bg="orange", fg="white")
    cre.grid(row=4, column=5)

    log = Button(root, text="Login", bg="#96D6FF", command=lambda:connect(root, user, passw))
    log.grid(row=4, column=7)

    

    
    
    root.mainloop()



if __name__ == "__main__":
    main()

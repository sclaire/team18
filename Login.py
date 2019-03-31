from tkinter import *
import tkinter.messagebox

StudentAccounts= {"Jake":"password","Antonia":"password1","Khadija":"password2","Sophie":"password3","Tim":"password4","Will":"password5"}
LecturerAccounts={"Helen":"password","Philipp":"password2"}

class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.userLabel = Label(self, text="Enter Your Username:",font=('Helvetica', 8))
        self.passwordLabel= Label(self, text="Enter Your Password Please:",font=('Helvetica', 8))
        self.usernameInput = Entry(self)
        self.passwordInput = Entry(self, show="*")#stars out the password being entered
        self.userLabel.grid(row=0)
        self.passwordLabel.grid(row=1)
        self.usernameInput.grid(row=0, column=1,pady=3)
        self.passwordInput.grid(row=1, column=1,pady=3)
        self.LecturerButton = Button(self, text="Login if you are a lecturer",font=('Helvetica', 8), command=self.lecturerclicked)
        self.LecturerButton.grid(columnspan=3,pady=3)
        self.StudentButton = Button(self, text="Login if you are a student",font=('Helvetica', 8), command=self.studentclicked)
        self.StudentButton.grid(columnspan=3, pady=3)
        self.RegisterButton = Button(self, text="Register for a student account",font=('Helvetica', 8), command=self.register)
        self.RegisterButton.grid(columnspan=3,pady=3)
        self.pack()

    def register(self):
        Username = self.usernameInput.get()#add validation
        Password = self.passwordInput.get()#add validation
        if Username in StudentAccounts:
            tkinter.messagebox.showinfo("Username Used", "This username is already in the system. Please try another name or login instead")
        else:
            StudentAccounts[Username]=Password
            tkinter.messagebox.showinfo("Register Sucess", "You have been registered and may now login")
            self.RegisterButton.grid_remove() #removes the register button once user has been registered
    
    def studentclicked(self):

        User = self.usernameInput.get()#validate
        Pass = self.passwordInput.get()#validate

        if User in StudentAccounts and Pass == StudentAccounts[User]:

            root.destroy()
            tkinter.messagebox.showinfo("Login Box", "Welcome " + User)
          #  exec(open(r"Student.py").read()) This opens the menu, commented out so can still run without file being present for moment
        else:
            tkinter.messagebox.showerror("Login Failed", "Check your username or password, as our system does not recognise these login details")    

    def lecturerclicked(self):

        User = self.usernameInput.get()#validate
        Pass = self.passwordInput.get()#validate

        if User in LecturerAccounts and Pass == LecturerAccounts[User]:
            root.destroy()
            tkinter.messagebox.showinfo("Login Box", "Welcome " + User)
           # exec(open(r"Lecturer.py").read())     This opens the menu, commented out so can still run without file being present for moment

        else:
            tkinter.messagebox.showerror("Login Failed", "Check your username or password, as our system does not recognise these login details")    


root = Tk()
root.title("Login")
root.resizable(0,0) 
root.geometry("300x150") 
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
app = LoginFrame(root)
root.mainloop()

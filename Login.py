from tkinter import * #relevant imports to python
import os
import tkinter.messagebox

class LoginFrame(Frame):
    def __init__(self, master): #tkinter initialisation
        super().__init__(master)
        
        self.userLabel = Label(self, text="Enter Your Username:",font=('Helvetica', 8)) #label for username field
        self.passwordLabel= Label(self, text="Enter Your Password Please:",font=('Helvetica', 8))#username input field
        self.usernameInput = Entry(self)
        self.passwordInput = Entry(self, show="*")#stars out the password being entered
        self.userLabel.grid(row=0)#formatting - all grid is formatting
        self.passwordLabel.grid(row=1)
        self.usernameInput.grid(row=0, column=1,pady=3)
        self.passwordInput.grid(row=1, column=1,pady=3)
        self.LecturerButton = Button(self, text="Login if you are a lecturer",font=('Helvetica', 8), command=self.lecturerclicked)#button clicked runs the lecturerclicked command
        self.LecturerButton.grid(columnspan=3,pady=3)
        self.StudentButton = Button(self, text="Login if you are a student",font=('Helvetica', 8), command=self.studentclicked)#if clicked runs student clicked
        self.StudentButton.grid(columnspan=3, pady=3)
        self.RegisterButton = Button(self, text="Register for a student account",font=('Helvetica', 8), command=self.register)#register will run
        self.RegisterButton.grid(columnspan=3,pady=3)
        self.pack() #pack formats all the fields and buttons together

    def register(self):
        Username = self.usernameInput.get()# username from form
        Password = self.passwordInput.get()# password from form

        studentfile=open("StudentAccount.txt","a")# opens student account file, with append 
        studentfile.write("\n"+ Username + " " + Password) #writes to the file new line the username and password, seperated by a space so the login process will work
        tkinter.messagebox.showinfo("Register Sucess", "You have been registered and may now login " + Username +".")#message saying registered
        self.RegisterButton.grid_remove() #removes the register button once user has been registered, the fields are now still filled so can just click to login
        #does allow for multiple registration but the login process means this doesnt matter as the real will still be set to 1 , just potentilly multiple times.

    
    def studentclicked(self): #checks if the student login is correct
        User = self.usernameInput.get()# takes the username from the form
        Pass = self.passwordInput.get()# takes the password from the form
        real=0 #initalised

        studentfile= open("StudentAccount.txt", "r") # opens the txt file with the login details as studentfile, read only
        for line in studentfile: #goes through each line
            line=line.split() # splits the line across 2 lines (each line in txt has the format username (space) password)
            if User == line[0]: # if the username on form matches the first line created (remeber starts from 0 in python)
                if Pass == line[1]: # if the password is on the second line created
                    real=1 #the variable real is set to 1 - i.e set to true as it is declared as false above

        if real==1 :#checks variable - so if the details were found this would be true
            root.destroy() #closes login
            tkinter.messagebox.showinfo("Login Box", "Welcome " + User) #shows welcome message and concenates with the username that has been entered
            exec(open(r"Student.py").read())# This opens the menu for student
        else:
            tkinter.messagebox.showerror("Login Failed", "Check your username or password, as our system does not recognise these login details.Please also check you clicked the correct login")    
            #if not correct user details, error message shows and returns to login page

    def lecturerclicked(self): # same as stduent login, just uses different text file
        User = self.usernameInput.get()# takes the username from the form
        Pass = self.passwordInput.get()# takes the password from the form
        real=0 #initalised

        lecturerfile= open("LecturerAccount.txt", "r") # opens the txt file with the login details as lecturerfile
        for line in lecturerfile: #goes through each line
            line=line.split() # splits the line across 2 lines (each line in txt has the format username (space) password)
            if User == line[0]: # if the username on form matches the first line created (remeber starts from 0 in python)
                if Pass == line[1]: # if the password is on the second line created
                    real=1 #the variable real is set to 1 - i.e set to true as it is declared as false above

        if real==1 :#checks variable - so if the details were found this would be true
            root.destroy() #closes login
            tkinter.messagebox.showinfo("Login Box", "Welcome " + User) #shows welcome message and concenates with the username that has been entered
            exec(open(r"Lecturer.py").read()) #This opens the menu file
        else:
            tkinter.messagebox.showerror("Login Failed", "Check your username or password, as our system does not recognise these login details. Please also check you clicked the correct login")    
            #if not correct user details, error message shows and returns to login page


root = Tk() #roots
root.title("Login") # window title
root.geometry("300x150")  #window size
root.columnconfigure(0, weight=1) #styling
root.rowconfigure(0, weight=1)# styling
app = LoginFrame(root) #roots
root.mainloop() #tkinter roots

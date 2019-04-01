from tkinter import *
import tkinter.messagebox as tkm
import csv

class createTest(Frame):

	def window(self):
		#Question text
		self.txtQ1 = StringVar()
		self.txtQ2 = StringVar()
		self.txtQ3 = StringVar()
		self.txtQ4 = StringVar()
		self.txtQ5 = StringVar()
		self.txtQ6 = StringVar()
		self.txtQ7 = StringVar()
		self.txtQ8 = StringVar()
		self.txtQ9 = StringVar()
		self.txtQ10 = StringVar()

		#Multiple choice answer text
		self.txtQ1a = StringVar()
		self.txtQ1b = StringVar()
		self.txtQ1c = StringVar()
		self.txtQ1d = StringVar()

		self.txtQ2a = StringVar()
		self.txtQ2b = StringVar()
		self.txtQ2c = StringVar()
		self.txtQ2d = StringVar()

		self.txtQ3a = StringVar()
		self.txtQ3b = StringVar()
		self.txtQ3c = StringVar()
		self.txtQ3d = StringVar()

		self.txtQ4a = StringVar()
		self.txtQ4b = StringVar()
		self.txtQ4c = StringVar()
		self.txtQ4d = StringVar()

		self.txtQ5a = StringVar()
		self.txtQ5b = StringVar()
		self.txtQ5c = StringVar()
		self.txtQ5d = StringVar()

		self.txtQ6a = StringVar()
		self.txtQ6b = StringVar()
		self.txtQ6c = StringVar()
		self.txtQ6d = StringVar()

		self.txtQ7a = StringVar()
		self.txtQ7b = StringVar()
		self.txtQ7c = StringVar()
		self.txtQ7d = StringVar()

		self.txtQ8a = StringVar()
		self.txtQ8b = StringVar()
		self.txtQ8c = StringVar()
		self.txtQ8d = StringVar()

		self.txtQ9a = StringVar()
		self.txtQ9b = StringVar()
		self.txtQ9c = StringVar()
		self.txtQ9d = StringVar()

		self.txtQ10a = StringVar()
		self.txtQ10b = StringVar()
		self.txtQ10c = StringVar()
		self.txtQ10d = StringVar()

		############################################################

		lblQ1 = Label(self, text = 'Q1.', font=('MS', 8,'bold'))
		lblQ1.grid(row=1, column= 1)
		self.Q1Entry = Entry(self)
		self.Q1Entry.grid(row=1,column=2)

		lblQ2 = Label(self, text = 'Q2.', font=('MS', 8,'bold'))
		lblQ2.grid(row=2, column= 1)
		self.Q2Entry = Entry(self)
		self.Q2Entry.grid(row=2,column=2)

		lblQ3 = Label(self, text = 'Q3.', font=('MS', 8,'bold'))
		lblQ3.grid(row=3, column= 1)
		self.Q3Entry = Entry(self)
		self.Q3Entry.grid(row=3,column=2)

		lblQ4 = Label(self, text = 'Q4.', font=('MS', 8,'bold'))
		lblQ4.grid(row=4, column= 1)
		self.Q4Entry = Entry(self)
		self.Q4Entry.grid(row=4,column=2)

		lblQ5 = Label(self, text = 'Q5.', font=('MS', 8,'bold'))
		lblQ5.grid(row=5, column= 1)
		self.Q5Entry = Entry(self)
		self.Q5Entry.grid(row=5,column=2)

		lblQ6 = Label(self, text = 'Q6.', font=('MS', 8,'bold'))
		lblQ6.grid(row=6, column= 1)
		self.Q6Entry = Entry(self)
		self.Q6Entry.grid(row=6,column=2)

		lblQ7 = Label(self, text = 'Q7.', font=('MS', 8,'bold'))
		lblQ7.grid(row=7, column= 1)
		self.Q7Entry = Entry(self)
		self.Q7Entry.grid(row=7,column=2)

		lblQ8 = Label(self, text = 'Q8.', font=('MS', 8,'bold'))
		lblQ8.grid(row=8, column= 1)
		self.Q8Entry = Entry(self)
		self.Q8Entry.grid(row=8,column=2)
	
		lblQ9 = Label(self, text = 'Q9.', font=('MS', 8,'bold'))
		lblQ9.grid(row=9, column= 1)
		self.Q9Entry = Entry(self)
		self.Q9Entry.grid(row=9,column=2)

		lblQ10 = Label(self, text = 'Q10.', font=('MS', 8,'bold'))
		lblQ10.grid(row=10, column= 1)
		self.Q10Entry = Entry(self)
		self.Q10Entry.grid(row=10,column=2)

		##############################################################

		



	def __init__(self, master):
		# Initialise Lecturer Class
		Frame.__init__(self, master)
		self.grid()
		self.window()




root = Tk()
root.title("This is shit")
root.resizable(0,0) 
root.geometry("400x400") 
app = createTest(root)
root.mainloop()
from tkinter import *


class EditQ(Frame):
	# GUI Setup
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()

class AddQ(Frame):
	# GUI Setup
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
class Assessment(Frame):



	def AddQ(self):
		t1 = Toplevel(root)
		AddQ(t1)

	def EditQ(self):
		
		t1 = Toplevel(root)
		EditQ(t1)
		
		self.butEditQ.grid_remove()

	def hideButtons(self):
		pass



	def createButtons(self):

		butEditQ = Button(self, text='Modify Question',font=('Helvetica', 8))
		butEditQ['command']=self.EditQ #Note: no () after the method
		butEditQ.grid(row=14, column=2, columnspan=2, padx=10, pady=10)

		butAddQ = Button(self, text='Add Question',font=('Helvetica', 8))
		butAddQ['command']=self.AddQ #Note: no () after the method
		butAddQ.grid(row=12, column=2, columnspan=2, padx=10, pady=10)



	# GUI Setup
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.createButtons()

class Lecturer(Frame):

	def AddQ(self):
		t1 = Toplevel(root)
		AddQ(t1)

	def EditQ(self):
		
		t1 = Toplevel(root)
		EditQ(t1)

	def viewStatistics(self):
		pass

	def createAssSelect(self):
		lblProg = Label(self, text='Degree Programme:', font=('MS', 8,'bold'))
		lblProg.grid(row=0, column=0, columnspan=2, sticky=NE )

		self.listProg = Listbox(self, height= 3)
		scroll = Scrollbar(self, command= self.listProg.yview) 
		self.listProg.configure(yscrollcommand=scroll.set)

		self.listProg.grid(row=0, column=2, columnspan=2, sticky=NE)
		scroll.grid(row=0, column=4, sticky=W) 

		for item in ["CS", "CS with", "BIS", "SE", "Joints",""]: 
			self.listProg.insert(END, item)

		self.listProg.selection_set(END)  

	def createButtons(self):

		butEditQ = Button(self, text='Modify Question',font=('Helvetica', 8))
		butEditQ['command']=self.EditQ #Note: no () after the method
		butEditQ.grid(row=12, column=2, columnspan=2, padx=10, pady=10)

		butAddQ = Button(self, text='Add Question',font=('Helvetica', 8))
		butAddQ['command']=self.AddQ #Note: no () after the method
		butAddQ.grid(row=10, column=2, columnspan=2, padx=10, pady=10)

		butviewStatistics = Button(self, text='View Statistics',font=('Helvetica', 8))
		butviewStatistics['command']=self.viewStatistics #Note: no () after the method
		butviewStatistics.grid(row=14, column=2, columnspan=2, padx=10, pady=10)  

	# GUI Setup
	def __init__(self, master):
		# Initialise Lecturer Class
		Frame.__init__(self, master)
		self.grid()
		self.createButtons()

root = Tk()
root.title("Lecturer Screen")
root.configure(background='black')
root.resizable(0,0) 
root.geometry("200x200") 
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
app = Lecturer(root)
root.mainloop()
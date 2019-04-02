from tkinter import *


class Formative(Frame):
	# GUI Setup
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()

class Summative(Frame):
	# GUI Setup
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
class Assessment(Frame):


	def summativeAssessment(self):
		t1 = Toplevel(root)
		Summative(t1)

	def formativeAssessment(self):
		
		t1 = Toplevel(root)
		Formative(t1)
		
		self.butFormative.grid_remove()

	def hideButtons(self):
		pass



	def createButtons(self):

		butFormative = Button(self, text='Formative',font=('Helvetica', 8))
		butFormative['command']=self.formativeAssessment #Note: no () after the method
		butFormative.grid(row=14, column=2, columnspan=2, padx=10, pady=10)

		butSummative = Button(self, text='Summative',font=('Helvetica', 8))
		butSummative['command']=self.summativeAssessment #Note: no () after the method
		butSummative.grid(row=12, column=2, columnspan=2, padx=10, pady=10)



	# GUI Setup
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.createButtons()

class Student(Frame):

	def summativeAssessment(self):
		t1 = Toplevel(root)
		Summative(t1)

	def formativeAssessment(self):
		
		t1 = Toplevel(root)
		Formative(t1)

	def viewFeedback(self):
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

		"""
		butAssessment = Button(self, text='Assessment',font=('Helvetica', 8))
		butAssessment['command']=self.takeAssessment #Note: no () after the method
		butAssessment.grid(row=12, column=2, columnspan=2, padx=10, pady=10)
		"""

		butFormative = Button(self, text='Formative',font=('Helvetica', 8))
		butFormative['command']=self.formativeAssessment #Note: no () after the method
		butFormative.grid(row=12, column=2, columnspan=2, padx=10, pady=10)

		butSummative = Button(self, text='Summative',font=('Helvetica', 8))
		butSummative['command']=self.summativeAssessment #Note: no () after the method
		butSummative.grid(row=10, column=2, columnspan=2, padx=10, pady=10)

		butViewFeedback = Button(self, text='View Feedback',font=('Helvetica', 8))
		butViewFeedback['command']=self.viewFeedback #Note: no () after the method
		butViewFeedback.grid(row=14, column=2, columnspan=2, padx=10, pady=10)  

	# GUI Setup
	def __init__(self, master):
		# Initialise Student Class
		Frame.__init__(self, master)
		self.grid()
		self.createButtons()

# Main
root = Tk()
root.title("Student Menu")
root.resizable(0,0) #Disallows resizing
root.geometry("200x200") #Fix the size of the window to 500x500
root.columnconfigure(0, weight=1) #I think these center, methods need further research
root.rowconfigure(0, weight=1)
app = Student(root)
root.mainloop()

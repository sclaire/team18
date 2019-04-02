from tkinter import *
import csv


def calcAverage(data):	
	dictionary = []
	for i in range (len(dictionary)):
		dictionary.append(list(data[i].items()))

	result = {}
	for i in range(3, 3+10):
		right = 0 
		score = 0
		for mark in dictionary:
			if mark[0][1] == '1':
				if mark[i][1] == '1':
					right = right + 1
					score = score + 1
				elif result[i][1] == '0':
					score = score + 1
		result[i-2] = round((right/score * 100), 2)
	return result

def mostIncorrect(dictionary):
	average = []
	for i in dictionary:
		average.append(dictionary[i])
	return(average.index(max(average))+1)



class Statistics(Frame):

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.master = master
		self.grid()
		self.init_window()
		self.assessment = "Example Assessment"
		self.score = opencsv(fileName)
		self.questionAverage = calcAverage(self.score)
		self.mostInc = mostIncorrect(self.questionAverage)
		#opencsv file

	def viewStatistics(self):
		title = Label(self, text = ("Percentage questions were answered correctly:\n for " + self.assessment), font = ('Helvetica', 8))
		title.grid(row = 0, column = 0, columnspan = 3)

		question1 = Label(self, text = ("Question 1: " + str(self.questionAverage[1] + "%"), font('Helvetica', 8)))
		question1.grid(row = 1, column = 0, columnspan = 3)

		question2 = Label(self, text = ("Question 2: " + str(self.questionAverage[2] + "%"), font('Helvetica', 8)))
		question2.grid(row = 2, column = 0, columnspan = 3)

		question3 = Label(self, text = ("Question 3: " + str(self.questionAverage[3] + "%"), font('Helvetica', 8)))
		question3.grid(row = 3, column = 0, columnspan = 3)

		question4 = Label(self, text = ("Question 4: " + str(self.questionAverage[4] + "%"), font('Helvetica', 8)))
		question4.grid(row = 4, column = 0, columnspan = 3)

		question5 = Label(self, text = ("Question 5: " + str(self.questionAverage[5] + "%"), font('Helvetica', 8)))
		question5.grid(row = 5, column = 0, columnspan = 3)

		question6 = Label(self, text = ("Question 6: " + str(self.questionAverage[6] + "%"), font('Helvetica', 8)))
		question6.grid(row = 6, column = 0, columnspan = 3)

		question7 = Label(self, text = ("Question 7: " + str(self.questionAverage[7] + "%"), font('Helvetica', 8)))
		question7.grid(row = 7, column = 0, columnspan = 3)

		question8 = Label(self, text = ("Question 8: " + str(self.questionAverage[8] + "%"), font('Helvetica', 8)))
		question8.grid(row = 8, column = 0, columnspan = 3)

		question9 = Label(self, text = ("Question 9: " + str(self.questionAverage[9] + "%"), font('Helvetica', 8)))
		question9.grid(row = 9, column = 0, columnspan = 3)

		question10 = Label(self, text = ("Question 10: " + str(self.questionAverage[10] + "%"), font('Helvetica', 8)))
		question10.grid(row = 10, column = 0, columnspan = 3)

		mostIncAns = Label(self, text = ("Question answered most incorrectly: Question " + str(self.mostInc)), font = ('Helvetica', 8))
		title.grid(row = 12, column = 0, columnspan = 3)

		root = Tk()

root.title("Statistics")
root.resizable(0,0) 
root.geometry("200x200") 
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
app = Lecturer(root)
root.mainloop()

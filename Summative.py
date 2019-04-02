from tkinter import *
import tkinter.messagebox
import csv

Answers=[]
question = []
options = [[], [], [], [], [], [], [], [], [], []]

with open('summative.csv', 'r') as csv_file:
    _data = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in _data:
        if line_count < 10:
            question.append(row[0])
            options[line_count].append(row[1])
            options[line_count].append(row[2])
            options[line_count].append(row[3])
            options[line_count].append(row[4])
            line_count += 1
        elif line_count == 10:
            for dts in row:
                Answers.append(int(dts))
            line_count += 1

    
class Summative:
    def __init__(self, master):
        self.questionNo = 0
        self.selected = IntVar()
        self.right = 0
        self.questions = self.PrintQuestion(master, self.questionNo) 
        self.option = self.radios(master,4)
        button = Button(master, text="Exit", command=self.Exit)
        button.pack(side=BOTTOM)
        button = Button(master, text="Save Answer", command=self.Check)
        button.pack(side=BOTTOM)        
        button = Button(master, text="Previous Question", command=self.Previous)
        button.pack(side=LEFT)
        button = Button(master, text="Next Question", command=self.Next)
        button.pack(side=RIGHT)
        self.ShowQuestion(self.questionNo)
        self.instantresult= Label(master, text='')
        self.instantresult.pack(side=BOTTOM, fill =X)

    def PrintQuestion(self, master, questionNo):
        Question = Label(master, text=question[questionNo])
        Question.pack(side=TOP)
        return Question


    def radios(self, master, n):
        answer = 0
        buttons = []
        while answer < n:
            Buttonn = Radiobutton(master, text="Please choose the right answer", variable=self.selected, value=answer + 1)
            buttons.append(Buttonn)
            Buttonn.pack(side=TOP, anchor="w")
            answer = answer + 1
        return buttons


    def ShowQuestion(self, questionNo):
        answer = 0
        self.selected.set(0)
        self.questions['text'] = question[questionNo]
        for op in options[questionNo]:
            self.option[answer]['text'] = op
            answer = answer + 1


    def answer(self, questionNo):
        if self.selected.get() == Answers[questionNo]:
            return True
        return False

    def Previous(self):
        if self.questionNo > 0:
            self.instantresult['text'] = ""
            self.questionNo = self.questionNo - 1;
            self.ShowQuestion(self.questionNo)
           

    def Next(self):
        if self.questionNo > 8:
            self.FinalResult()
        elif self.questionNo < 9:
            self.instantresult['text'] = ""
            self.questionNo = self.questionNo + 1;
            self.ShowQuestion(self.questionNo)
        
            
    
    def Exit(self):
         root.destroy()
        
    def Check(self):
        if self.answer(self.questionNo):
            self.instantresult['text'] = "Answer saved"
            self.right += 1
        else:
            self.instantresult['text'] = "Answer saved"
        
        
        


    def FinalResult(self):
        score = "Score: " + str(self.right) + " out of  " + str(len(question))
        tkinter.messagebox.showinfo("Final Result", score)
        root.destroy()
        


root = Tk()

root.resizable(0,0) 
root.geometry("600x200")
root.title("Summative Test")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
app = Summative(root)
root.mainloop()

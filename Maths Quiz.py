import random
from tkinter import *
from tkinter import Tk


class Math():
    def __init__(self, parent):
       
        self.index = 0
        self.score = 0
        global EnterName

        self.Welcome = Frame(parent)
        self.Welcome.configure(bg = "grey")
        self.Welcome.grid(row=0, column=0)
       
   
        self.TitleLabel = Label(self.Welcome, text = "Welcome",
                                bg = "black", fg = "white", width = 50, padx = 30,
                                pady = 10, font = ("14"))
        self.TitleLabel.grid(row = 0, columnspan = 2)

        self.MessageLabel = Label(self.Welcome, text = """Welcome to Maths Quiz
Please enter your name,
age, and difficulty level.
Thank you.""", bg = "grey", fg = "white", font = ("comic sans ms", "18"))
        self.MessageLabel.grid(row = 5, column = 0)
       
       
        self.LabelName = Label(self.Welcome, text = "Enter Name: ",
                               fg = "black", bg = "grey", padx = 5, pady = 5,
                               font = ("10"))
        self.LabelName.grid(row = 1, column = 1)
       
        self.EnterName = Entry(self.Welcome)
        self.EnterName.grid(row = 2, column = 1)
       
     
        self.LabelAge = Label(self.Welcome, text = "Enter Age: ",
                               fg = "black", bg = "grey", padx = 5, pady = 5,
                               font = ("10"))
        self.LabelAge.grid(row = 3, column = 1)
       
        self.EnterAge = Entry(self.Welcome)
        self.EnterAge.grid(row = 4, column = 1)

        self.WarningLabel = Label(self.Welcome, text = '', anchor = W, fg = "red", bg = "grey", width= 20, padx = 30, pady = 10)
        self.WarningLabel.grid(row = 5, column = 1)

        self.DifficultyLabel = Label(self.Welcome, text = 'Choose diffculity', anchor = W, fg = "black",bg = "grey", width= 14, padx = 30, pady = 20, font = ("12"))
        self.DifficultyLabel.grid(row = 6, column = 1)
       
        self.difficulty = ["Easy", "Medium", "Hard"]
        self.diff_lvl = StringVar()
        self.diff_lvl.set(0)
        self.diff_btns = []

        for i in range(len(self.difficulty)):
            rb = Radiobutton(self.Welcome, variable = self.diff_lvl, value = i, text = self.difficulty[i], anchor = W, padx = 50, width = "5", height = "2", bg = "grey",)
            self.diff_btns.append(rb)
            rb.grid(row = i+7, column = 1, sticky = NSEW)

   
        self.Return = Label(self.Welcome, fg = "red",bg = "grey",
                            font = ("10"))
        self.Return.grid(row = 5, column = 1)
        self.Return.configure(text = "")
       
     
        self.ToQuiz = Button(self.Welcome, text = "Next", bg = "grey",
                             activebackground = "light blue",
                             command = lambda:[self.UserDetails(), selfg.QuestionGenAdd()])
        self.ToQuiz.grid(row = 10, column = 1)
       
        global score
        global count
       
        score = 0
        count = 0
   
        self.Quiz = Frame(parent)
        self.Quiz.configure(bg = "grey")
       
     
        self.TitleLabel = Label(self.Quiz, text = "QUIZ",
                                bg = "black", fg = "white", width = 50, padx = 30,
                                pady = 10, font = ("14"))
        self.TitleLabel.grid(row = 0, columnspan = 2)
       
     
        self.Question = Label(self.Quiz, padx = 5, pady = 5, bg = "grey", font = ("10"))
        self.Question.grid(row = 1, column = 0)
       
 
        self.AnswerBox = Entry(self.Quiz)
        self.AnswerBox.grid(row = 1, column = 1)

        self.ScoreLabel = Label(self.Quiz, text = "", bg = "grey",)
        self.ScoreLabel.grid(row = 5, column =1)
       

        self.ButtonCheck = Button(self.Quiz, text = "Check question",
                            activebackground = "gray", bg = "grey",
                            command = self.Check)
        self.ButtonCheck.grid(row = 2, column = 0)
       

        self.feedback = Label(self.Quiz, padx = 5, pady = 5, bg = "grey", font = ("10"))
        self.feedback.grid(row = 2, column = 1)
       

        self.Score_Page = Frame(parent)
        self.Score_Page.configure(bg = "grey")

        self.TitleScore = Label(self.Score_Page, text = "YOUR SCORE",
                                bg = "Black", fg = "white", width = 30, padx = 30,
                                pady = 10, font = ("14"))
        self.TitleScore.grid(row = 0, columnspan = 2)

        self.BlankSpace = Label(self.Score_Page, text = "", bg = "grey")

        self.ScoreDisplay = Label(self.Score_Page, text = "Name:Liam          Score: 5/5",
                                   padx = 3, pady = 3, bg = "grey", font = ("comic sans ms", "22"))
        self.ScoreDisplay.grid(row = 1, column = 1)
       
       
       
    """FUNCTIONS"""

    def destroy(self):
        self.Quiz.grid_remove()
        self.Score_Page.grid()    
   
    def ShowQuiz(self):
 
        self.Welcome.grid_remove()
        self.Quiz.grid()
        global EnterName

   
    def UserDetails(self):

        if self.EnterName.get() == "":
            self.Return.configure(text = "Please enter your name!")
       
        else:
            try:
                if int(self.EnterAge.get()) <= 5:
                    self.Return.configure(text = "You're too young!")
               
                elif int(self.EnterAge.get()) >= 16:
                    self.Return.configure(text = "You're too old!")
                   
                else:
                    self.ShowQuiz()
           
            except ValueError:
                self.Return.configure(text = "Please enter your \nage in numbers")            
               
               
    def QuestionGenAdd(self):

        num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
       
        #Picks numbers
        self.number_1 = random.choice(num_list)
        self.number_2 = random.choice(num_list)
        self.total = self.number_1 + self.number_2
        self.add = self.number_1, "+", self.number_2, "="
       
        self.Question.configure(text = self.add)
       
       
       

    def Check(self):

        global score
        global count

        try:
            self.answer = self.AnswerBox.get()
            self.answer_mod = int(self.answer)
           
            #Clears
            self.AnswerBox.delete(0, 'end')
           
            if self.answer_mod == self.total:
                self.feedback.configure(text = "Correct!")
               
                score += 1
                count += 1

                self.TitleLabel.configure(text = "Score: {}/5".format(score))
               
                if count == 5:
                    self.destroy()
                   
                else:
                    self.QuestionGenAdd()
   
            else:
                self.feedback.configure(text = "Incorrect!")
                count += 1
                if count == 5:
                    self.destroy()
                   
                else:
                    self.QuestionGenAdd()
       
        except ValueError:
            self.feedback.configure(text = "Please enter \na number")

if __name__ == "__main__":
    root = Tk()
    frames = Math(root)
    root.title("Math quiz")
    root.mainloop() 

import random
from tkinter import *
from tkinter import Tk


class Math():
    def __init__(self, parent):
       
        self.index = 0
        self.score = 0

        self.Welcome = Frame(parent)
        self.Welcome.grid(row=0, column=0)
        self.Welcome.configure(bg = "light gray")
       
   
        self.TitleLabel = Label(self.Welcome, text = "Welcome",
                                bg = "black", fg = "white", width = 20, padx = 30,
                                pady = 10, font = ("comic sans ms", "14", "bold italic"))
        self.TitleLabel.grid(row = 0, columnspan = 2)
       
       
        self.LabelName = Label(self.Welcome, text = "Enter Name: ",
                               fg = "black", bg = "light gray", padx = 5, pady = 5,
                               font = ("comic sans ms", "10", "bold italic"))
        self.LabelName.grid(row = 1, column = 0)
       
        self.EnterName = Entry(self.Welcome)
        self.EnterName.grid(row = 1, column = 1)
       
     
        self.LabelAge = Label(self.Welcome, text = "Enter Age: ",
                               fg = "black", bg = "light gray", padx = 5, pady = 5,
                               font = ("comic sans ms", "10", "bold italic"))
        self.LabelAge.grid(row = 2, column = 0)
       
        self.EnterAge = Entry(self.Welcome)
        self.EnterAge.grid(row = 2, column = 1)

       
   
       
        #Warning, Difficulty level label and radio buttons
        self.WarningLabel = Label(self.Welcome, text = '', anchor = W, fg = "red", width= 20, padx = 30, pady = 10)
        self.WarningLabel.grid(row = 4, columnspan = 1)

        self.DifficultyLabel = Label(self.Welcome, text = 'Choose diffculity', anchor = W, fg = "black", bg = "light gray", width= 14, padx = 30, pady = 20, font = ("Time", "12", "bold italic"))
        self.DifficultyLabel.grid(row = 5, column = 0)
       
        self.difficulty = ["Easy", "Medium", "Hard"]
        self.diff_lvl = StringVar()
        self.diff_lvl.set(0)
        self.diff_btns = []

        for i in range(len(self.difficulty)):
            rb = Radiobutton(self.Welcome, variable = self.diff_lvl, value = i, text = self.difficulty[i], anchor = W, padx = 50, width = "5", height = "2")
            self.diff_btns.append(rb)
            rb.grid(row = i+6, column = 0, sticky = W)

   
        self.Return = Label(self.Welcome, fg = "red", bg = "light gray",
                            font = ("comic sans ms", "10", "italic"))
        self.Return.grid(row = 3, column = 1)
        self.Return.configure(text = "")
       
     
        self.Toquiz = Button(self.Welcome, text = "Next",
                             activebackground = "gray", bg = "light gray",
                             command = lambda:[self.UserDetails(), self.QuestionGen()])
        self.Toquiz.grid(row = 4, column = 0)
       
        global score
        global count
       
        score = 0
        count = 0
   
        self.Quiz = Frame(parent)
        self.Quiz.configure(bg = "light grey")
       
     
        self.TitleLabel = Label(self.Quiz, text = "QUIZ",
                                bg = "black", fg = "white", width = 40, padx = 30,
                                pady = 10, font = ("comic sans ms", "14", "bold italic"))
        self.TitleLabel.grid(row = 0, columnspan = 2)
       
     
        self.Question = Label(self.Quiz, padx = 5, pady = 5, bg = "light grey", font = ("comic sans ms", "10"))
        self.Question.grid(row = 1, column = 0)
       
 
        self.AnswerBox = Entry(self.Quiz)
        self.AnswerBox.grid(row = 1, column = 1)

        self.ScoreLabel = Label(self.Quiz, bg = "light grey", text = "")
        self.ScoreLabel.grid(row = 5, column =1)
       

        self.ButtonCheck = Button(self.Quiz, text = "Check question",
                            activebackground = "gray",
                            command = self.Check)
        self.ButtonCheck.grid(row = 2, column = 0)
       

        self.feedback = Label(self.Quiz, padx = 5, pady = 5, bg = "light grey", font = ("comic sans ms", "10"))
        self.feedback.grid(row = 2, column = 1)
       

        self.Score_page = Frame(parent)
        #Title
        self.TitleScore = Label(self.Score_page, text = "YOUR SCORE",
                                bg = "black", fg = "white", width = 20, padx = 30,
                                pady = 10, font = ("comic sans ms", "14", "bold italic"))
        self.TitleScore.grid(row = 0, columnspan = 2)
       
        #Name displays
        self.Name_display = Label(self.Score_page, text = "{}".format(self.EnterName.get()), padx = 3,
                                   pady = 3, font = ("comic sans ms", "10"))
        self.Name_display.grid(row = 1, column = 0)
       
       
        #Score displays
        self.Score_display = Label(self.Score_page, text = "Name:Rishita          Score: 5/5",
                                   padx = 3, pady = 3, font = ("comic sans ms", "10"))
        self.Score_display.grid(row = 1, column = 1)
       
    """FUNCTIONS"""

    def End(self):
        #Should run when count reaches 5
        self.Quiz.grid_remove()
        self.Score_page.grid()    
   
    def ShowQuiz(self):
 
        self.Welcome.grid_remove()
        self.Quiz.grid()
   
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
               
               
    def QuestionGen(self):

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

                self.TitleLabel.configure(text = "QUIZ \nScore: {}/5".format(score))
               
                if count == 5:
                    self.End()
                   
                else:
                    self.QuestionGen()
   
            else:
                self.feedback.configure(text = "Incorrect!", fg = "red")
                count += 1
                if count == 5:
                    self.End()
                   
                else:
                    self.QuestionGen()
       
        except ValueError:
            self.feedback.configure(text = "Please enter \na number")

if __name__ == "__main__":
    root = Tk()
    frames = Math(root)
    root.title("Math quiz")
    root.mainloop()

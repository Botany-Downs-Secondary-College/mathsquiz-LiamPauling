#Maths_Quiz_V3.py
#Use function .grid_remove()
#L.Pauling Feb 2021

#Import tkinter modules for GUI
from tkinter import*
from tkinter import ttk

#Parent class
class MathQuiz:
    def __init__(self,parent):

        '''Widgets for Welcome Frame'''

        self.Welcome = Frame(parent)
        self.Welcome.grid(row=0, column=0)

        self.TitleLabel = Label(self.Welcome, text = "Welcome to Maths Quiz",
                                bg = "black", fg = "white", width = 20, padx = 30, pady = 10,
                                font = ("Time", "14", "bold"))
        self.TitleLabel.grid(columnspan = 2)

        self.NextButton = ttk.Button(self.Welcome, text = 'Next')
        self.NextButton.grid(row = 8, column = 1)

        '''Widgets for Questions Frame'''

        self.Questions = Frame(parent)
        self.Questions.grid(row = 0, column = 1)

        self.QuestionsLabel = Label(self.Questions, text = "Quiz Questions",
                                    bg = "black", fg = "white", width = 20, padx = 30, pady = 10,
                                    font = ("Time", "14", "bold"))
        self.QuestionsLabel.grid(columnspan = 2)

        self.Homebutton = Button(self.Questions, text = 'Next')
        self.Homebutton.grid(row = 8, column = 1)

    '''A method that removes Questions Frame. Same done for Questions Frame'''
    def show_Welcome(self):
        self.Questions.grid_remove()
        self.Welcome.grid()

    def show_Questions(self):
        self.Welcome.grid_remove()
        self.Questions.grid()


#Main Routine
if __name__ == "__main__":
    root = Tk()
    frames = MathQuiz(root)
    root.title("Quiz")
    root.mainloop()


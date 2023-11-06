
import openpyxl 
class Question :
    def __init__(self,question,correct_ans,option):
        self.question = question
        self.correct_ans = correct_ans
        self.option  = option

    def check_ans(self, user_choice):
        choice = str(user_choice)
        correct = str(self.correct_ans)
        if (choice==correct):
            return True  
        else:
            return False
class Student :
    def __init__(self,score = 0):
        self.score = score
        
class ListQuestion:
    def __init__(self):
        self.Questions = []

    def readFromExcel(self, filename):
        self.Questions.clear()
        workbook = openpyxl.load_workbook(filename)
        sheet = workbook.active
        for row in sheet.iter_rows(min_row=2, values_only=True):
            if not all(cell is None or cell == '' for cell in row):
                question_text, correct_ans ,options_str = row
                options = options_str.split(',')
                question = Question(question_text, correct_ans, options)
                self.Questions.append(question)
            else:
                print("warning: Empty row encountered")
                break

class Repond:
    def __init__(self,repond):
        self.repond = repond 
    def setRepond(self,repond):
        self.repond = repond



    


        


 
import tkinter as tk
import question as qs
from tkinter import messagebox


student1 = qs.Student(0)
question = qs.ListQuestion()
question.readFromExcel("Book2.xlsx")
questions = question.Questions
repond = qs.Repond(" ")
def check_answer(question_index,user_choice):
    current_question = questions[question_index]
    correct = current_question.check_ans(user_choice)
    print(user_choice)
    if(correct==True):
        student1.score +=1
        messagebox.showinfo("Resultat","Correct!")
    else:
        messagebox.showinfo("Resultat","Incorrect!")
def getRepond(repondre,choice):
    repondre = choice    

def display_question(question_index):
    current_question = questions[question_index]
    question_label.config(text=current_question.question)
    for button in option_buttons:
        button.destroy()
    option_buttons.clear()
    for i in range(len(current_question.option)):
        new_button = tk.Button(root, text=current_question.option[i], width=30,
                               command=lambda i=i: repond.setRepond(current_question.option[i]))
        new_button.pack()
        option_buttons.append(new_button)
    verifier_button=tk.Button(root,text='Verifier',command=lambda : check_answer(question_index,repond.repond))
    verifier_button.pack()
    option_buttons.append(verifier_button)
    next_button.config(command=lambda: next_question(question_index))


def next_question(question_index):
    question_index += 1
    if question_index < len(questions):
       display_question(question_index)
    else:
        messagebox.showinfo('Fin du questionnaire', 'Le questionnaire est terminé. Score: {}'.format(student1.score))
root = tk.Tk()
root.title('QCM')
next_button = tk.Button(root, text='Question suivante', command=lambda: next_question(0))
next_button.pack()
question_label = tk.Label(root, text='', wraplength=300)
question_label.pack()
option_buttons = []

display_question(0)
root.mainloop()









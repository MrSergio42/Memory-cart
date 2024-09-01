from PyQt5.QtWidgets import QApplication
from random import choice, shuffle

app = QApplication([]) # Створення додатка

# Імпортування main_window, menu_window
from main_window import *
from menu_window import *

# Показ вікна з запитаннями
main_window.show()

# Клас з питаннями
class Question:
    def __init__(self, question, answer, wrong_ans1, wrong_ans2, wrong_ans3):
        self.question = question
        self.answer = answer
        self.wrong_ans1 = wrong_ans1
        self.wrong_ans2 = wrong_ans2
        self.wrong_ans3 = wrong_ans3

# Питання
q1 = Question("Вікно", "window", "apple", "s", "negr")
q2 = Question("Меню", "menu", "net", "da", "spaces")
q3 = Question("Араб", "Arab", "aryb", "Vitya", "21")
q4 = Question("6^2", "36", "29", "38", "34")

questions = [q1, q2, q3, q4]
radio_btns = [r_btn1, r_btn2, r_btn3, r_btn4]

count_right = 0
count_wrong = 0
count_all = 0

def new_question():
    global cur_quest
    cur_quest = choice(questions)
    lbl_question.setText(cur_quest.question)
    lbl_right.setText(cur_quest.answer)

    shuffle(radio_btns)
    radio_btns[0].setText(cur_quest.answer)
    radio_btns[1].setText(cur_quest.wrong_ans1)
    radio_btns[2].setText(cur_quest.wrong_ans2)
    radio_btns[3].setText(cur_quest.wrong_ans3)

new_question()

def check_ans():
    global count_all, count_right, count_wrong
    radio_buttons_group.setExclusive(False)
    for btn in radio_btns:
        if btn.isChecked():
            if btn.text() == cur_quest.answer:
                count_right += 1
                count_all += 1
                lbl_correct.setText("Правильно")
                btn.setChecked(False)
                break
    else:
        lbl_correct.setText("Не правильно")
        btn.setChecked(False)
        count_all += 1
        count_wrong += 1
    radio_buttons_group.setExclusive(True)

# Функція яка відкриває вікно меню
def to_menu():
    main_window.hide()
    menu_window.show()

# Функція яка відкриває вікно з запитаннями
def to_main():
    menu_window.hide()
    main_window.show()

# Якась штука яка, наверно, теж перемикає вікна
btn_menu.clicked.connect(to_menu)
btn_back.clicked.connect(to_main)

app.exec_()
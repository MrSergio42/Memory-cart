from PyQt5.QtWidgets import QApplication
from random import choice, shuffle

app = QApplication([]) # Створення додатка

# Імпортування main_window, menu_window
from main_window import *
from menu_window import *

# Показ вікна з запитаннями
main_window.show()

# Створення Класу з питаннями
class Question:
    def __init__(self, question, answer, wrong_ans1, wrong_ans2, wrong_ans3):
        self.question = question
        self.answer = answer
        self.wrong_ans1 = wrong_ans1
        self.wrong_ans2 = wrong_ans2
        self.wrong_ans3 = wrong_ans3

# Питання
q1 = Question("Вікно", "window", "apple", "vindov", "vindow")
q2 = Question("Меню", "menu", "nenu", "danu", "spaces")
q3 = Question("5+5+5*2", "20", "25", "35", "21")
q4 = Question("6^2", "36", "29", "38", "34")

questions = [q1, q2, q3, q4]
radio_btns = [r_btn1, r_btn2, r_btn3, r_btn4]

count_right = 0
count_wrong = 0
count_all = 0

# Додавання питань в вікно з карткою
def new_question():
    global cur_quest
    cur_quest = choice(questions)# Вибирає рандомне питання
    lbl_question.setText(cur_quest.question)# Відображаємо питання
    lbl_right.setText(cur_quest.answer)# Відображаємо правильну відповідь

    shuffle(radio_btns)# Перемішуємо список з кнопками
    # Додаємо варіанти відповідей в кнопки
    radio_btns[0].setText(cur_quest.answer)
    radio_btns[1].setText(cur_quest.wrong_ans1)
    radio_btns[2].setText(cur_quest.wrong_ans2)
    radio_btns[3].setText(cur_quest.wrong_ans3)

new_question()

def check_ans(): # Перевірка правильності відповіді
    global count_all, count_right, count_wrong
    radio_buttons_group.setExclusive(False)# Дозволяємо змінювати кнопки
    for btn in radio_btns: # Перебираємо список з кнопками
        if btn.isChecked():# Знаходимо вибрану кнопку
            if btn.text() == cur_quest.answer:# Перевірка правельності відповіді
                count_right += 1
                count_all += 1
                lbl_correct.setText("Правильно")
                btn.setChecked(False) # Прибираємо виділення з кнопки
                break 
    else:
        lbl_correct.setText("Не правильно")
        btn.setChecked(False)
        count_all += 1
        count_wrong += 1
    radio_buttons_group.setExclusive(True) # Блокуємо зміну кнопок

def next_question():
    if btn_answer.text() == "Відповісти":
        check_ans()
        answer_group_box.hide()
        result_group_box.show()
        btn_answer.setText("Наступне запитання")
    elif btn_answer.text() == "Наступне запитання":
        new_question()
        result_group_box.hide()
        answer_group_box.show()
        btn_answer.setText("Відповісти")

def clear():
    question_input.clear()
    right_ans_input.clear()
    wrong_ans1_input.clear()
    wrong_ans2_input.clear()
    wrong_ans3_input.clear()

def add_quesion():
    question = Question(question_input.text(), right_ans_input.text(), wrong_ans1_input.text(), wrong_ans2_input.text(), wrong_ans3_input.text())
    questions.append(question)
    clear()

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
btn_answer.clicked.connect(next_question)
btn_add.clicked.connect(add_quesion)
btn_clear.clicked.connect(clear)

app.exec_()

# СЛЕДУЮЩИЙ НІК НА БЛУКЕТ АБО КАХУТ Квадробер Олег
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QRadioButton, QSpinBox, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup

main_window = QWidget() # Створення вінв
main_window.resize(600, 500) # Залаємо розміри вікна
main_window.setWindowTitle("Memory card") 
main_window.move(300, 300) 
# Створення кнопок
btn_menu = QPushButton("Меню")
btn_sleep = QPushButton("Відпочити")

box_minutes = QSpinBox() # Лічильник секунд 
box_minutes.setValue(50)
box_minutes_lbl = QLabel("хвилин")

lbl_question = QLabel('Question')

# Створення групи віджеті
answer_group_box = QGroupBox("Варіанти відповідей")
radio_buttons_group = QButtonGroup() # Створення кнопок в групу 
r_btn1 = QRadioButton('1')
r_btn2 = QRadioButton('2')
r_btn3 = QRadioButton('3')
r_btn4 = QRadioButton('4')
# Додаємо кнопки в групу
radio_buttons_group.addButton(r_btn1)
radio_buttons_group.addButton(r_btn2)
radio_buttons_group.addButton(r_btn3)
radio_buttons_group.addButton(r_btn4)

# Створюємо лінії
v_line1 = QVBoxLayout()
v_line2 = QVBoxLayout()
h_line = QHBoxLayout()

# Додаємо на першу лінію віджети
v_line1.addWidget(r_btn1)
v_line1.addWidget(r_btn2)
# Додаємо на другу лінію віджети
v_line2.addWidget(r_btn3)
v_line2.addWidget(r_btn4)

# Додаємо на вертикальну лінію віджети
h_line.addLayout(v_line1)
h_line.addLayout(v_line2)
# Наверно, групіруємо віджети
answer_group_box.setLayout(h_line)

result_group_box = QGroupBox("Результат теста") # створення групи віджетів
lbl_correct = QLabel('Правильно')
lbl_right = QLabel('Правильна відповідь')

# Создаємо лінію і додаємо на неї віджети
result_line = QVBoxLayout()
result_line.addWidget(lbl_correct, alignment=(Qt.AlignLeft|Qt.AlignTop))
result_line.addWidget(lbl_right, alignment=Qt.AlignCenter, stretch=3)
result_group_box.setLayout(result_line)
result_group_box.hide()

# Створення кпонки відповісти
btn_answer = QPushButton("Відповісти")

# Створюємо ще одну лінію і додаємо на неї віджети
line1 = QHBoxLayout()
line1.addWidget(btn_menu)
line1.addStretch(2)
line1.addWidget(btn_sleep)
line1.addWidget(box_minutes)
line1.addWidget(box_minutes_lbl)

# Створюємо ще одну лінію і додаємо на неї віджети
main_line = QVBoxLayout()
main_line.addLayout(line1)
main_line.addWidget(lbl_question, alignment=(Qt.AlignCenter|Qt.AlignCenter))

# Створюємо ще одну лінію і додаємо на неї віджети
line2 = QHBoxLayout()
line2.addWidget(answer_group_box)
line2.addWidget(result_group_box)

# Налаштування довжини між віджетами і додавання віджету
main_line.addLayout(line2, stretch=4)
main_line.addWidget(btn_answer)
main_line.addStretch(0)

# Незнаю шо це но воно корисне, наверно, кудись прикріплює лінію
main_window.setLayout(main_line)














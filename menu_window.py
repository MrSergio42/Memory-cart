from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QLineEdit

# Встановлення назви віна, розмірів
menu_window = QWidget()
menu_window.resize(400, 300)
menu_window.setWindowTitle("Memory cart")
menu_window.move(700, 300)

# Текст в віджетах в меню
question_lbl = QLabel("Введіть запитання:")
right_ans_lbl = QLabel("Введіть правильну відповідь:")
wrong_ans1_lbl = QLabel("Введіть неправильну відповідь:")
wrong_ans2_lbl = QLabel("Введіть неправильну відповідь:")
wrong_ans3_lbl = QLabel("Введіть неправильну відповідь:")

# Запити тексту в віджет шось таке
question_input = QLineEdit()
right_ans_input = QLineEdit()
wrong_ans1_input = QLineEdit()
wrong_ans2_input = QLineEdit()
wrong_ans3_input = QLineEdit()

# Додавання кнопок додати запитання, очистити
btn_add = QPushButton("Додати  запитання")
btn_clear = QPushButton("Очистити")
 
# статистика і її розмір ну і інші дані
lbl_stat = QLabel("СТАТИСТИКА")
lbl_stat.setStyleSheet("font-size: 30px; font-weight: bold;")

# Статистика
statistic = QLabel()

# Кнопка яка буде повертати на перше вікно
btn_back = QPushButton("Назад")

# Ще одні лінії
col1 = QVBoxLayout()
col2 = QVBoxLayout()

# Додавання віджетів на першу лінію
col1.addWidget(question_lbl)
col1.addWidget(right_ans_lbl)
col1.addWidget(wrong_ans1_lbl)
col1.addWidget(wrong_ans2_lbl)
col1.addWidget(wrong_ans3_lbl)

# Додавання віджетів на другу лінію
col2.addWidget(question_input)
col2.addWidget(right_ans_input)
col2.addWidget(wrong_ans1_input)
col2.addWidget(wrong_ans2_input)
col2.addWidget(wrong_ans3_input)

# Создаєм лінію 2 і додаєм віджети
line2 = QHBoxLayout()
line2.addWidget(btn_add)
line2.addWidget(btn_clear)

# Создаєм лінію і прикріплюємо на неї лінії
line1 = QHBoxLayout()
line1.addLayout(col1)
line1.addLayout(col2)

# Создаєм лінію і прикріплюємо на неї лінії і віджети 
main_line = QVBoxLayout()
main_line.addLayout(line1)
main_line.addLayout(line2)
main_line.addWidget(lbl_stat)
main_line.addWidget(statistic)
main_line.addWidget(btn_back)

# Прикріплюємо лінію на шось, наверно, вікно
menu_window.setLayout(main_line)
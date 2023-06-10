# Import libraries
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

# Create the app and window
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Winner Generator')
main_win.resize(400, 200)

# Create widgets
label_text = QLabel('Click the button to randomly select a winner')
label_winner = QLabel('')
button_generator = QPushButton('Generate')

# Arrange the widgets
v_line = QVBoxLayout()
v_line.addWidget(label_text, alignment = Qt.AlignCenter)
v_line.addWidget(label_winner, alignment = Qt.AlignCenter)
v_line.addWidget(button_generator, alignment = Qt.AlignCenter)
main_win.setLayout(v_line)


# Event handling
def show_winner():
    result = randint(1, 100)
    label_winner.setText(str(result))
    label_text.setText('Winner')


button_generator.clicked.connect(show_winner)

# Show the win and run the app
main_win.show()
app.exec_()


# Test

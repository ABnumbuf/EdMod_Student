# This Python file uses the following encoding: windows-1251

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5 import QtCore
import My_DiscrtLog as dis
from util import read_text, get_values


class Window_2_2(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('ЗДЛ: Метод Сильвестра-Полига-Хелмана')
        self.setFixedSize(760, 800)
        main_layout = QGridLayout(self)
        self.setLayout(main_layout)
        tab = QTabWidget(self)
        tab.setFont(QFont('Arial', 12))
        # Page Theory
        page_text = QWidget(self)
        layout = QFormLayout()
        page_text.setLayout(layout)
        text = read_text('text_mod2_block2.html')
        label_text = QLabel(text)
        label_text.setFont(QFont('Arial', 12))
        label_text.setWordWrap(True)
        scrollArea = QScrollArea()
        scrollArea.setWidget(label_text)
        layout.addRow(scrollArea)
        # Page Example
        page_example = QWidget(self)
        layout_ex = QFormLayout()
        page_example.setLayout(layout_ex)
        layout_ex.addRow(QLabel(
            f'<p>Решение задачи <box>a<sup>x</sup></box> &#8801; b (mod p)<p> методом СПХ'))
        layout_ex.addRow(QLabel('Введи значения:'))
        self.inp_ex_a = QLineEdit()
        self.inp_ex_b = QLineEdit()
        self.inp_ex_n = QLineEdit()
        btn_ex = QPushButton("Решить")
        btn_ex.clicked.connect(self.click_btn_ex)
        self.outp_ex = QTextBrowser()

        layout_ex.addRow(QLabel('a = '), self.inp_ex_a)
        layout_ex.addRow(QLabel('b = '), self.inp_ex_b)
        layout_ex.addRow(QLabel('n = '), self.inp_ex_n)
        layout_ex.addRow(btn_ex)
        layout_ex.addRow(QLabel('Результат:'))
        layout_ex.addRow(self.outp_ex)
        # Page Task
        page_task = QWidget(self)
        layout_tsk = QFormLayout()
        page_task.setLayout(layout_tsk)
        layout_tsk.addRow(QLabel('Проверка решения ЗДЛ методом СПХ'))
        self.v_tsk_a, self.v_tsk_b, self.v_tsk_n = get_values(1)[0]
        self.v_x = dis.coherence_method(self.v_tsk_a, self.v_tsk_b, self.v_tsk_n)
        while self.v_x == 'None':
            self.v_tsk_a, self.v_tsk_b, self.v_tsk_n = get_values(1)[0]
            self.v_x = dis.coherence_method(self.v_tsk_a, self.v_tsk_b, self.v_tsk_n)
        self.task_text = QLabel(
            f'<p>Реши задачу: <box>{self.v_tsk_a}<sup>x</sup></box> &#8801; {self.v_tsk_b} (mod {self.v_tsk_n})</p>')
        self.task_text.setAlignment(QtCore.Qt.AlignCenter)
        self.task_text.setFixedHeight(160)
        self.inp_tsk = QLineEdit()
        btn_tsk_chk = QPushButton("Проверить")
        btn_tsk_rst = QPushButton("Обновить")
        self.outp_tsk = QTextBrowser()
        btn_tsk_chk.clicked.connect(self.click_btn_tsk_chk)
        btn_tsk_rst.clicked.connect(self.click_btn_tsk_rst)

        layout_tsk.addRow(self.task_text)
        layout_tsk.addRow(QLabel('Ввведи значение:'), self.inp_tsk)
        layout_tsk.addRow(btn_tsk_chk)
        layout_tsk.addRow(btn_tsk_rst)
        layout_tsk.addRow(QLabel('Результат:'))
        layout_tsk.addRow(self.outp_tsk)

        tab.addTab(page_text,    'Теория')
        tab.addTab(page_example, 'Примеры')
        tab.addTab(page_task,    'Задачи')
        
        main_layout.addWidget(tab, 0, 0, 2, 1)

    def click_btn_ex(self):
        try:
            v_exmpl_a = int(self.inp_ex_a.text())
            v_exmpl_b = int(self.inp_ex_b.text())
            v_exmpl_n = int(self.inp_ex_n.text())
            self.outp_ex.setText(dis.sylvester_pohlig_hellman_method_output(v_exmpl_a, v_exmpl_b, v_exmpl_n))
            self.inp_ex_a.clear()
            self.inp_ex_b.clear()
            self.inp_ex_n.clear()
            self.update()
        except ValueError:
            self.outp_ex.setText(f"Введи значения: \na, b, n - целые числa")
            self.update()
    
    def click_btn_tsk_chk(self):
        try:
            inp_tsk = int(self.inp_tsk.text())
            v_x = dis.sylvester_pohlig_hellman_method(self.v_tsk_a, self.v_tsk_b, self.v_tsk_n)
            if (inp_tsk == v_x):
                self.outp_tsk.setText(
                    f"<p><box>{self.v_tsk_a}<sup>{v_x}</sup></box> &#8801; {self.v_tsk_b} (mod {self.v_tsk_n})</p><p>Верно</n><p></p>")
            else:
                self.outp_tsk.setText(
                    f"<p><box>{self.v_tsk_a}<sup>{inp_tsk}</sup></box> &#8801; {self.v_tsk_b} (mod {self.v_tsk_n})</p><p>Неверно</n>")
            self.inp_tsk.clear()
            self.update()
        except ValueError:
            self.outp_tsk.setText(f"Введи значения: \nx - целое число")
            self.update()

    def click_btn_tsk_rst(self):
        try:
            self.v_tsk_a, self.v_tsk_b, self.v_tsk_n = get_values(1)[0]
            self.task_text.setText(
                f'<p>Реши задачу: <box>{self.v_tsk_a}<sup>x</sup></box> &#8801; {self.v_tsk_b} (mod {self.v_tsk_n})</p>')
            self.inp_tsk.clear()
            self.update()
        except ValueError:
            print(ValueError)


def win_2_2(w):
    
    w.window = Window_2_2()
    w.window.show()


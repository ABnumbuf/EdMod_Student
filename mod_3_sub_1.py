# This Python file uses the following encoding: windows-1251

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5 import QtCore
import My_Knapsack as ks
from util import read_text


class Window_3_1(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Рюкзачная криптосистема: Задача о рюкзаке')
        self.setFixedSize(760, 800)
        main_layout = QGridLayout(self)
        self.setLayout(main_layout)
        tab = QTabWidget(self)
        tab.setFont(QFont('Arial', 12))
        # Page Theory
        page_text = QWidget(self)
        layout = QFormLayout()
        page_text.setLayout(layout)
        text = read_text('text_mod3_block1.html')
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
            f'Решение задачи о рюкзаке по введенным значениям'))
        layout_ex.addRow(QLabel('Введи значения:'))
        self.inp_ex_w = QLineEdit()
        self.inp_ex_s = QLineEdit()
        btn_ex = QPushButton("Решить")
        btn_ex.clicked.connect(self.click_btn_ex)
        self.outp_ex = QTextBrowser()

        layout_ex.addRow(QLabel('w = '), self.inp_ex_w)
        layout_ex.addRow(QLabel('s = '), self.inp_ex_s)
        layout_ex.addRow(btn_ex)
        layout_ex.addRow(QLabel('Результат:'))
        layout_ex.addRow(self.outp_ex)
        # Page Task
        page_task = QWidget(self)
        layout_tsk = QFormLayout()
        page_task.setLayout(layout_tsk)
        layout_tsk.addRow(QLabel('Проверка решения задачи о рюкзаке по заданным значениям'))
        self.v_tsk_w, self.v_tsk_s = ks.get_val_tsk_3_1()
        self.task_text = QLabel(
            f'w = {self.v_tsk_w}\n s = {self.v_tsk_s}')
        self.task_text.setAlignment(QtCore.Qt.AlignCenter)
        self.task_text.setFixedSize(620, 160)
        self.inp_tsk = QLineEdit()
        btn_tsk_chk = QPushButton("Проверить")
        btn_tsk_rst = QPushButton("Обновить")
        self.outp_tsk = QTextBrowser()
        btn_tsk_chk.clicked.connect(self.click_btn_tsk_chk)
        btn_tsk_rst.clicked.connect(self.click_btn_tsk_rst)

        layout_tsk.addRow(self.task_text)
        layout_tsk.addRow(QLabel('Ввведи ответ:'), self.inp_tsk)
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
            v_exmpl_w = [int(i) for i in str(self.inp_ex_w.text()).split(',')]
            v_exmpl_s = int(self.inp_ex_s.text())
            self.outp_ex.setText(ks.knapSack_out(v_exmpl_w, v_exmpl_s))
            self.inp_ex_w.clear()
            self.inp_ex_s.clear()
            self.update()
        except ValueError:
            self.inp_ex_w.clear()
            self.inp_ex_s.clear()
            self.outp_ex.setText(f"Введи значения: \nw - последовательность целых \ns - целое число")
            self.update()
    
    def click_btn_tsk_chk(self):
        try:
            inp_tsk = [int(i) for i in str(self.inp_tsk.text()).split(',')]
            v_x =  ks.knapSack(self.v_tsk_w, self.v_tsk_s)
            if (inp_tsk == v_x):
                self.outp_tsk.setText(
                    f"w = {self.v_tsk_w}\n s = {self.v_tsk_s}\nОтвет: {self.inp_tsk.text()}\nВерно")
            else:
                self.outp_tsk.setText(
                    f"w = {self.v_tsk_w}\n s = {self.v_tsk_s}\nОтвет: {self.inp_tsk.text()}\nНеверно")
            self.inp_tsk.clear()
            self.update()
        except ValueError:
            self.inp_tsk.clear()
            self.outp_tsk.setText(f"Введи значения: \nцелое число")
            self.update()

    def click_btn_tsk_rst(self):
        try:
            self.v_tsk_w, self.v_tsk_s = ks.get_val_tsk_3_1()
            self.task_text.setText(
                f'w = {self.v_tsk_w}\n s = {self.v_tsk_s}')
            self.inp_tsk.clear()
            self.update()
        except ValueError:
            print(ValueError)


def win_3_1(w):
    
    w.window = Window_3_1()
    w.window.show()


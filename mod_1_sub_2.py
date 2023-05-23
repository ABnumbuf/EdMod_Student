# This Python file uses the following encoding: windows-1251

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5 import QtCore
from util import read_text
import My_ElGamal as elg


class Window_1_2(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('ЭЦП по схеме Эль-Гамаля: Создание подписи')
        self.setFixedSize(760, 800)
        main_layout = QGridLayout(self)
        self.setLayout(main_layout)
        tab = QTabWidget(self)
        tab.setFont(QFont('Arial', 12))
        # Page Theory
        page_text = QWidget(self)
        layout = QFormLayout()
        page_text.setLayout(layout)
        text = read_text('text_mod1_block2.html')
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
        layout_ex.addRow(QLabel('Создание ЭЦП по схеме Эль-Гамаля по введенным значениям'))
        layout_ex.addRow(QLabel('Введи значения:'))
        self.inp_ex_m = QLineEdit()
        self.inp_ex_p = QLineEdit()
        self.inp_ex_g = QLineEdit()
        self.inp_ex_x = QLineEdit()
        btn_ex = QPushButton("Решить")
        btn_ex.clicked.connect(self.click_btn_ex)
        self.outp_ex = QTextBrowser()
        layout_ex.addRow(QLabel('m = '), self.inp_ex_m)
        layout_ex.addRow(QLabel('p = '), self.inp_ex_p)
        layout_ex.addRow(QLabel('g = '), self.inp_ex_g)
        layout_ex.addRow(QLabel('x = '), self.inp_ex_x)
        layout_ex.addRow(btn_ex)
        layout_ex.addRow(QLabel('Результат:'))
        layout_ex.addRow(self.outp_ex)
        # Page Task
        page_task = QWidget(self)
        layout_tsk = QFormLayout()
        page_task.setLayout(layout_tsk)
        layout_tsk.addRow(QLabel('Проверка ЭЦП Эль-Гамаля по заданным значениям'))
        self.v_tsk_p,self.v_tsk_g,self.v_tsk_x,self.v_tsk_m = elg.get_val_tsk_1_2()
        self.task_text = QLabel(
                                f'Найди значения подписи для: \np = {self.v_tsk_p}, \ng = {self.v_tsk_g}, \nx = {self.v_tsk_x}, \nm = {self.v_tsk_m}')
        self.task_text.setAlignment(QtCore.Qt.AlignCenter)
        self.task_text.setFixedHeight(160)
        self.inp_tsk_r = QLineEdit()
        self.inp_tsk_s = QLineEdit()
        btn_tsk_chk = QPushButton("Проверить")
        btn_tsk_rst = QPushButton("Обновить")
        btn_tsk_chk.clicked.connect(self.click_btn_tsk_chk)
        btn_tsk_rst.clicked.connect(self.click_btn_tsk_rst)
        self.outp_tsk = QTextBrowser()
        
        layout_tsk.addRow(self.task_text)
        layout_tsk.addRow(QLabel('Введи значения:'))
        layout_tsk.addRow(QLabel('r = '), self.inp_tsk_r)
        layout_tsk.addRow(QLabel('s = '), self.inp_tsk_s)
        layout_tsk.addRow(btn_tsk_chk)
        layout_tsk.addRow(btn_tsk_rst)
        layout_tsk.addRow(QLabel('Результат:'))
        layout_tsk.addRow(self.outp_tsk)

        # add pane to the tab widget
        tab.addTab(page_text, 'Теория')
        tab.addTab(page_example, 'Примеры')
        tab.addTab(page_task, 'Задачи')
        
        main_layout.addWidget(tab, 0, 0, 2, 1)

    def click_btn_ex(self):
        try:
            v_exmpl_m = str(self.inp_ex_m.text())
            v_exmpl_p = int(self.inp_ex_p.text())
            v_exmpl_g = int(self.inp_ex_g.text())
            v_exmpl_x = int(self.inp_ex_x.text())
            self.outp_ex.setText(elg.ds_ElGamal_outp(v_exmpl_m, v_exmpl_p, v_exmpl_g, v_exmpl_x))
            self.inp_ex_m.clear()
            self.inp_ex_g.clear()
            self.inp_ex_x.clear()
            self.inp_ex_p.clear()
            self.update()
        except ValueError:
            self.outp_ex.setText(f"Введи значения: \nm - строка \np, g, x - целые числa")
            self.inp_ex_m.clear()
            self.inp_ex_g.clear()
            self.inp_ex_x.clear()
            self.inp_ex_p.clear()
            self.update()
    
    def click_btn_tsk_chk(self):
        try:
            v_tsk_r = int(self.inp_tsk_r.text())
            v_tsk_s = int(self.inp_tsk_s.text())
            v_r, v_s = elg.ds_ElGamal(self.v_tsk_m, self.v_tsk_p, self.v_tsk_g, self.v_tsk_x)
            if (v_tsk_r == v_r and v_tsk_s == v_s):
                self.outp_tsk.setText(f"Числа <{v_tsk_r}, {v_tsk_s}> являются подписью для:\np = {self.v_tsk_p}, \ng = {self.v_tsk_g}, \nx = {self.v_tsk_x}, \nm = {self.v_tsk_m}\nВерно")
            else:
                self.outp_tsk.setText(f"Числа <{v_tsk_r}, {v_tsk_s}> не являются подписью для:\np = {self.v_tsk_p}, \ng = {self.v_tsk_g}, \nx = {self.v_tsk_x}, \nm = {self.v_tsk_m}\nНеверно")
            self.inp_tsk_r.clear()
            self.inp_tsk_s.clear()
            self.update()
        except ValueError:
            self.outp_tsk.setText(f"Введи значения: \nr - целое число \ns - целое число")
            self.inp_tsk_r.clear()
            self.inp_tsk_s.clear()
            self.update()

    def click_btn_tsk_rst(self):
        try:
            self.v_tsk_p, self.v_tsk_g, self.v_tsk_x, self.v_tsk_m = elg.get_val_tsk_1_2()
            self.task_text.setText(
                f'Найди значения подписи для: \np = {self.v_tsk_p}, \ng = {self.v_tsk_g}, \nx = {self.v_tsk_x}, \nm = {self.v_tsk_m}')
            self.inp_tsk_r.clear()
            self.inp_tsk_s.clear()
            self.outp_tsk.setText(f"")
            self.update()
        except ValueError:
            print(ValueError)


def win_1_2(w):
    
    w.window = Window_1_2()
    w.window.show()


# This Python file uses the following encoding: windows-1251

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5 import QtCore
import random
from util import read_text
import My_ElGamal as elg

class Window_1_3(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('ЭЦП по схеме Эль-Гамаля: Валидация подписи')
        self.setFixedSize(760, 800)
        main_layout = QGridLayout(self)
        self.setLayout(main_layout)
        tab = QTabWidget(self)
        tab.setFont(QFont('Arial', 12))
        # Page Theory
        page_text = QWidget(self)
        layout = QFormLayout()
        page_text.setLayout(layout)
        text = read_text('text_mod1_block3.html')
        label_text = QLabel(text)
        label_text.setFont(QFont('Arial', 12))
        label_text.setWordWrap(True)
        scrollArea = QScrollArea()
        scrollArea.setWidget(label_text)
        layout.addRow(scrollArea)
        # Page Example
        page_example = QWidget(self)
        layout_ex = QGridLayout()
        page_example.setLayout(layout_ex)
        
        self.inp_ex_m = QLineEdit()
        self.inp_ex_p = QLineEdit()
        self.inp_ex_g = QLineEdit()
        self.inp_ex_y = QLineEdit()
        self.inp_ex_r = QLineEdit()
        self.inp_ex_s = QLineEdit()
        btn_ex = QPushButton("Решить")
        btn_ex.clicked.connect(self.click_btn_ex)
        self.outp_ex = QTextBrowser()

        layout_ex.addWidget(QLabel('Валидация ЭЦП по схеме Эль-Гамаля по введенным значениям'), 0, 0, 1, 4)
        layout_ex.addWidget(QLabel('Введи значения:'),                                          1, 0, 1, 4)
        layout_ex.addWidget(QLabel('m = '),                                                     2, 0)
        layout_ex.addWidget(QLabel('p = '),                                                     2, 2)
        layout_ex.addWidget(QLabel('g = '),                                                     3, 0)
        layout_ex.addWidget(QLabel('y = '),                                                     3, 2)
        layout_ex.addWidget(QLabel('r = '),                                                     4, 0)
        layout_ex.addWidget(QLabel('s = '),                                                     4, 2)
        layout_ex.addWidget(self.inp_ex_m,                                                      2, 1)
        layout_ex.addWidget(self.inp_ex_p,                                                      2, 3)
        layout_ex.addWidget(self.inp_ex_g,                                                      3, 1)
        layout_ex.addWidget(self.inp_ex_y,                                                      3, 3)
        layout_ex.addWidget(self.inp_ex_r,                                                      4, 1)
        layout_ex.addWidget(self.inp_ex_s,                                                      4, 3)
        layout_ex.addWidget(btn_ex,                                                             5, 0, 1, 4)
        layout_ex.addWidget(QLabel('Результат:'),                                               6, 0, 1, 4)
        layout_ex.addWidget(self.outp_ex,                                                       7, 0, 1, 4)
        # Page Task
        page_task = QWidget(self)
        layout_tsk = QFormLayout()
        page_task.setLayout(layout_tsk)
        layout_tsk.addRow(QLabel('Проверка валидации ЭЦП Эль-Гамаля по заданным значениям'))
        self.v_tsk_m, self.v_tsk_p, self.v_tsk_g, self.v_tsk_y, self.v_tsk_r, self.v_tsk_s = elg.get_val_tsk_1_3()
        self.w_tsk_text = QLabel(
            f'Являеется ли подпись правильной для: \np = {self.v_tsk_p}, g = {self.v_tsk_g}, y = {self.v_tsk_y}, \nm = {self.v_tsk_m}, \nr = {self.v_tsk_r}, s = {self.v_tsk_s}')
        self.w_tsk_text.setAlignment(QtCore.Qt.AlignCenter)
        self.w_tsk_text.setFixedHeight(160)
        self.inp_tsk = QComboBox()
        self.inp_tsk.addItems(['Подпись подлина', 'Подпись подделана'])
        btn_tsk_chk = QPushButton("Проверить")
        btn_tsk_rst = QPushButton("Обновить")
        self.outp_tsk = QTextBrowser()
        btn_tsk_chk.clicked.connect(self.click_btn_tsk_chk)
        btn_tsk_rst.clicked.connect(self.click_btn_tsk_rst)

        layout_tsk.addRow(self.w_tsk_text)
        layout_tsk.addRow(QLabel('Выбери:'), self.inp_tsk)
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
            v_exmpl_m = str(self.inp_ex_m.text())
            v_exmpl_p = int(self.inp_ex_p.text())
            v_exmpl_g = int(self.inp_ex_g.text())
            v_exmpl_r = int(self.inp_ex_r.text())
            v_exmpl_s = int(self.inp_ex_s.text())
            v_exmpl_y = int(self.inp_ex_y.text())
            self.outp_ex.setText(elg.check_ds_ElGamal_outp(v_exmpl_m, v_exmpl_r, v_exmpl_s,v_exmpl_y, v_exmpl_g, v_exmpl_p))
            self.inp_ex_m.clear()
            self.inp_ex_p.clear()
            self.inp_ex_g.clear()
            self.inp_ex_r.clear()
            self.inp_ex_s.clear()
            self.inp_ex_y.clear()
            self.update()
        except ValueError:
            self.outp_ex.setText(f"Введи значения: \nm - строка \np, g, y, r, s - целые числa")
            self.inp_ex_m.clear()
            self.inp_ex_p.clear()
            self.inp_ex_g.clear()
            self.inp_ex_r.clear()
            self.inp_ex_s.clear()
            self.inp_ex_y.clear()
            self.update()
    
    def click_btn_tsk_chk(self):
        try:
            v_tsk = str(self.inp_tsk.currentText())
            res = elg.check_ds_ElGamal(self.v_tsk_m, self.v_tsk_r, self.v_tsk_s, self.v_tsk_y, self.v_tsk_g, self.v_tsk_p)
            if ((res and v_tsk =='Подпись подлина') or 
                    (not res and v_tsk =='Подпись подделана')):
                self.outp_tsk.setText(
                    f"p = {self.v_tsk_p}, g = {self.v_tsk_g}, y = {self.v_tsk_y}, \nm = {self.v_tsk_m}, \nr = {self.v_tsk_r}, s = {self.v_tsk_s}\nВерно\n{v_tsk}")
            else:
                self.outp_tsk.setText(
                    f"p = {self.v_tsk_p}, g = {self.v_tsk_g}, y = {self.v_tsk_y}, \nm = {self.v_tsk_m}, \nr = {self.v_tsk_r}, s = {self.v_tsk_s}\nНеверно")
            self.update()
        except ValueError:
            self.outp_tsk.setText(f"Введи ответ")
            self.update()

    def click_btn_tsk_rst(self):
        try:
            self.v_tsk_m, self.v_tsk_p, self.v_tsk_g, self.v_tsk_y, self.v_tsk_r, self.v_tsk_s = elg.get_val_tsk_1_3()
            self.w_tsk_text.setText(
                f'Являеется ли подпись правильной для: \np = {self.v_tsk_p}, g = {self.v_tsk_g}, y = {self.v_tsk_y}, \nm = {self.v_tsk_m}, \nr = {self.v_tsk_r}, s = {self.v_tsk_s}')
            self.outp_tsk.setText(f"")
            self.update()
        except ValueError:
            print(ValueError)


def win_1_3(w):
    
    w.window = Window_1_3()
    w.window.show()


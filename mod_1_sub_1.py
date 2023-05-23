# This Python file uses the following encoding: windows-1251

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5 import QtCore
from util import read_text, get_prime_numbers_in_range, binary_pow
import My_ElGamal as elg
import sympy


class Window_1_1(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('ЭЦП по схеме Эль-Гамаля: Генерация ключей')
        self.setFixedSize(700, 800)
        main_layout = QGridLayout(self)
        self.setLayout(main_layout)
        tab = QTabWidget(self)
        tab.setFont(QFont('Arial', 12))
        # Page Theory
        page_text = QWidget(self)
        layout = QFormLayout()
        page_text.setLayout(layout)
        text = read_text('text_mod1_block1.html')
        label_text = QLabel(text)
        label_text.setFont(QFont('Arial', 12))
        label_text.setWordWrap(True)
        scrollArea = QScrollArea()
        scrollArea.setWidget(label_text)
        layout.addRow(scrollArea)
        # Page Example
        page_example = QWidget(self)
        page_example.setFont(QFont('Arial', 12))
        layout_ex = QGridLayout()
        page_example.setLayout(layout_ex)
        tab_ex = QTabWidget(self)
        tab_ex.setTabPosition(QTabWidget.East)

        page_ex_1 = QWidget(self)

        layout_ex_1 = QGridLayout()
        page_ex_1.setLayout(layout_ex_1)
        self.inp_ex_1_lb = QLineEdit()
        self.inp_ex_1_rb = QLineEdit()
        btn_ex_1 = QPushButton("Решить")
        btn_ex_1.clicked.connect(self.click_btn_ex_1)
        self.outp_ex_1 = QTextBrowser()

        layout_ex_1.addWidget(QLabel('Нахождение простых чисел в диапазоне значений'), 0, 0, 1, 3)
        layout_ex_1.addWidget(QLabel('Введи диапазон значений:'),                      1, 0)
        layout_ex_1.addWidget(self.inp_ex_1_lb,                                        1, 1)
        layout_ex_1.addWidget(self.inp_ex_1_rb,                                        1, 2)
        layout_ex_1.addWidget(btn_ex_1,                                                2, 0, 1, 3)
        layout_ex_1.addWidget(QLabel('Результат:'),                                    3, 0, 1, 3)
        layout_ex_1.addWidget(self.outp_ex_1,                                          4, 0, 1, 3)

        page_ex_2 = QWidget(self)

        layout_ex_2 = QGridLayout()
        page_ex_2.setLayout(layout_ex_2)
        self.inp_ex_root = QLineEdit()
        btn_ex_2 = QPushButton("Решить")
        btn_ex_2.clicked.connect(self.click_btn_ex_2)
        self.outp_ex_2 = QTextBrowser()

        layout_ex_2.addWidget(QLabel('Нахождение первообразных корней числа'), 0, 0, 1, 3)
        layout_ex_2.addWidget(QLabel('Введи число:'),                          1, 0)
        layout_ex_2.addWidget(self.inp_ex_root,                                1, 1)
        layout_ex_2.addWidget(btn_ex_2,                                        2, 0, 1, 3)
        layout_ex_2.addWidget(QLabel('Результат:'),                            3, 0, 1, 3)
        layout_ex_2.addWidget(self.outp_ex_2,                                  4, 0, 1, 3)

        page_ex_3 = QWidget(self)

        layout_ex_3 = QGridLayout()
        page_ex_3.setLayout(layout_ex_3)
        self.inp_ex_g = QLineEdit()
        self.inp_ex_x = QLineEdit()
        self.inp_ex_p = QLineEdit()
        btn_ex_3 = QPushButton("Решить")
        btn_ex_3.clicked.connect(self.click_btn_ex_3)
        self.outp_ex_3 = QTextBrowser()

        layout_ex_3.addWidget(QLabel(\
            '<p>Нахождение y &#8801; g<sup>x</sup> (mod p)</p>')\
            ,0,0,1,2)
        layout_ex_3.addWidget(QLabel('Введи значения:'), 1, 0, 1, 2)
        layout_ex_3.addWidget(QLabel('g = '),            2, 0)
        layout_ex_3.addWidget(QLabel('x = '),            3, 0)
        layout_ex_3.addWidget(QLabel('p = '),            4, 0)
        layout_ex_3.addWidget(self.inp_ex_g,             2, 1)
        layout_ex_3.addWidget(self.inp_ex_x,             3, 1)
        layout_ex_3.addWidget(self.inp_ex_p,             4, 1)
        layout_ex_3.addWidget(btn_ex_3,                  5, 0, 1, 2)
        layout_ex_3.addWidget(QLabel('Результат:'),      6, 0, 1, 2)
        layout_ex_3.addWidget(self.outp_ex_3,            7, 0, 1, 2)

        tab_ex.addTab(page_ex_1, '1')
        tab_ex.addTab(page_ex_2, '2')
        tab_ex.addTab(page_ex_3, '3')
        layout_ex.addWidget(tab_ex, 0, 0, 2, 1)

        # Page Task
        page_task = QWidget(self)
        page_task.setFont(QFont('Arial', 12))
        layout_tsk = QGridLayout()
        page_task.setLayout(layout_tsk)
        tab_tsk = QTabWidget(self)
        tab_tsk.setTabPosition(QTabWidget.East)

        page_tsk_1 = QWidget(self)
        layout_tsk_1 = QGridLayout()
        page_tsk_1.setLayout(layout_tsk_1)

        self.v_tsk_1_p_a, self.v_tsk_1_p_b = elg.get_val_tsk_1_1_1()
        self.w_tsk_1_text = QLabel(
            f'\nНайди простое число на промежутке [{self.v_tsk_1_p_a}, {self.v_tsk_1_p_b}]\n')
        self.w_tsk_1_text.setAlignment(QtCore.Qt.AlignCenter)
        self.inp_tsk_1 = QLineEdit()
        btn_tsk_1_chk = QPushButton("Решить")
        btn_tsk_1_chk.clicked.connect(self.click_btn_tsk_1_chk)
        btn_tsk_1_rst = QPushButton("Обновить")
        btn_tsk_1_rst.clicked.connect(self.click_btn_tsk_1_rst)
        self.outp_tsk_1 = QTextBrowser()

        layout_tsk_1.addWidget(QLabel('Нахождение простых чисел в диапазоне значений'),0,0,1,3)
        layout_tsk_1.addWidget(self.w_tsk_1_text,1,0,3,3)
        layout_tsk_1.addWidget(QLabel('Введи ответ:'),4,0)
        layout_tsk_1.addWidget(self.inp_tsk_1,4,1)
        layout_tsk_1.addWidget(btn_tsk_1_chk,5,0,1,3)
        layout_tsk_1.addWidget(btn_tsk_1_rst,6,0,1,3)
        layout_tsk_1.addWidget(QLabel('Результат:'),7,0,1,3)
        layout_tsk_1.addWidget(self.outp_tsk_1,8,0,1,3)

        page_tsk_2 = QWidget(self)
        layout_tsk_2 = QGridLayout()
        page_tsk_2.setLayout(layout_tsk_2)

        self.v_tsk_2 = elg.get_val_tsk_1_1_2()
        self.w_tsk_2_text = QLabel(
            f'\nНайди первообразный корень числа {self.v_tsk_2}\n')
        self.w_tsk_2_text.setAlignment(QtCore.Qt.AlignCenter)
        self.inp_tsk_2 = QLineEdit()
        btn_tsk_2_chk = QPushButton("Решить")
        btn_tsk_2_chk.clicked.connect(self.click_btn_tsk_2_chk)
        btn_tsk_2_rst = QPushButton("Обновить")
        btn_tsk_2_rst.clicked.connect(self.click_btn_tsk_2_rst)
        self.outp_tsk_2 = QTextBrowser()

        layout_tsk_2.addWidget(QLabel('Нахождение первообразных корней числа'),0,0,1,3)
        layout_tsk_2.addWidget(self.w_tsk_2_text,1,0,3,3)
        layout_tsk_2.addWidget(QLabel('Введи число:'),4,0)
        layout_tsk_2.addWidget(self.inp_tsk_2,4,1)
        layout_tsk_2.addWidget(btn_tsk_2_chk,5,0,1,3)
        layout_tsk_2.addWidget(btn_tsk_2_rst,6,0,1,3)
        layout_tsk_2.addWidget(QLabel('Результат:'),7,0,1,3)
        layout_tsk_2.addWidget(self.outp_tsk_2,8,0,1,3)

        page_tsk_3 = QWidget(self)
        layout_tsk_3 = QGridLayout()
        page_tsk_3.setLayout(layout_tsk_3)

        self.v_tsk_3_p, self.v_tsk_3_g, self.v_tsk_3_x = elg.get_val_tsk_1_1_3()
        self.w_tsk_3_text = QLabel(
            f'<p>Найди y &#8801; {self.v_tsk_3_g}<sup>{self.v_tsk_3_x}</sup> (mod {self.v_tsk_3_p})</p><p></p>')
        self.w_tsk_3_text.setAlignment(QtCore.Qt.AlignCenter)
        self.inp_tsk_3 = QLineEdit()
        btn_tsk_3_chk = QPushButton("Решить")
        btn_tsk_3_chk.clicked.connect(self.click_btn_tsk_3_chk)
        btn_tsk_3_rst = QPushButton("Обновить")
        btn_tsk_3_rst.clicked.connect(self.click_btn_tsk_3_rst)
        self.outp_tsk_3 = QTextBrowser()

        layout_tsk_3.addWidget(QLabel(\
            '<p>Нахождение y &#8801; g<sup>x</sup> (mod p)</p><p></p>')\
            ,0,0,2,2)
        layout_tsk_3.addWidget(self.w_tsk_3_text,2,0,2,2)
        layout_tsk_3.addWidget(QLabel('Введи ответ: y = '),4,0)
        layout_tsk_3.addWidget(self.inp_tsk_3,4,1)
        layout_tsk_3.addWidget(btn_tsk_3_chk,5,0,1,3)
        layout_tsk_3.addWidget(btn_tsk_3_rst,6,0,1,3)
        layout_tsk_3.addWidget(QLabel('Результат:'),7,0,1,2)
        layout_tsk_3.addWidget(self.outp_tsk_3,8,0,1,2)

        tab_tsk.addTab(page_tsk_1, '1')
        tab_tsk.addTab(page_tsk_2, '2')
        tab_tsk.addTab(page_tsk_3, '3')
        layout_tsk.addWidget(tab_tsk, 0, 0, 2, 1)

        tab.addTab(page_text, 'Теория')
        tab.addTab(page_example, 'Примеры')
        tab.addTab(page_task, 'Задачи')
        
        main_layout.addWidget(tab, 0, 0, 2, 1)


    def click_btn_ex_1(self):
        try:
            v_ex_1_lb = int(self.inp_ex_1_lb.text())
            v_ex_1_rb = int(self.inp_ex_1_rb.text())
            self.outp_ex_1.setText(
                f"Простые числа в промежутке [{v_ex_1_lb}, {v_ex_1_rb}]:\n{str(get_prime_numbers_in_range(v_ex_1_lb, v_ex_1_rb))}")
            self.inp_ex_1_lb.clear()
            self.inp_ex_1_rb.clear()
            self.update()
        except ValueError:
            self.outp_ex_1.setText(f"Введи значения: целые числa")
            self.inp_ex_1_lb.clear()
            self.inp_ex_1_rb.clear()
            self.update()

    def click_btn_ex_2(self):
        try:
            v_ex_root = int(self.inp_ex_root.text())
            self.outp_ex_2.setText(
                f"Первообразные корни числа {v_ex_root}:\n{elg.get_primitive_roots(v_ex_root)}")
            self.inp_ex_root.clear()
            self.update()
        except ValueError:
            self.outp_ex_2.setText(f"Введи значение: \nцелое простое число")
            self.inp_ex_root.clear()
            self.update()

    def click_btn_ex_3(self):
        try:
            v_ex_g = int(self.inp_ex_g.text())
            v_ex_x = int(self.inp_ex_x.text())
            v_ex_p = int(self.inp_ex_p.text())
            self.outp_ex_3.setText(
                f"<p>{binary_pow(v_ex_g, v_ex_x, v_ex_p)} &#8801; {v_ex_g}<sup>{v_ex_x}</sup> (mod {v_ex_p})</p>")
            self.inp_ex_g.clear()
            self.inp_ex_x.clear()
            self.inp_ex_p.clear()
            self.update()
        except ValueError:
            self.outp_ex_3.setText(f"Введи значения: \np, g, x - целые числa")
            self.inp_ex_g.clear()
            self.inp_ex_x.clear()
            self.inp_ex_p.clear()
            self.update()
    
    def click_btn_tsk_1_chk(self):
        try:
            v_tsk = int(self.inp_tsk_1.text())
            if (v_tsk > self.v_tsk_1_p_a and v_tsk < self.v_tsk_1_p_b and sympy.isprime(v_tsk)):
                self.outp_tsk_1.setText(f"Число {v_tsk} является простым на промежутке [{self.v_tsk_1_p_a}, {self.v_tsk_1_p_b}]\nВерно")
            else:
                self.outp_tsk_1.setText(f"Число {v_tsk} не является простым на промежутке [{self.v_tsk_1_p_a}, {self.v_tsk_1_p_b}]\nНеверно")
            self.inp_tsk_1.clear()
            self.update()
        except ValueError:
            self.outp_tsk_1.setText(f"Введи значение: \nцелое число")
            self.inp_tsk_1.clear()
            self.update()

    def click_btn_tsk_1_rst(self):
        try:
            self.v_tsk_1_p_a, self.v_tsk_1_p_b = elg.get_val_tsk_1_1_1()
            self.w_tsk_1_text.setText(
                f'\nНайди простое число на промежутке [{self.v_tsk_1_p_a}, {self.v_tsk_1_p_b}]\n')
            self.outp_tsk_1.setText(f"")
            self.inp_tsk_1.clear()
            self.update()
        except ValueError:
            print(ValueError)

    def click_btn_tsk_2_chk(self):
        try:
            v_tsk = int(self.inp_tsk_2.text())
            if (v_tsk in elg.get_primitive_roots(self.v_tsk_2)):
                self.outp_tsk_2.setText(f"Число {v_tsk} является первообразным корнем числа {self.v_tsk_2}\nВерно")
            else:
                self.outp_tsk_2.setText(f"Число {v_tsk} не является первообразным корнем числа {self.v_tsk_2}\nНеверно")
            self.inp_tsk_2.clear()
            self.update()
        except ValueError:
            self.outp_tsk_2.setText(f"Введи значение: \nцелое число")
            self.inp_tsk_2.clear()
            self.update()

    def click_btn_tsk_2_rst(self):
        try:
            self.v_tsk_2 = elg.get_val_tsk_1_1_2()
            self.w_tsk_2_text.setText(
                f'\nНайди первообразный корень числа {self.v_tsk_2}\n')
            self.outp_tsk_2.setText(f"")
            self.inp_tsk_2.clear()
            self.update()
        except ValueError:
            print(ValueError)
    
    def click_btn_tsk_3_chk(self):
        try:
            v_tsk = int(self.inp_tsk_3.text())
            if (v_tsk == binary_pow(self.v_tsk_3_g, self.v_tsk_3_x, self.v_tsk_3_p)):
                self.outp_tsk_3.setText(f"<p>{v_tsk} &#8801; {self.v_tsk_3_g}<sup>{self.v_tsk_3_x}</sup> (mod {self.v_tsk_3_p})</p><p>Верно</p>")
            else:
                self.outp_tsk_3.setText(f"<p>{v_tsk} &#8800; {self.v_tsk_3_g}<sup>{self.v_tsk_3_x}</sup> (mod {self.v_tsk_3_p})</p><p>Неверно</p>")
            self.inp_tsk_3.clear()
            self.update()
        except ValueError:
            self.outp_tsk_3.setText(f"Введи значение: \nцелое число")

    def click_btn_tsk_3_rst(self):
        try:
            self.v_tsk_3_g, self.v_tsk_3_x, self.v_tsk_3_p = elg.get_val_tsk_1_1_3()
            self.w_tsk_3_text.setText(
                f'<p>Найди y &#8801; {self.v_tsk_3_g}<sup>{self.v_tsk_3_x}</sup> (mod {self.v_tsk_3_p})</p><p></p>')
            self.outp_tsk_3.setText(f"")
            self.inp_tsk_3.clear()
            self.update()
        except ValueError:
            print(ValueError)
            self.inp_tsk_3.clear()
            self.update()


def win_1_1(w):

    w.window = Window_1_1()
    w.window.show()

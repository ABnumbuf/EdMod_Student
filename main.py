# This Python file uses the following encoding: windows-1251

import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui
import mod_1_sub_1, mod_1_sub_2, mod_1_sub_3 \
    , mod_2_sub_1 , mod_2_sub_2, mod_2_sub_3 \
    , mod_3_sub_1, mod_3_sub_2, mod_3_sub_3 \
    , mod_4
import oracledb
import datetime

mods = ['ЭЦП по схеме Эль-Гамаля'
        ,'Задача дискретного логарифмирования'
        ,'Рюкзачная криптосистема'
        , 'Тестирование']
sub_1 = ['Генерация ключей'
        ,'Создание подписи'
        ,'Валидация подписи']
sub_2 = ['Метод согласования'
        ,'Метод СПХ'
        ,'Время выполнения']
sub_3 = ['Задача о рюкзаке'
        ,'Алгоритм шифрования'
        ,'Алгоритм дешифрования']


class MainWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('EdMod Student')
        self.setFixedSize(650, 300)
        self.setFont(QFont('Arial', 12))
        self.main_layout = QGridLayout(self)
        self.setLayout(self.main_layout)

        self.current_win = 0
        self.user_name = ''

        self.w_lb_EdMod = QLabel("EdMod")
        self.w_lb_EdMod.setFont(QFont('Arial', 50))
        self.w_lb_EdMod.setAlignment(QtCore.Qt.AlignHCenter)
        self.w_lb_CryptMeth = QLabel("Криптографические методы")
        self.w_lb_CryptMeth.setAlignment(QtCore.Qt.AlignHCenter)
        self.w_lb_CryptMeth.setFixedHeight(110)

        self.w_lb_log_info = QLabel("Студент")
        self.w_lb_log_msg = QLabel("")
        self.w_lb_username = QLabel("Имя:")
        self.inp_user_name = QLineEdit()
        self.w_lb_userpasw = QLabel("Пароль:")
        self.inp_user_pasw = QLineEdit()
        self.inp_user_pasw.setEchoMode(QLineEdit.Password)
        self.btn_log = QPushButton("Войти")
        self.btn_log.clicked.connect(self.click_btn_log)

        self.w_lb_chs = QLabel("Выберите раздел")
        self.w_lb_chs.setAlignment(QtCore.Qt.AlignHCenter)
        self.w_cmb_mods = QComboBox()
        self.w_cmb_mods.addItems(mods)
        self.btn_next = QPushButton("Далее")
        self.btn_next.clicked.connect(self.click_btn_next)
        self.btn_back = QPushButton("Назад")
        self.btn_back.clicked.connect(self.click_btn_back)

        self.main_layout.addWidget(self.w_lb_log_info, 0, 0, 1, 3, QtCore.Qt.AlignRight)
        self.main_layout.addWidget(self.w_lb_EdMod, 1, 0, 1, 3, QtCore.Qt.AlignBottom)
        self.main_layout.addWidget(self.w_lb_CryptMeth, 2, 0, 1, 3, QtCore.Qt.AlignTop)

        self.main_layout.addWidget(self.w_lb_log_msg, 3, 0, 1, 3, QtCore.Qt.AlignLeft)
        
        self.main_layout.addWidget(self.w_lb_username, 4, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.main_layout.addWidget(self.inp_user_name, 4, 1, 1, 1)
     
        self.main_layout.addWidget(self.w_lb_userpasw, 5, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.main_layout.addWidget(self.inp_user_pasw, 5, 1, 1, 1)

        self.main_layout.addWidget(self.btn_log, 5, 2, 1, 1)

    def click_btn_log(self):
        try:
            self.user_name = self.inp_user_name.text().lower()
            self.user_pasw = self.inp_user_pasw.text()

            if self.user_name and self.user_pasw:

                try:

                    oracledb.init_oracle_client()

                    self.connection = oracledb.connect(
                    user="edmod",
                    password="edmod",
                    host="192.168.92.60",
                    port="49161",
                    service_name="xe")

                    if self.connection: print(f"Successfully connected to Database: {datetime.datetime.now()}")
                    else: print(f"Error with connect to Database: {datetime.datetime.now()}")
                except ValueError:
                    print(f"ERROR")
                    return 0

                sql = f"SELECT user_name, user_pasw FROM USERS where user_name='{self.user_name}'"
                
                cursor = self.connection.cursor()
                cursor.execute(sql)
                user = cursor.fetchall()

                if not user:
                    self.w_lb_log_msg.setText(f'Пользователь не найден')
                elif user[0][1] == self.user_pasw:
                    print(f"Successfully logged {self.user_name}: {datetime.datetime.now()}")

                    self.current_win = 1

                    self.w_lb_log_info.setText(f"Студент - {self.user_name}")

                    self.w_lb_log_msg.setParent(None)
                    self.w_lb_username.setParent(None)
                    self.inp_user_name.setParent(None)
                    self.w_lb_userpasw.setParent(None)
                    self.inp_user_pasw.setParent(None)
                    self.btn_log.setParent(None)

                    self.main_layout.addWidget(self.w_lb_chs, 3, 0, 1, 1, QtCore.Qt.AlignBottom)
                    self.main_layout.addWidget(self.w_cmb_mods, 4, 0, 1, 1)
                    self.main_layout.addWidget(self.btn_next, 4, 1, 1, 1)
                    self.main_layout.addWidget(self.btn_back, 4, 2, 1, 1)

                else: self.w_lb_log_msg.setText(f'Неверный пароль')
            else: self.w_lb_log_msg.setText(f'Введите значения')
            self.update()
        except ValueError:
            print(f"ERROR")
            return 0
    
    
    def click_btn_next(self):
        try:
            choosed_mod = self.w_cmb_mods.currentText()
            print(f"Mod [{choosed_mod}] chosen {datetime.datetime.now()}")
            if choosed_mod in mods:

                self.current_win = 2
                self.w_cmb_mods.clear()
                self.w_lb_chs.setText(choosed_mod)
                if choosed_mod == mods[0]: self.w_cmb_mods.addItems(sub_1)
                elif choosed_mod == mods[1]: self.w_cmb_mods.addItems(sub_2)
                elif choosed_mod == mods[2]: self.w_cmb_mods.addItems(sub_3)
                elif choosed_mod == mods[3]:
                    mod_4.win_4(self, self.user_name)
                    self.w_cmb_mods.clear()
                    self.w_cmb_mods.addItems(mods)

            else:
                self.current_win = 1
                if   choosed_mod == sub_1[0]: mod_1_sub_1.win_1_1(self)
                elif choosed_mod == sub_1[1]: mod_1_sub_2.win_1_2(self)
                elif choosed_mod == sub_1[2]: mod_1_sub_3.win_1_3(self)
                elif choosed_mod == sub_2[0]: mod_2_sub_1.win_2_1(self)
                elif choosed_mod == sub_2[1]: mod_2_sub_2.win_2_2(self)
                elif choosed_mod == sub_2[2]: mod_2_sub_3.win_2_3(self)
                elif choosed_mod == sub_3[0]: mod_3_sub_1.win_3_1(self)
                elif choosed_mod == sub_3[1]: mod_3_sub_2.win_3_2(self)
                elif choosed_mod == sub_3[2]: mod_3_sub_3.win_3_3(self)
                self.w_cmb_mods.clear()
                self.w_cmb_mods.addItems(mods)
                self.w_lb_chs.setText('Выбери раздел')
            
            self.update()
        except ValueError:
            print(f"ERROR")
            return 0
        
    def click_btn_back(self):
        try:
            if self.current_win == 1:

                self.current_win = 0

                self.w_lb_log_info.setText('Студент')
                self.w_lb_log_msg.setText('')

                self.w_lb_chs.setParent(None)
                self.w_cmb_mods.setParent(None)
                self.btn_next.setParent(None)
                self.btn_back.setParent(None)
                
                self.main_layout.addWidget(self.w_lb_log_msg, 3, 0, 1, 3, QtCore.Qt.AlignLeft)
        
                self.main_layout.addWidget(self.w_lb_username, 4, 0, 1, 1, QtCore.Qt.AlignLeft)
                self.main_layout.addWidget(self.inp_user_name, 4, 1, 1, 1)
            
                self.main_layout.addWidget(self.w_lb_userpasw, 5, 0, 1, 1, QtCore.Qt.AlignLeft)
                self.main_layout.addWidget(self.inp_user_pasw, 5, 1, 1, 1)

                self.main_layout.addWidget(self.btn_log, 5, 2, 1, 1)

            elif self.current_win == 2:

                self.current_win = 1

                self.w_cmb_mods.clear()
                self.w_cmb_mods.addItems(mods)
                self.w_lb_chs.setText('Выбери раздел')
            
            self.update()
        except ValueError:
            print(f"ERROR")
            return 0


if __name__ == '__main__':
    app = QApplication(sys.argv)

    app.setStyle('Fusion')

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

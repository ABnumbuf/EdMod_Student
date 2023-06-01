# This Python file uses the following encoding: windows-1251

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5 import QtCore
import datetime
import My_ElGamal as elg
import My_Knapsack as ks
import My_DiscrtLog as dis
from util import binary_pow, get_values
import oracledb


list_mod = ['Генерация ключей'
            ,'Создание подписи'
            ,'Валидация подписи'
            ,'Задача дискретного логарифмирования'
            ,'Задача о рюкзаке'
            ,'Алгоритм шифрования'
            ,'Алгоритм дешифрования']


class Window_4(QWidget):

    def __init__(self, user_name, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.user_name = user_name

        self.setWindowTitle('Тестирование')
        self.setFixedSize(1000, 770)
        self.setFont(QFont('Arial', 12))
        main_layout = QGridLayout(self)
        self.setLayout(main_layout)
        self.w_chb_1_1 = QCheckBox(list_mod[0])
        self.w_chb_1_2 = QCheckBox(list_mod[1])
        self.w_chb_1_3 = QCheckBox(list_mod[2])
        self.w_chb_2   = QCheckBox(list_mod[3])
        self.w_chb_3_1 = QCheckBox(list_mod[4])
        self.w_chb_3_2 = QCheckBox(list_mod[5])
        self.w_chb_3_3 = QCheckBox(list_mod[6])
        self.w_btn_strt = QPushButton("Начать")
        self.w_btn_strt.clicked.connect(self.click_btn_strt)
        self.w_btn_fnsh = QPushButton("Завершить")
        self.w_btn_fnsh.clicked.connect(self.click_btn_fnsh)
        self.w_btn_my_stat = QPushButton("Моя статистика")
        self.w_btn_my_stat.clicked.connect(self.click_btn_my_stat)

        self.w_scrollArea = QScrollArea()
        self.w_inp_1 = QLineEdit()
        self.w_inp_2 = QLineEdit()
        self.w_inp_3 = QLineEdit()
        self.w_inp_4 = QLineEdit()
        self.w_inp_5 = QLineEdit()
        self.w_inp_6 = QLineEdit()
        self.w_inp_7 = QLineEdit()
        self.w_outp = QTextBrowser()
        self.list_inp = [self.w_inp_1, 
                    self.w_inp_2,
                    self.w_inp_3,
                    self.w_inp_4,
                    self.w_inp_5,
                    self.w_inp_6,
                    self.w_inp_7]
        self.outp = ''
        
        main_layout.addWidget(QLabel(f'Студент - {self.user_name}'),         0, 0, 1, 1, alignment=QtCore.Qt.AlignLeft)
        main_layout.addWidget(self.w_scrollArea,                             1, 0, 14, 1)
        main_layout.addWidget(QLabel("ЭЦП по схеме Эль-Гамаля"),             1, 1, 1, 2, alignment=QtCore.Qt.AlignHCenter)
        main_layout.addWidget(self.w_chb_1_1,                                2, 1, 1, 2)
        main_layout.addWidget(self.w_chb_1_2,                                3, 1, 1, 2)
        main_layout.addWidget(self.w_chb_1_3,                                4, 1, 1, 2)
        main_layout.addWidget(QLabel("Задача дискретного логарифмирования"), 5, 1, 1, 2, alignment=QtCore.Qt.AlignHCenter)
        main_layout.addWidget(self.w_chb_2,                                  6, 1, 1, 2)
        main_layout.addWidget(QLabel("Рюкзачная криптосистема"),             7, 1, 1, 2, alignment=QtCore.Qt.AlignHCenter)
        main_layout.addWidget(self.w_chb_3_1,                                8, 1, 1, 2)
        main_layout.addWidget(self.w_chb_3_2,                                9, 1, 1, 2)
        main_layout.addWidget(self.w_chb_3_3,                               10, 1, 1, 2)
        main_layout.addWidget(self.w_btn_strt,                              11, 1, 1, 1)
        main_layout.addWidget(self.w_btn_fnsh,                              11, 2, 1, 1)
        main_layout.addWidget(self.w_btn_my_stat,                           12, 1, 1, 2)
        main_layout.addWidget(self.w_outp,                                  13, 1, 1, 2)

        self.count = 0
        try:
                oracledb.init_oracle_client()
                self.connection = oracledb.connect(
                                        user="student",
                                        password="student",
                                        host="192.168.92.60",
                                        port="49161",
                                        service_name="xe")
                print(f"Successfully connected to Database: {datetime.datetime.now()}") if self.connection else print(f"Error with connect to Database: {datetime.datetime.now()}")
        except ValueError:
            print(f"ERROR")
            return 0

        sql = f"SELECT user_id FROM EDMOD.USERS where user_name='{self.user_name}'"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.user_id = int(cursor.fetchall()[0][0])
        


    def click_btn_strt(self):
        try:
            
            self.w_w_scroll = QWidget()
            self.w_box_tst = QVBoxLayout()
            self.test_plan = [self.w_chb_1_1.isChecked(),
                            self.w_chb_1_2.isChecked(),
                            self.w_chb_1_3.isChecked(),
                            self.w_chb_2.isChecked(),
                            self.w_chb_3_1.isChecked(),
                            self.w_chb_3_2.isChecked(),
                            self.w_chb_3_3.isChecked()]
            self.w_inp_1 = QLineEdit()
            self.w_inp_2 = QLineEdit()
            self.w_inp_3 = QLineEdit()
            self.w_inp_4 = QLineEdit()
            self.w_inp_5 = QLineEdit()
            self.w_inp_6 = QLineEdit()
            self.w_inp_7 = QLineEdit()
            self.list_inp = [self.w_inp_1, 
                            self.w_inp_2,
                            self.w_inp_3,
                            self.w_inp_4,
                            self.w_inp_5,
                            self.w_inp_6,
                            self.w_inp_7]
            self.test_ans = [''  for i in self.test_plan]
            self.outp = ""
            self.result_to_bd = [0 for i in range(len(list_mod)*2)]
            self.count = 0
            for i in range(len(self.test_plan)):
                if self.test_plan[i]:
                    self.count +=1
                    self.w_box_tst.addWidget(QLabel(f"Задача {self.count}: {list_mod[i]}"))
                    self.outp += f"\nЗадача {self.count}: {list_mod[i]}"
                    if i == 0:
                        self.result_to_bd[0] = 1
                        v_tsk_1_p, v_tsk_1_g, v_tsk_1_x = elg.get_val_tsk_1_1_3()
                        self.test_ans[i] = str(binary_pow(v_tsk_1_g, v_tsk_1_x, v_tsk_1_p))
                        w_tsk_1_text = QLabel(
                            f'<p>Найди y &#8801; {v_tsk_1_g}<sup>{v_tsk_1_x}</sup> (mod {v_tsk_1_p})</p>')
                        self.outp += f'<p>Найди y &#8801; {v_tsk_1_g}<sup>{v_tsk_1_x}</sup> (mod {v_tsk_1_p})</p>'
                        self.w_box_tst.addWidget(w_tsk_1_text)
                    elif i == 1:
                        self.result_to_bd[2] = 1
                        v_tsk_2_p, v_tsk_2_g, v_tsk_2_x, v_tsk_2_m = elg.get_val_tsk_1_2()
                        self.test_ans[i] = str(elg.ds_ElGamal(v_tsk_2_m, v_tsk_2_p, v_tsk_2_g, v_tsk_2_x))
                        self.w_tsk_2_text = QLabel(
                                f'Найди значения подписи для: \np = {v_tsk_2_p}, \ng = {v_tsk_2_g}, \nx = {v_tsk_2_x}, \nm = {v_tsk_2_m}')
                        self.outp += f'\nНайди значения подписи для: \np = {v_tsk_2_p}, \ng = {v_tsk_2_g}, \nx = {v_tsk_2_x}, \nm = {v_tsk_2_m}'
                        self.w_box_tst.addWidget(self.w_tsk_2_text)
                    elif i == 2:
                        self.result_to_bd[4] = 1
                        v_tsk_3_m, v_tsk_3_p, v_tsk_3_g, v_tsk_3_y, v_tsk_3_r, v_tsk_3_s = elg.get_val_tsk_1_3()
                        self.test_ans[i] = str(elg.check_ds_ElGamal(v_tsk_3_m, v_tsk_3_r, v_tsk_3_s, v_tsk_3_y, v_tsk_3_g, v_tsk_3_p))
                        self.w_tsk_3_text = QLabel(
                                f'Являеется ли подпись правильной для: \np = {v_tsk_3_p}, g = {v_tsk_3_g}, y = {v_tsk_3_y}, \nm = {v_tsk_3_m}, \nr = {v_tsk_3_r}, s = {v_tsk_3_s}')
                        self.outp += f'\nЯвляеется ли подпись правильной для: \np = {v_tsk_3_p}, g = {v_tsk_3_g}, y = {v_tsk_3_y}, \nm = {v_tsk_3_m}, \nr = {v_tsk_3_r}, s = {v_tsk_3_s}'
                        self.w_box_tst.addWidget(self.w_tsk_3_text)
                    elif i == 3:
                        self.result_to_bd[6] = 1
                        v_tsk_4_a, v_tsk_4_b, v_tsk_4_n = get_values(1)[0]
                        self.test_ans[i] = str(dis.coherence_method(v_tsk_4_a, v_tsk_4_b, v_tsk_4_n))
                        while self.test_ans[i] == 'None':
                            v_tsk_4_a, v_tsk_4_b, v_tsk_4_n = get_values(1)[0]
                            self.test_ans[i] = str(dis.coherence_method(v_tsk_4_a, v_tsk_4_b, v_tsk_4_n))
                        self.w_tsk_4_text = QLabel(
                                f'<p>Реши задачу: <box>{v_tsk_4_a}<sup>x</sup></box> &#8801; {v_tsk_4_b} (mod {v_tsk_4_n})</p>')
                        self.outp += f'<p>Реши задачу: <box>{v_tsk_4_a}<sup>x</sup></box> &#8801; {v_tsk_4_b} (mod {v_tsk_4_n})</p>'
                        self.w_box_tst.addWidget(self.w_tsk_4_text)
                    elif i == 4:
                        self.result_to_bd[8] = 1
                        v_tsk_5_w, v_tsk_5_s = ks.get_val_tsk_3_1()
                        self.test_ans[i] = str(ks.knapSack(v_tsk_5_w, v_tsk_5_s))
                        self.w_tsk_5_text = QLabel(
                                f'Реши задачу о рюкзаке:\nw = {v_tsk_5_w}\ns = {v_tsk_5_s}')
                        self.outp += f'\nРеши задачу о рюкзаке:\nw = {v_tsk_5_w}\ns = {v_tsk_5_s}'
                        self.w_box_tst.addWidget(self.w_tsk_5_text)
                    elif i == 5:
                        self.result_to_bd[10] = 1
                        v_tsk_6_w, v_tsk_6_m, v_tsk_6_v, v_tsk_6_text = ks.get_val_tsk_3_2()
                        self.test_ans[i] = str(ks.ks_encrypt(v_tsk_6_w, v_tsk_6_m, v_tsk_6_v, v_tsk_6_text))
                        self.w_tsk_6_text = QLabel(
                                 f'Зашифруй сообщение: \n{v_tsk_6_text}\nv = {v_tsk_6_v}\nw = {v_tsk_6_w}\nm = {v_tsk_6_m}')
                        self.outp += f'\nЗашифруй сообщение: \n{v_tsk_6_text}\nv = {v_tsk_6_v}\nw = {v_tsk_6_w}\nm = {v_tsk_6_m}'
                        self.w_box_tst.addWidget(self.w_tsk_6_text)
                    elif i == 6:
                        self.result_to_bd[12] = 1
                        v_tsk_7_w, v_tsk_7_m, v_tsk_7_v, v_tsk_7_crypt = ks.get_val_tsk_3_3()
                        self.test_ans[i] = str(ks.ks_decrypt(v_tsk_7_w, v_tsk_7_m, v_tsk_7_v, v_tsk_7_crypt))
                        self.w_tsk_7_text = QLabel(
                                f'Расшифруй сообщение: \n{v_tsk_7_crypt}\nv = {v_tsk_7_v}\nw = {v_tsk_7_w}\nm = {v_tsk_7_m}')
                        self.outp += f'\nРасшифруй сообщение: \n{v_tsk_7_crypt}\nv = {v_tsk_7_v}\nw = {v_tsk_7_w}\nm = {v_tsk_7_m}'
                        
                        self.w_box_tst.addWidget(self.w_tsk_7_text)
                    self.outp += f'\nПравильный ответ: {self.test_ans[i]}'
                    
                    self.w_box_tst.addWidget(QLabel("Ответ: "))
                    self.w_box_tst.addWidget(self.list_inp[i])
                    
            self.w_w_scroll.setLayout(self.w_box_tst)
            self.w_scrollArea.setWidget(self.w_w_scroll)
            print(str(self.test_ans))
            self.update()
        except ValueError:
            self.update()
            return 0


    def click_btn_fnsh(self):
        try:
            rght_ans = 0
            self.outp2 = ''
            if self.count:
                number_of_task = 1
                for i in range(len(self.test_plan)):
                    if self.test_plan[i]:
                        self.outp2 += f"Задача {number_of_task} - "
                        if str(self.list_inp[i].text()) == self.test_ans[i]:
                            self.outp2 += "Верно\n"
                            self.result_to_bd[i*2+1] = 1
                            rght_ans += 1
                        else: self.outp2 += "Неверно\n"
                        number_of_task += 1
                self.outp2 += f"\nРезультат: {round(rght_ans/sum(1 for x in self.test_plan if x), 2)*100}%"
                print(self.result_to_bd)
                self.w_outp.setText(self.outp2)
                self.outp += self.outp2

                insert_in_result = [self.user_id]
                for i in self.result_to_bd: insert_in_result.append(i)
                print(insert_in_result)

                sql = f"insert into edmod.results values(:1, CURRENT_DATE, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14, :15)"
                with self.connection.cursor() as cursor:
                    cursor.execute(sql, insert_in_result)
                    print(f"Successfully insert the result of {self.user_name}: {datetime.datetime.now()}")
                self.connection.commit()

                self.w_w_scroll.setParent(None)
                
                self.update()
        except ValueError:
            self.update()
            return 0
        with open(f'statistics_{self.user_name}.txt', mode="a", encoding="windows-1251") as f:
                f.write(f"\n{str(datetime.datetime.now())}{self.outp}")

    def click_btn_my_stat(self):
        try:
            output_stat = ''

            oracledb.init_oracle_client()
            self.connection = oracledb.connect(
                                        user="student",
                                        password="student",
                                        host="192.168.92.60",
                                        port="49161",
                                        service_name="xe")
            print(f"Successfully connected to Database: {datetime.datetime.now()}") if self.connection else print(f"Error with connect to Database: {datetime.datetime.now()}")

            sql = f"SELECT sum(mod_1_sub_1), sum(answer_mod_1_sub_1), \
                            sum(mod_1_sub_2), sum(answer_mod_1_sub_2), \
                            sum(mod_1_sub_3), sum(answer_mod_1_sub_3),\
                            sum(mod_2), sum(answer_mod_2),\
                            sum(mod_3_sub_1), sum(answer_mod_3_sub_1), \
                            sum(mod_3_sub_2), sum(answer_mod_3_sub_2), \
                            sum(mod_3_sub_3), sum(answer_mod_3_sub_3)\
                    FROM EDMOD.results R JOIN EDMOD.USERS u ON R.user_id = u.user_id where r.user_id = {self.user_id}"
            cursor = self.connection.cursor()

            for row in cursor.execute(sql):
                number_of_mod = 0
                for j in range(0, len(row), 2):
                    output_stat += f'{list_mod[number_of_mod]}: {row[j+1]}/{row[j]} - {row[j+1]*100 // row[j] if row[j] else 0}%\n'
                    number_of_mod += 1

            self.w_outp.setText(output_stat)
            self.update()
        except ValueError:
            self.update()
            return 0


def win_4(w, user_name):
    w.window = Window_4(user_name=user_name)
    w.window.show()

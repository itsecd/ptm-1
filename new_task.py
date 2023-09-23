import os
import time
import datetime

from tkinter import Tk, Label, Button, Entry, StringVar, Spinbox, \
    filedialog as fd, messagebox as mb, scrolledtext, INSERT, END
from PIL import ImageTk, Image, ImageChops

import runpy
import speech_recognition as sr

FACE_FILE_NAME = ''
VOICE_FILE_NAME = ''
CURRENT_NAME = ''
CURRENT_LAST_NAME = ''
CURRENT_FACE_FILE_NAME = ''
CURRENT_VOICE_FILE_NAME = ''
IS_FIRST = 0
K = 0


def auth_button():
    def current_face_btn_pressed():
        global CURRENT_FACE_FILE_NAME
        CURRENT_FACE_FILE_NAME = fd.askopenfilename()
        wn1.focus_force()

    def current_voice_btn_pressed():
        def start_voice():
            global IS_FIRST
            global lbl4

            def end_voice():
                global IS_FIRST
                wn3.destroy()
                IS_FIRST = 0

            try:
                mic = sr.Microphone(device_index=1)
                r = sr.Recognizer()
                with mic as source:
                    print("Говорите:")
                    audio = r.listen(source)
            except:
                mb.showerror("Ошибка", "Проверьте подключение микрофона!")
                wn3.focus_force()
            try:
                a = r.recognize_google(audio, language="ru_RU")
            except sr.UnknownValueError:
                a = "Повторите попытку!"
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                a = "Повторите попытку!"
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
            lbl3 = Label(wn3, text="Ваше слово:", font=("Times New Roman", 14))
            lbl3.place(x=60, y=170)

            print(IS_FIRST)
            if IS_FIRST == 1:
                lbl4.destroy()
            lbl4 = Label(wn3, text=a, font=("Times New Roman", 20))
            lbl4.place(x=200, y=200)

            IS_FIRST = 1
            print(a)
            global CURRENT_VOICE_FILE_NAME
            CURRENT_VOICE_FILE_NAME = str.lower(a)
            print(CURRENT_VOICE_FILE_NAME)
            dal_btn = Button(wn3, text="Продолжить", font="18", command=end_voice)
            dal_btn.place(x='150', y='310', height=40, width=160)

        wn3 = Tk()
        wn3.geometry('450x400')
        wn3.title("Голосовой вход")
        lbl = Label(wn3, text="Нажмите кнопку,после чего\n произнесите кодовое слово.", font=("Times New Roman", 20))
        lbl.place(x=60, y=20)
        start_btn = Button(wn3, text="Начать", font="18", command=start_voice)
        start_btn.place(x='150', y='110', height=40, width=160)
        # wn1.focus_force()

    def log_in():
        def update_clock():
            start = datetime.datetime(2021, 5, 10, int(cur_h), int(cur_m[:-1]), int(cur_s))
            end = datetime.datetime(2021, 5, 10, int(time.strftime("%H")), int(time.strftime("%M")),
                                    int(time.strftime("%S")))
            delta = end - start
            now = time.strftime("%H:%M:%S")
            label.configure(text=delta)
            wn5.after(1000, update_clock)

        def prin():
            # print("h(",cur_h,") m(",cur_m,') s(',cur_s)
            if int(cur_h) >= 9 and int(str(cur_m)[:-1]) >= 0 and int(cur_s) >= 0:
                f1.write("Опоздание: " + str(int(cur_h) - 9) + ":" + str(cur_m) + str(cur_s) + '\n')
            else:
                f1.write("Опоздание: нет" + "\n")
            f1.write("Время отбытия: " + str(time.strftime("%H:%M:%S")) + '\n')
            start = datetime.datetime(2021, 5, 10, int(cur_h), int(cur_m[:-1]), int(cur_s))
            end = datetime.datetime(2021, 5, 10, int(time.strftime("%H")), int(time.strftime("%M")),
                                    int(time.strftime("%S")))
            delta = end - start
            f1.write("Активное время: " + str(delta) + "\n")
            f1.write("-------------------------------------------------" + "\n")
            print(str(delta))
            wn5.destroy()
            f1.close()

        def clear_notice():
            try:
                os.remove("db-notice.txt")
                txt1.delete(1.0, END)
                txt1.insert(INSERT, "Нет уведомлений")
                mb.showinfo("Удалено", "Оповещения успешно удалены!")
                wn5.focus_force()
            except:
                mb.showerror("Ошибка", "Активных уведомлений нет!")
                wn5.focus_force()

        is_find = 0
        cur_s = 0
        cur_m = 0
        cur_h = 0
        var1 = {}
        var2 = {}

        asj = []
        k = 0
        try:
            f = open('db.txt', 'r')
        except:
            mb.showerror("Ошибка", "База данных отсутствует!")
            wn1.focus_force()
        for line in f:
            string = line.split("`")
            if login_entry.get() == string[2] and pass_entry.get() == string[3]:
                is_find = 1
                if CURRENT_FACE_FILE_NAME != '':
                    image_1 = Image.open(string[4])
                    image_2 = Image.open(CURRENT_FACE_FILE_NAME)
                    result = ImageChops.difference(image_1, image_2)
                    if result.getbbox() is None:
                        if CURRENT_VOICE_FILE_NAME == '':
                            if str.lower(string[5][:-1]) != CURRENT_VOICE_FILE_NAME:
                                current_name = string[1]
                                current_last_name = string[0]
                                mb.showinfo("Успешно!", "Вы успешно авторизировались!")
                                wn1.destroy()
                                wn5 = Tk()
                                wn5.geometry('900x500')
                                wn5.title("Личный кабинет")
                                wn5.protocol('WM_DELETE_WINDOW', prin)
                                inic = Label(wn5, text="Добро пожаловать, " + current_name + ' ' + current_last_name,
                                             font=("Times New Roman", 18))
                                inic.place(x=70, y=20)
                                exit_btn = Button(wn5, text="Выход", font="15", command=prin)
                                exit_btn.place(x='750', y='20', height=30, width=130)
                                Label(wn5, text="Задачи", font=("Times New Roman", 20)).place(x=150, y=60)
                                try:
                                    f2 = open('db-task.txt', 'r')
                                    for line in f2:
                                        k = k + 1
                                        var1[k] = Label(wn5, text=line, font=("Times New Roman", 14)).place(x=50,
                                                                                                            y=60 + k * 50)
                                    k = 0
                                except:
                                    Label(wn5, text="Актуальные задания отсутствуют!",
                                          font=("Times New Roman", 14)).place(x=50, y=120)
                                tasks = Label(wn5, text="Оповещения", font=("Times New Roman", 20))
                                tasks.place(x=590, y=60)
                                txt1 = scrolledtext.ScrolledText(wn5, width=40, height=15, font=("Times New Roman", 14))
                                txt1.place(x='480', y='110')
                                try:
                                    f1 = open('db-notice.txt', 'r')
                                    txt1.insert(INSERT, f1.read())
                                    f1.close()
                                    clrnr = Button(wn5, text="Очистить", font="15", command=clear_notice).place(x='700',
                                                                                                                y='450',
                                                                                                                height=30,
                                                                                                                width=130)

                                except:
                                    txt1.insert(INSERT, "Нет уведомлений")
                                lbll = Label(wn5, text="Время:", font=("Times New Roman", 20))
                                lbll.place(x=60, y=450)
                                label = Label(wn5, text="", font=('Times New Roman', 20), fg='green')
                                label.place(x=170, y=450)
                                f1 = open('db-time.txt', 'a')
                                f1.write("Пользователь: " + current_name + ' ' + current_last_name + '\n')
                                f1.write("Дата: " + str(time.strftime("%d.%m.%Y")) + '\n')
                                f1.write("Время прибытия: " + str(time.strftime("%H:%M:%S")) + '\n')
                                cur_s = time.strftime("%S")
                                cur_m = time.strftime("%M:")
                                cur_h = time.strftime("%H")
                                update_clock()

                            else:
                                mb.showerror("Ошибка", "Данные голоса неверны!")
                                wn1.focus_force()
                        else:
                            mb.showerror("Ошибка", "Введите данные голоса!")
                            wn1.focus_force()
                    else:
                        mb.showerror("Ошибка", "Данные лица не верны!")
                        result.save('result.jpg')
                        wn1.focus_force()
                    break
                else:
                    mb.showerror("Ошибка", "Введите данные лица!")
                    wn1.focus_force()
            else:
                print("1)", login_entry.get(), "=", string[2])
                print("2)", pass_entry.get(), "=", string[3])
        if is_find == 0:
            mb.showerror("Ошибка", "Введите все данные!")
            wn1.focus_force()

    global K
    K = K + 1
    wn1 = Tk()
    wn1.geometry('450x400')
    wn1.title("Авторизация")
    lbl = Label(wn1, text="Авторизация", font=("Arial", 25))
    lbl.place(x=120, y=35)

    lbl1 = Label(wn1, text="Логин", font=("Times New Roman", 14))
    lbl1.place(x=70, y=107)
    login_entry = Entry(wn1, width=25, textvariable=StringVar())
    login_entry.place(x=225, y=120, anchor="c")
    lbl1 = Label(wn1, text="Пароль", font=("Times New Roman", 14))
    lbl1.place(x=70, y=137)
    pass_entry = Entry(wn1, width=25, textvariable=StringVar())
    pass_entry.place(x=225, y=150, anchor="c")

    face_data = Label(wn1, text="Данные лица:", font=("Times New Roman", 14))
    face_data.place(x=70, y=174)

    face_btn = Button(wn1, text="Загрузить файл", font="15", command=current_face_btn_pressed)
    face_btn.place(x='170', y='210', height=30, width=130)

    voice_data = Label(wn1, text="Голосовое подтверждение:", font=("Times New Roman", 14))
    voice_data.place(x=70, y=254)

    face_btn = Button(wn1, text="Кодовое слово", font="15", command=current_voice_btn_pressed)
    face_btn.place(x='170', y='290', height=30, width=130)

    bt1 = Button(wn1, text="Ввод", font="15", command=log_in)
    bt1.place(x='160', y='345', height=30, width=130)


def btn2_button():
    def reg_btn():
        if len(name_entry.get()) <= 0 or len(last_name_entry.get()) <= 0 or len(login_entry.get()) <= 0 or len(
                passw_entry.get()) <= 0 or FACE_FILE_NAME == '' or len(code_entry.get()) <= 0:
            mb.showerror("Ошибка", "Заполните все поля!")
            wn2.focus_force()
        else:
            f = open('db.txt', 'a')
            f.write(last_name_entry.get() + '`')
            f.write(name_entry.get() + '`')
            f.write(login_entry.get() + '`')
            f.write(passw_entry.get() + '`')
            f.write(FACE_FILE_NAME + '`')
            f.write(code_entry.get())
            f.write("\n")
            f.close()

            mb.showinfo("Успешно!", "Вы успешно зарегистрировались!")
            global from_reg
            wn2.destroy()
            from_reg = True
            auth_button()

    def face_btn_pressed():
        global FACE_FILE_NAME
        FACE_FILE_NAME = fd.askopenfilename()
        print(FACE_FILE_NAME)
        wn2.focus_force()

    def voice_btn_pressed():
        global VOICE_FILE_NAME
        VOICE_FILE_NAME = fd.askopenfilename()
        print(VOICE_FILE_NAME)

    field_last_name = StringVar()
    field_name = StringVar()
    field_login = StringVar()
    field_pass = StringVar()

    wn2 = Tk()
    wn2.geometry('455x580')
    wn2.title("Регистрация")
    lbl = Label(wn2, text="Регистрация", font=("Times New Roman", 25))
    lbl.place(x=130, y=30)

    last_name = Label(wn2, text="Фамилия:", font=("Times New Roman", 14))
    last_name.place(x=90, y=110)
    last_name_entry = Entry(wn2, width=25, textvariable=field_last_name)
    last_name_entry.place(x=275, y=124, anchor="c")

    name = Label(wn2, text="Имя:", font=("Times New Roman", 14))
    name.place(x=90, y=146)
    name_entry = Entry(wn2, width=25, textvariable=field_name)
    name_entry.place(x=275, y=160, anchor="c")

    login = Label(wn2, text="Логин:", font=("Times New Roman", 14))
    login.place(x=90, y=182)
    login_entry = Entry(wn2, width=25, textvariable=field_login)
    login_entry.place(x=275, y=196, anchor="c")

    passw = Label(wn2, text="Пароль:", font=("Times New Roman", 14))
    passw.place(x=90, y=218)
    passw_entry = Entry(wn2, width=25, textvariable=field_pass)
    passw_entry.place(x=275, y=232, anchor="c")

    face_data = Label(wn2, text="Данные лица:", font=("Times New Roman", 14))
    face_data.place(x=90, y=254)

    face_btn = Button(wn2, text="Загрузить файл", font="15", command=face_btn_pressed)
    face_btn.place(x='200', y='285', height=30, width=130)

    voice_data = Label(wn2, text="Введите кодовое слово:", font=("Times New Roman", 14))
    voice_data.place(x=90, y=330)

    code_entry = Entry(wn2, width=25, textvariable=StringVar())
    code_entry.place(x=225, y=380, anchor="c")

    reg = Button(wn2, text="Зарегистрироваться", font="15", command=reg_btn)
    reg.place(x='140', y='485', height=30, width=180)


def btn3_button():
    def main_panel():
        def jornal():
            def back():
                wn6.destroy()

            def clear_journal():
                try:
                    os.remove("db-time.txt")
                    txt.delete(1.0, END)
                    mb.showinfo("Удалено", "Журнал успешно удален!")
                    wn6.focus_force()
                except:
                    mb.showerror("Ошибка", "Невозможно удалить журнал!")
                    wn6.focus_force()

            try:
                f = open('db-time.txt', 'r')
                wn6 = Tk()
                wn6.geometry('685x580')
                wn6.title("Журнал посещений")
                lbl11 = Label(wn6, text="Журнал", font=("Times New Roman", 25))
                lbl11.place(x=295, y=30)
                txt = scrolledtext.ScrolledText(wn6, width=50, height=10, font=("Times New Roman", 18))
                txt.place(x='40', y='90')
                for line in f:
                    txt.insert(INSERT, line)
                f.close()
                Button(wn6, text="Назад", font="15", command=back).place(x='40', y='520', height=25, width=130)
                Button(wn6, text="Очистить журнал", font="15", command=clear_journal).place(x='500', y='520', height=25,
                                                                                            width=160)
            except:
                mb.showerror("Ошибка", "Данные отсутствуют!")
                wn8.focus_force()

        def tasks():
            global last_x
            last_x = 0

            def make_tsk():
                btn5['state'] = 'disabled'
                global last_x
                var = {}
                entry_name = ['1', '2', '3', '4', '5']

                def command():
                    a = []
                    for i in range(int(spin.get())):
                        if var[i].get() == "":
                            mb.showerror("Ошибка", "Заполните все поля!")
                            wn7.focus_force()
                            break
                        else:
                            a.append(var[i].get())
                    f1 = open('db-task.txt', 'w')
                    for i in a:
                        f1.write(i + '\n')
                    f1.close()
                    wn7.destroy()

                def clear():
                    btn5['state'] = 'normal'
                    for i in range(4):
                        var[i].destroy()

                for x in range(int(spin.get())):
                    txt = Label(wn7, text=x)
                    var[x] = Entry(wn7, width=80)
                    var[x].place(x=110, y=200 + int(x) * 50)
                afk = Button(wn7, text="Добавить заметку", font="15", command=command)
                afk.place(x='300', y='490', height=25, width=140)

                clr = Button(wn7, text="Очистить", font="15", command=clear)
                clr.place(x='300', y='450', height=25, width=140)
                print(var)

            wn7 = Tk()
            wn7.geometry('685x580')
            wn7.title("Задания")
            lbl = Label(wn7, text="Задачи для работников", font=("Arial", 25))
            lbl.place(x=180, y=35)
            lbl1 = Label(wn7, text="Количество задач:", font=("Times New Roman", 18))
            lbl1.place(x=200, y=100)
            spin = Spinbox(wn7, from_=1, to=4, width=10)
            spin.place(x=405, y=109)
            btn5 = Button(wn7, text="Создать", font="15", command=make_tsk)
            btn5.place(x='300', y='144', height=25, width=100)

        def notice():
            def ttt():
                if txt.get("1.0", 'end-1c') != '':
                    f1 = open('db-notice.txt', 'w')
                    f1.write(txt.get("1.0", 'end-1c'))
                    print(txt.get("1.0", 'end-1c'))
                    f1.close()
                    wnn.destroy()
                else:
                    mb.showerror("Ошибка", "Заполните все поля!")
                    wnn.focus_force()

            wnn = Tk()
            wnn.geometry('450x500')
            wnn.title("Оповещения")
            Label(wnn, text="Создать оповещение", font=("Arial", 16)).place(x=120, y=30)
            txt = scrolledtext.ScrolledText(wnn, width=30, height=10, font=("Times New Roman", 18))
            txt.place(x='40', y='90')
            btn5 = Button(wnn, text="Создать", font="15", command=ttt)
            btn5.place(x='180', y='400', height=25, width=100)

        if login_entry.get() == 'admin' and pass_entry.get() == 'admin':
            wn1.destroy()
            wn8 = Tk()
            wn8.geometry('500x250')
            wn8.title("Панель Администратора")
            lbl = Label(wn8, text="Панель администратора", font=("Arial", 18))
            lbl.place(x=120, y=50)
            btn4 = Button(wn8, text="Журнал", font="15", command=jornal)
            btn4.place(x='40', y='120', height=30, width=120)
            btn5 = Button(wn8, text="Задачи", font="15", command=tasks)
            btn5.place(x='190', y='120', height=30, width=120)
            btn6 = Button(wn8, text="Оповещения", font="15", command=notice)
            btn6.place(x='340', y='120', height=30, width=120)
        else:
            mb.showerror("Ошибка", "Неверные данные!")
            wn1.focus_force()

    wn1 = Tk()
    wn1.geometry('450x250')
    wn1.title("Панель Администратора")
    lbl = Label(wn1, text="Панель администратора", font=("Times New Roman", 18))
    lbl.place(x=110, y=50)

    lbl1 = Label(wn1, text="Логин", font=("Times New Roman", 14))
    lbl1.place(x=70, y=107)
    login_entry = Entry(wn1, width=25, textvariable=StringVar())
    login_entry.place(x=225, y=120, anchor="c")
    lbl1 = Label(wn1, text="Пароль", font=("Times New Roman", 14))
    lbl1.place(x=70, y=137)
    pass_entry = Entry(wn1, width=25, textvariable=StringVar())
    pass_entry.place(x=225, y=150, anchor="c")
    bt1 = Button(wn1, text="Ввод", font="15", command=main_panel)
    bt1.place(x='160', y='185', height=30, width=130)


window = Tk()
window.geometry('900x500')
window.title("Главное меню")
path = r"logo.png"
# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))
# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = Label(window, image=img)
panel.place(x='315', y='10')

img1 = ImageTk.PhotoImage(Image.open("logo_ru.png").resize((180, 100)))
panel1 = Label(window, image=img1)
panel1.place(x='20', y='20')
# The Pack geometry manager packs widgets in rows or columns.
# panel.pack(side = "bottom", fill = "both", expand = "yes")


lbl = Label(window, text="Контроль рабочего\n времени и бизнес-процессов", font=("Ariel", 30))
lbl.place(x=180, y=155)

btn1 = Button(text="Авторизация", font="15", command=auth_button)
btn1.place(x='370', y='300', height=40, width=200)

btn2 = Button(text="Регистрация", font="15", command=btn2_button)
btn2.place(x='370', y='350', height=40, width=200)

btn3 = Button(text="Администрирование", font="15", command=btn3_button)
btn3.place(x='370', y='400', height=40, width=200)

window.mainloop()

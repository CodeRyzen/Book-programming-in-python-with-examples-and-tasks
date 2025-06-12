from tkinter import *
# Функция для обработки нажатия кнопки:
def clicked():
    global t
    # Считывается содержимое текстового поля
    t=txt.get()
    # Закрывается окно:
    wnd.destroy()
# Создается объект для первого окна:
wnd=Tk()
# Параметры окна:
wnd.title("Давайте познакомимся")
wnd.geometry("300x120")
wnd.resizable(False,False)
# Шрифты:
fnt_1=("Arial",13,"bold")
fnt_2=("Arial",13,"italic")
fnt_3=("Arial",10,"bold")
# Переменная для записи текста из поля ввода:
t=""
# Создание объекта для текстовой метки:
lbl=Label(master=wnd,text="Как Вас зовут?")
# Шрифт для метки:
lbl.configure(font=fnt_1)
# Добавление метки в окно:
lbl.place(x=10,y=20)
# Создание объекта для поля ввода:
txt=Entry(master=wnd,width=30)
# Шрифт для поля ввода:
txt.configure(font=fnt_2)
# Размещение текстового поля в окне:
txt.place(x=10,y=50)
# Создание объектов для кнопок:
btn_1=Button(master=wnd,text="OK")
btn_2=Button(master=wnd,text="Отмена")
# Параметры кнопок:
btn_1.configure(font=fnt_3)
btn_1.configure(command=clicked)
btn_2.configure(font=fnt_3)
btn_2.configure(command=wnd.destroy)
# Размещение кнопок в окне:
btn_1.place(x=40,y=80,width=100,height=30)
btn_2.place(x=150,y=80,width=100,height=30)
# Отображение первого окна на экране:
wnd.mainloop()
# Если пользователь ввел текст:
if t!="":
    # Создание объекта для второго окна:
    msg=Tk()
    # Параметры второго окна:
    msg.title("Знакомство состоялось")
    msg.geometry("320x100")
    msg.resizable(False,False)
    # Метка с сообщением для второго окна:
    lbl=Label(master=msg,text="Очень приятно, "+t+"!",relief=GROOVE)
    # Шрифт для метки:
    lbl.configure(font=fnt_1)
    # Размещение метки во втором окне:
    lbl.place(x=10,y=10,height=40,width=300)
    # Создание объекта кнопки:
    btn=Button(master=msg,text="OK")
    # Шрифт для кнопки:
    btn.configure(font=fnt_3)
    # Метод для обработки нажатия кнопки:
    btn.configure(command=msg.destroy)
    # Размещение кнопки во втором окне:
    btn.place(x=110,y=60,width=100,height=30)
    # Отображение второго окна на экране:
    msg.mainloop()

from tkinter import *
from math import *
# Функция для обработки события, связанного
# с наведением курсора на область рисования:
def msEnter(evt):
    # Смена изображения:
    cnv.itemconfig(Pct,image=img_2)
# Функция для обработки события, связанного
# с тем, что курсор покидает область рисования:
def msLeave(evt):
    # Смена изображения:
    cnv.itemconfig(Pct,image=img_1)
    # Удаление "старых" линий возле курсора:
    cnv.delete("ln")
# Функция для обработки события, связанного
# с перемещением курсора в области рисования:
def msMotion(evt):
    # Координаты курсора в области рисования:
    x=evt.x
    y=evt.y
    # Удаление "старых" линий:
    cnv.delete("ln")
    # Отображение линий:
    cnv.create_line(x,5,x,H-5,fill=clr_C1,width=2,tag="ln")
    cnv.create_line(5,y,W-5,y,fill=clr_C1,width=2,tag="ln")
    # Координаты прямоугольника:
    Rxy=cnv.coords(Rtn)
    # Координаты окружности:
    Cxy=cnv.coords(Crl)
    # Координаты центра окружности:
    x0=(Cxy[2]+Cxy[0])/2
    y0=(Cxy[3]+Cxy[1])/2
    # Расстояние от курсора до центра окружности:
    r=sqrt((x-x0)**2+(y-y0)**2)
    # Если курсор находится внутри окружности:
    if r<R:
        # Белый цвет заливки для окружности:
        cnv.itemconfig(Crl,fill=clr_C2)
        # Красный цвет заливки для прямоугольника:
        cnv.itemconfig(Rtn,fill=clr_C1)
        # Завершение выполнения функции:
        return
    # Если курсор находится вне окружности:
    else:
        # Красный цвет заливки для окружности:
        cnv.itemconfig(Crl,fill=clr_C1)
    # Если курсор находится внутри прямоугольника:
    if x>Rxy[0] and x<Rxy[2] and y>Rxy[1] and y<Rxy[3]:
        # Зеленый цвет заливки для прямоугольника:
        cnv.itemconfig(Rtn,fill=clr_R2)
    # Если курсор находится вне прямоугольника:
    else:
        # Белый цвет заливки для прямоугольника:
        cnv.itemconfig(Rtn,fill=clr_R1)
# Функция для обработки события, связанного
# с нажатием кнопки "вверх":
def msUp(evt):
    # Группа линий смещается на один пиксель вверх:
    cnv.move("Lns",0,-1)
    # Окружность смещается на три пикселя вниз:
    cnv.move(Crl,0,3)
# Функция для обработки события, связанного
# с нажатием кнопки "вниз":
def msDown(evt):
    # Группа линий смещается на один пиксель вверх:
    cnv.move("Lns",0,1)
    # Окружность смещается на три пикселя вверх:
    cnv.move(Crl,0,-3)
# Функция для обработки события, связанного
# с нажатием кнопки "влево":
def msLeft(evt):
    # Текст смещается на одну позицию влево:
    cnv.move(Txt,-1,0)
# Функция для обработки события, связанного
# с нажатием кнопки "вправо":
def msRight(evt):
    # Текст смещается на одну позицию вправо:
    cnv.move(Txt,1,0)
# Ширина и высота области рисования:
W=600
H=400
# Ширина и высота прямоугольника:
w=200
h=100
# Количество линий:
N=10
# Декремент для длины линий:
d=20
# Радиус окружности:
R=30
# Шрифт:
fnt=("Arial",20,"bold")
# Текст:
txt="Синий текст"
# Цвет для линий:
clr="lightgreen"
# Цвет для фона области рисования:
clr_1="lightyellow"
clr_2="yellow"
# Цвет для закраски окружности:
clr_C1="red"
clr_C2="white"
# Цвет для закраски прямоугольника:
clr_R1="white"
clr_R2="green"
# Создание объекта окна:
wnd=Tk()
# Размеры и положение окна:
wnd.geometry(str(W+10)+"x"+str(H+10)+"+400+300")
# Заголовок для окна:
wnd.title("Графика")
# Окно постоянных размеров:
wnd.resizable(False,False)
# Создание объекта для области рисования:
cnv=Canvas(wnd,bg=clr_1,bd=3,relief=GROOVE)
# Размещение области рисования в окне:
cnv.place(x=5,y=5,width=W,height=H)
# Передача фокуса области рисования:
cnv.focus_set()
# Создание текстового элемента:
Txt=cnv.create_text(W/2,50,text=txt,font=fnt,fill="blue")
# Создание группы горизонтальных линий:
for k in range(N):
    # Координаты линий:
    x1=70+k*d
    y1=H/4+10*k
    x2=W-70-d*k
    y2=H/4+10*k
    cnv.create_line(x1,y1,x2,y2,fill=clr,width=5,tag="Lns")
# Координаты для создания окружности:
x1=W/2-R
y1=H/2-R+30
x2=W/2+R
y2=H/2+R+30
# Создание окружности:
Crl=cnv.create_oval(x1,y1,x2,y2,fill=clr_C1)
# Координаты для создания прямоугольника:
x1=20
y1=H-h-20
x2=x1+w
y2=y1+h
# Создание прямоугольника:
Rtn=cnv.create_rectangle(x1,y1,x2,y2,fill=clr_R1)
# Создание объектов изображений:
img_1=PhotoImage(file="D:\\Pictures\\sad.png")
img_2=PhotoImage(file="D:\\Pictures\\smile.png")
# Создание объекта изображения:
Pct=cnv.create_image(W-20,H-20,anchor=SE,image=img_1)
# Регистрация обработчиков:
cnv.bind("<Left>",msLeft)
cnv.bind("<Right>",msRight)
cnv.bind("<Up>",msUp)
cnv.bind("<Down>",msDown)
cnv.bind("<Enter>",msEnter)
cnv.bind("<Leave>",msLeave)
cnv.bind("<Motion>",msMotion)
cnv.bind("<Button-1>",lambda evt: cnv.config(bg=clr_2))
cnv.bind("<Button-3>",lambda evt: cnv.config(bg=clr_1))
# Отображение главного окна:
wnd.mainloop()

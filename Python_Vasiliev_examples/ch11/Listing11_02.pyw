# Импорт классов из пакета:
from tkinter import *
# Создание объекта окна:
wnd=Tk()
# Заголовок для окна:
wnd.title("Окно с кнопкой")
# Геометрические размеры окна:
wnd.geometry("250x150")
# Окно постоянных размеров:
wnd.resizable(False,False)
# Создание объекта метки:
lbl=Label(wnd,text="Всем привет!",font=("Arial Bold",20))
# Размещение метки в окне:
lbl.place(x=40,y=30)
# Объект копки:
btn=Button(wnd,text="Закрыть",font=("Courier New Bold",13),command=wnd.destroy)
# Размещение объекта кнопки в окне:
btn.place(x=40,y=100,width=170,height=30)
# Отображение окна на экране:
wnd.mainloop()

from tkinter import *
import random, time
def bros():
    x=random.choice(['1.png','2.png', '3.png',
                     '4.png', '5.png', '6.png'])
    return x
def img(event):
    global b1, b2
    for i in range(18):
        b1 = PhotoImage(file=(bros()))
        b2 = PhotoImage(file=(bros()))
        lab1['image'] = b1
        lab2['image'] = b2
        root.update()#для обновления экрана, то есть не нужно самому нажимать на область окна для выбора кубика
        time.sleep(0.12)
root = Tk()
root.geometry('400x200')
root.title('Игра в кости. Сделай бросок!')
root.resizable(height = False, width = False) #Для того чтобы окошко игры не растягивалось, было фиксированным
root.iconphoto(True, PhotoImage(file=('iconka.png'))) #для отображения иконки игры с изображением из указанного файла
fon = PhotoImage(file=('holst.png'))#создание фона
Label(root, image=fon).pack()#создание метки, т.е. привязка к окошку тгры
lab1 = Label(root)#создание метки через переменную
lab1.place(relx=0.3, rely=0.5, anchor=CENTER)#расположение метки в определенной зоне
lab2 = Label(root)
lab2.place(relx=0.7, rely=0.5, anchor=CENTER)
root.bind('<1>', img)#вызов функции рандомного броска "левой кнопкой мыши"
img('event')#запись для того, чтобы убрать метки белые на начальном экране
root.mainloop()

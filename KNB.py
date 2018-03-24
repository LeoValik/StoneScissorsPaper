from tkinter import *
from tkinter import messagebox  # messagebox - подмодуль
from random import *
from time import *  #  Позволит нам приостанавливать циклы

pc_score = 0
user_score = 0
pc_figur = ""   #  То, что выбрал комп
user_figur = ""  # То, что выбирет игрок

def stone():    # При нажатии на кнопку Камень
    global user_figur # Что её видело вся программа, доступна с любой точки проги благодаря global
    Kbut["bg"]="green" # Указ имя кнопки, [], "", bg - background
    Nbut["bg"]="white"
    Bbut["bg"]="white"
    user_figur = "камень"
    PCbut["state"] = "normal" # После того, как мы выбрали камень,  кнопка Сгенерировать должна стать активной

def scissors(): # При нажатии на кнопку  Ножницы
    global user_figur
    Kbut["bg"]="white"
    Nbut["bg"]="green"
    Bbut["bg"]="white"
    user_figur = "ножницы"
    PCbut["state"] = "normal"

def paper():    # При нажатии на кнопку  Бумага
    global user_figur
    Kbut["bg"]="white"
    Nbut["bg"]="white"
    Bbut["bg"]="green"
    user_figur = "бумага"
    PCbut["state"] = "normal"

def go():  # При нажатии на кнопку  Сгенерировать
    global pc_figur, user_figur, user_score, pc_score # Все переменные делаем глобальными, так как они у нас будут менятся
    t4["text"] = "выбор pc - "
    for i in range(30): # 30 раз будет выполнятся этот код
        rand = randint(1,4)     # rand - случайная переменная, от 1 до 3-х, пишем 4 так как Четверка НЕ включается
        if rand == 1:
            pc_figur = "камень"
        if rand == 2:
            pc_figur = "ножницы"
        if rand == 3:
            pc_figur = "бумага"

        t4["text"] = "выбор pc - " + pc_figur
        t4.update() # Обновляем наш текст (точнее виджет)
        sleep(0.1)  # Должны подождать 0.1 секунду
        # Создали анимацию выбора компа (сверху код)
# НИЖЕ КОД ОТВЕЧАЕТ ЗА ТО, КТО ЖЕ ВЫИГРАЛ В ИГРЕ
    if pc_figur == user_figur:
        messagebox.showinfo("result", "Draw") # Выводит окошко-сообщение : result - заголовок, Draw - само сообщение

    else:
        if pc_figur=="камень" and user_figur=="ножницы":
            pc_score += 1
            messagebox.showinfo("result", "PC одержал победу")
        if pc_figur == "камень" and user_figur == "бумага":
            user_score += 1
            messagebox.showinfo("result", "Игрок Победил")

        if pc_figur=="ножницы" and user_figur=="бумага":
            pc_score += 1
            messagebox.showinfo("result", "PC одержал победу")
        if pc_figur == "ножницы" and user_figur == "камень":
            user_score += 1
            messagebox.showinfo("result", "Игрок Победил")

        if pc_figur=="бумага" and user_figur=="камень":
            pc_score += 1
            messagebox.showinfo("result", "PC одержал победу")
        if pc_figur == "бумага" and user_figur == "ножницы":
            user_score += 1
            messagebox.showinfo("result", "Игрок Победил")

        t5["text"] = "Игрок - " + str(user_score)
        t6["text"] = "PC - " + str(pc_score)

    PCbut["state"] = "disabled"

# ГРАФИЧЕСКАЯ ЧАСТЬ
root = Tk()     # Создается окно
root.title("Камень, ножницы, бумага") # Создается название этого окна

t1 = Label(root, text="Камень, ножницы, бумага", fg="red") # Первая надпись, заголовок, выдел. красным цветом
t1.grid(row=0, column=1)    # method grid = сетка (как будто таблица)
                            #  row - строка, column = столбец, нумерация с Нуля
t2 = Label(root, text="Выбор игрока", fg="green")
t2.grid(row=1, column=1)

Kbut=Button(root, text="Камень", command = stone)
Kbut.grid(row=2, column=0)
Nbut=Button(root, text="Ножницы", command = scissors)
Nbut.grid(row=2, column=1)
Bbut=Button(root, text="Бумага", command = paper)
Bbut.grid(row=2, column=2)

t3 = Label(root, text="Выбор Компьютера", fg="blue")
t3.grid(row=3, column=1)
PCbut=Button(root, text="Сгенерировать", command = go) # команда go - будет выполнять логику игры
PCbut["state"] ="disabled" # state - состояние, disabled - кнопка неактивна
                            # PCbut - указ имя кнопки, [] - параметр, state - имя параеметра, disabled - состояние
PCbut.grid(row=4, column=1)

t4 = Label(root, text="выбор pc - 0", fg="red" )
t4.grid(row=5, column=1)

t5 = Label(root, text="Игрок - 0", fg="green" ) #  Очки игрока
t5.grid(row=6, column=0)

t6 = Label(root, text="PC - 0", fg="blue" ) #  Очки компа
t6.grid(row=6, column=2)
root.mainloop()


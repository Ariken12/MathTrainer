from random import *
from tkinter import *
from time import *

class Main:

    def __init__(self):
        self.wndw = Tk()
        self.wndw.title("Train")
        self.answer = ''
        self.difficult = 0
        self.menu()

    def menu(self):
        self.info = Label(self.wndw, text="Выберите уровень тренеровки")
        self.dif1 = Button(self.wndw, text="1 уровень", command=self.difficult_1)
        self.dif2 = Button(self.wndw, text="2 уровень", command=self.difficult_2)
        self.dif3 = Button(self.wndw, text="3 уровень", command=self.difficult_3)
        self.dif4 = Button(self.wndw, text="4 уровень", command=self.difficult_4)
        self.dif5 = Button(self.wndw, text="5 уровень", command=self.difficult_5)
        self.back_to_menu = Button(self.wndw, text="Вернуться в меню", command=self.train_to_menu)
        self.info.pack()
        self.dif1.pack()
        self.dif2.pack()
        self.dif3.pack()
        self.dif4.pack()
        self.dif5.pack()
        self.wndw.mainloop()

    def clear(self):
        self.info.destroy()
        self.dif1.destroy()
        self.dif2.destroy()
        self.dif3.destroy()
        self.dif4.destroy()
        self.dif5.destroy()

    def difficult_1(self):
        self.clear()
        self.difficult = 1

        a = randint(1, 10)
        b = randint(1, 10)
        self.answer = str(a + b)
        text = "Сколько будет " + str(a) + " + " + str(b) + "?"

        self.time_begin = time()
        self.info = Label(self.wndw, text=text)
        self.input = Entry(self.wndw)
        self.time = Label(self.wndw)

        self.train()

    def difficult_2(self):
        self.clear()
        self.difficult = 2

        a = randint(1, 10)
        b = randint(1, 10)
        self.answer = str(a * b)
        text = "Сколько будет " + str(a) + " x " + str(b) + "?"

        self.time_begin = time()
        self.info = Label(self.wndw, text=text)
        self.input = Entry(self.wndw)
        self.time = Label(self.wndw)

        self.train()

    def difficult_3(self):
        self.clear()
        self.difficult = 3

        a = randint(10, 99)
        b = randint(10, 99)
        self.answer = str(a + b)
        text = "Сколько будет " + str(a) + " + " + str(b) + "?"

        self.time_begin = time()
        self.info = Label(self.wndw, text=text)
        self.input = Entry(self.wndw)
        self.time = Label(self.wndw)

        self.train()

    def difficult_4(self):
        self.clear()
        self.difficult = 4

        a = randint(10, 99)
        b = randint(2, 9)
        self.answer = str(a * b)
        text = "Сколько будет " + str(a) + " x " + str(b) + "?"

        self.time_begin = time()
        self.info = Label(self.wndw, text=text)
        self.input = Entry(self.wndw)
        self.time = Label(self.wndw)

        self.train()

    def difficult_5(self):
        self.clear()
        self.difficult = 5

        a = randint(10, 99)
        b = randint(2, 9)
        c = randint(10, 99)
        self.answer = str(a * b + c)
        text = "Сколько будет (" + str(a) + " x " + str(b) + ") + " + str(c) + "?"

        self.time_begin = time()
        self.info = Label(self.wndw, text=text)
        self.input = Entry(self.wndw)
        self.time = Label(self.wndw)

        self.train()

    def train(self):
        self.info.pack()
        self.input.pack()
        self.time.pack()

        while True:
            if self.input.get() == self.answer:
                break
            info = str(int(time() - self.time_begin))
            self.time['text'] = "Прошло " + info + " сек"
            self.wndw.update()

        self.info.pack_forget()
        self.input.pack_forget()
        self.time.pack_forget()

        self.info['text'] = "Вы решили пример за " + info + " сек"
        self.info.pack()
        self.back_to_menu.pack()

    def train_to_menu(self):
        self.info.destroy()
        self.back_to_menu.destroy()
        self.menu()


main = Main()

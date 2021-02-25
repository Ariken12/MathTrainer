import random as rand
import tkinter as tk

class Menu(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.answer = ''
        self.difficult = 0
        self.back = kwargs['back']
        self.info = tk.Label(self, text="Выберите уровень тренbровки")
        self.dif1 = tk.Button(self, text="1 уровень", command=(self.difficult_choose, 1))
        self.dif2 = tk.Button(self, text="2 уровень", command=(self.difficult_choose, 2))
        self.dif3 = tk.Button(self, text="3 уровень", command=(self.difficult_choose, 3))
        self.dif4 = tk.Button(self, text="4 уровень", command=(self.difficult_choose, 4))
        self.dif5 = tk.Button(self, text="5 уровень", command=(self.difficult_choose, 5))
        
        self.info.grid()
        self.dif2.grid()
        self.dif3.grid()
        self.dif1.grid()
        self.dif4.grid()
        self.dif5.grid()
    
    def difficult_choose(self, difficult):
        if difficult == '1':
            a = rand.randint(1, 10)
            b = rand.randint(1, 10)
            answer = str(a + b)
            text = "Сколько будет " + str(a) + " + " + str(b) + "?"
        elif difficult == '2':
            a = rand.randint(1, 10)
            b = rand.randint(1, 10)
            answer = str(a * b)
            text = "Сколько будет " + str(a) + " x " + str(b) + "?"
        elif difficult == '3':
            a = rand.randint(10, 99)
            b = rand.randint(10, 99)
            answer = str(a + b)
            text = "Сколько будет " + str(a) + " + " + str(b) + "?"
        elif difficult == '4':
            a = rand.randint(10, 99)
            b = rand.randint(2, 9)
            answer = str(a * b)
            text = "Сколько будет " + str(a) + " x " + str(b) + "?"
        elif difficult == '5':
            a = rand.randint(10, 99)
            b = rand.randint(2, 9)
            c = rand.randint(10, 99)
            answer = str(a * b + c)
            text = "Сколько будет (" + str(a) + " x " + str(b) + ") + " + str(c) + "?"
        self.back(text, answer)
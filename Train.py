import tkinter.tix as tk
import time
import re

class Task(tk.Frame):
    def __init__(self, task, answer, output):
        super().__init__()
        
        self.begin = time.time()
        self.count = 0
        self.filter = self.register(lambda x: re.fullmatch('(\d+)?'), x)

        self.label = tk.Label(self, text=task)
        self.input_for_answer = tk.Entry(self)
        self.time = tk.Label(self, text='Времени прошло 0 сек')
        self.back_to_menu = output

    def read_answer(self):
        pass
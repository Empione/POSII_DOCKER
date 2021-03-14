# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.filedialog as fd
import os
import shutil
import socket

path_main = '/home/endis/PycharmProjects/posii_2/Compose/total_dir/'

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        btn_file = tk.Button(self, text="Выбрать файл",
                             command=self.choose_file)
        btn_file.pack(padx=60, pady=10)

    def choose_file(self):
        filetypes = (("Изображение", "*.jpg *.gif *.png"),
                     ("Любой", "*"),
                     ("Текстовый файл", "*.txt"))
        p_file = fd.askopenfilename(title="Открыть файл", initialdir="./Example/",
                                      filetypes=filetypes)
        if p_file:
            name = os.path.basename(p_file)
            shutil.copy(p_file, path_main)
            sock = socket.socket()
            sock.connect(('localhost', 9090))
            sock.send((path_main+name).encode())
            #data = sock.recv(1024).decode()
            #sock.close()
            #print (data)
            
if __name__ == "__main__":
    app = App()
    app.mainloop()

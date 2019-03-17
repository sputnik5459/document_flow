#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.19
#  in conjunction with Tcl version 8.6
#    Jan 20, 2019 06:03:20 PM +03  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import auth_GUI_support, work_with_db, tkinter.messagebox, dir_GUI, secr_GUI

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    auth_GUI_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    auth_GUI_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:

    def log_in(self):
        log = self.Entry1.get()
        pwd = self.Entry2.get()
        if (log and pwd):
            login = work_with_db.db.db_log(log, pwd)
            if (login):
                self.topp.destroy()
                if (login[0]['login'] == "dir"):
                    dir_GUI.vp_start_gui()
                elif (login[0]['login'] == "secr"):
                    secr_GUI.vp_start_gui()
            else:
                self.Entry2.delete(0, tk.END)
                tkinter.messagebox.showinfo("Ошибка", "Введен неверный логин или пароль.") 
        else:
            tkinter.messagebox.showinfo("Ошибка", "Одно из полей осталось пустым.")

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#ececec' # Closest X11 color: 'gray92' 
        self.topp = top
        top.geometry("557x385+650+150")
        top.title("Электроналадка")
        top.configure(background="#dbffec")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.431, rely=0.052, height=21, width=77)
        self.Label1.configure(background="#dbffec")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Авторизация''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.431, rely=0.26,height=20, relwidth=0.294)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.251, rely=0.26, height=21, width=88)
        self.Label2.configure(background="#dbffec")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Введите логин:''')

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.431, rely=0.364,height=20, relwidth=0.294)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(show="*")

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.233, rely=0.364, height=21, width=95)
        self.Label3.configure(background="#dbffec")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Введите пароль:''')

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.413, rely=0.494, height=24, width=94)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Войти''')
        self.Button1.configure(width=94)
        self.Button1.configure(command=self.log_in)

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.413, rely=0.597, height=24, width=95)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Выход''')
        self.Button2.configure(width=95)
        self.Button2.configure(command=exit)

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

if __name__ == '__main__':
    vp_start_gui()






import tkinter as tk
from tkinter import messagebox as mg
class Validation(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("sum & sub")
        self.geometry("250x180")
        self.configure(background="#9E9E9D")
        self.resizable(width=False,height=False)
        self.controller()
        self.center(self)

    def center(self, win):
        win.update_idletasks()
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        win.deiconify()
    def controller(self):
        self.enter = tk.StringVar()
        tk.Entry(self,textvariable=self.enter).pack(padx=3,pady=3,ipadx=3,ipady=3)

        self.btn = tk.Button(self,text="validation",command=self.valid,background="#ACACAB",activebackground="#9E9E9D")
        self.btn.pack(padx=3,pady=3,ipadx=3,ipady=3)
        self.bind('<Return>',lambda event: self.btn.invoke())

        self.result = tk.StringVar()
        tk.Label(self, textvariable=self.result,justify="center",background="#9E9E9D",foreground="#F3F3F3").pack(padx=3, pady=3, ipadx=3, ipady=3)

    def valid(self):
        chars = self.enter.get()
        open_parentheses = 0
        close_parentheses = 0
        for ch in chars:
            if ch == "(":
                open_parentheses += 1
            elif ch == ")":
                close_parentheses += 1
            else:
                mg.showinfo("error","please, just enter parentheses")
                break
        if open_parentheses == close_parentheses:
            self.result.set("valid")
        else:
            self.result.set("invalid")

if __name__ == "__main__":
    app = Validation()
    app.mainloop()
import tkinter as tk

class SumSub(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("sum & sub")
        self.geometry("250x180")
        self.configure(background="#CED7B6")
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

        tk.Button(self,text="calculate",command=self.calc,background="#DFE7CA",activebackground="#CED7B6").pack(padx=3,pady=3,ipadx=3,ipady=3)

        self.result = tk.IntVar()
        tk.Entry(self, textvariable=self.result,justify="center").pack(padx=3, pady=3, ipadx=3, ipady=3)

    def calc(self):
        pass

if __name__ == "__main__":
    app = SumSub()
    app.mainloop()
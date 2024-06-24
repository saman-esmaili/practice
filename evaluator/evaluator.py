import tkinter as tk

class Evaluator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("evaluator")
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

        self.btn = tk.Button(self,text="calculate",command=self.calc,background="#DFE7CA",activebackground="#CED7B6")
        self.btn.pack(padx=3,pady=3,ipadx=3,ipady=3)
        self.bind('<Return>',lambda event: self.btn.invoke())

        self.result = tk.StringVar()
        tk.Entry(self, textvariable=self.result,justify="center",state="readonly").pack(padx=3, pady=3, ipadx=3, ipady=3)

    def calc(self):
        string = self.enter.get()
        result = 0
        characters = ''
        operators = ''
        for i, ch in enumerate(string):
            if ch == "+" or ch == "-":
                if i != 0:
                    if operators == '-':
                        result -= float(characters)
                    else:
                        result += float(characters)
                operators = ch
                characters = ''
            else:
                characters += ch
                if i == len(string) - 1:
                    if operators == '-':
                        result -= float(characters)
                    else:
                        result += float(characters)
        self.result.set(str(result))
if __name__ == "__main__":
    app = Evaluator()
    app.mainloop()
import tkinter as tk

class Validation(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("200x200")
        self.resizable(width=False,height=False)
        self.configure(background="#57A49A")
        self.title("validation")
        self.parentheses = []
        self.operators = []
        self.parentheses_index=-1
        self.operators_index=-1
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
        frame = tk.Frame(background="#57A49A")
        frame.pack(anchor="center")
        self.phrase = tk.StringVar()
        tk.Entry(frame,textvariable=self.phrase).grid(row=0,column=0,padx=3,pady=3,ipadx=3,ipady=3)

        tk.Button(frame,text="validation",command=self.valid,background="#4FBBAE",activebackground="#57A49A").grid(row=1,column=0,padx=3,pady=3,ipadx=3,ipady=3)

        self.result = tk.StringVar()
        tk.Label(frame,textvariable=self.result,background="#57A49A").grid(row=2,column=0,padx=3,pady=3,ipadx=3,ipady=3)

    def push(self):
        phrase = self.phrase.get()
        if phrase[0] != '-':
            self.final_phrase = f"+{phrase}"
        else:
            self.final_phrase = phrase
        for phs in self.final_phrase:
            if phs == "(":
                self.parentheses.append(phs)
                self.parentheses_index += 1
            elif phs == "+" or phs == "-":
                self.operators.append(phs)
                self.operators_index += 1

    def pop(self):
        index = 0
        for phs in self.final_phrase:
            if phs == ")":
                if self.operators_index != -1:
                    self.operators_index = -2
                else:
                    if self.parentheses_index >= 0:
                        self.parentheses.pop()
                        self.parentheses_index -= 1
                    else:
                        self.parentheses_index = -2
            elif phs != "(" and phs != "+" and phs != "-":
                if self.operators_index >= 0:
                    self.operators.pop()
                    self.operators_index -= 1

    def valid(self):
        phrase = self.phrase.get()
        if phrase[0] == ")" or phrase[len(phrase)-1] == "(":
            self.result.set("invalid")
        else:
            self.push()
            self.pop()
            if self.parentheses_index == -1 and self.operators_index == -1:
                self.result.set("valid")
            else:
                self.result.set("invalid")


if __name__ == "__main__":
    app = Validation()
    app.mainloop()


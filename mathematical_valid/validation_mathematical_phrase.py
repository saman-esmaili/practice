import tkinter as tk

from mathematical_valid.stack import Stack


class Validation(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("200x200")
        self.resizable(width=False,height=False)
        self.configure(background="#57A49A")
        self.title("validation")
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

    def valid(self):
        self.parentheses = Stack()
        self.operators = Stack()
        phrase = self.phrase.get()
        if phrase[0] != '-' and phrase[0] != "+":
            self.final_phrase = f"+{phrase}"
        else:
            self.final_phrase = phrase
        if self.final_phrase[1] == ")" or self.final_phrase[len(self.final_phrase)-1] == "(":
            self.result.set("invalid")
            return
        for phs in self.final_phrase:
            if phs == "(":
                self.parentheses.push(phs)
            elif phs == "+" or phs == "-":
                self.operators.push(phs)
            elif phs == ")":
                if self.operators.is_empty():
                    if self.parentheses.has_item():
                        self.parentheses.remove()
                    else:
                        self.parentheses.top_index = -2
            else:
                if self.operators.has_item():
                    self.operators.remove()
                else:
                    self.operators.top_index = -2
        if self.operators.is_empty() and self.parentheses.is_empty():
            self.result.set("valid")
        else:
            self.result.set("invalid")


if __name__ == "__main__":
    app = Validation()
    app.mainloop()
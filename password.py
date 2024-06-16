import string
import tkinter as tk
import random


class PasswordGenerator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("380x250")
        self.resizable(width=False, height=False)
        self.title("password generator")
        self.configure(background="#34495E")
        self.center(self)
        self.controller()
        self.generate()
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
        tk.Label(self, background="#34495E", fg="#EDE3F6", text="choose number of characters for your password").grid(
            row=0, column=1, padx=3, pady=3, ipadx=3, ipady=3)
        self.numbers = tk.IntVar()
        self.numbers.get()
        self.option3 = tk.Radiobutton(self, text="3", background="#34495E", fg="#EDE3F6", variable=self.numbers,
                                      value=1, selectcolor="#34495E",activebackground="#34495E")
        self.option5 = tk.Radiobutton(self, text="5", background="#34495E", fg="#EDE3F6", variable=self.numbers,
                                      value=2, selectcolor="#34495E",activebackground="#34495E")
        self.option14 = tk.Radiobutton(self, text="14", background="#34495E", fg="#EDE3F6", variable=self.numbers,
                                       value=3, selectcolor="#34495E",activebackground="#34495E")
        self.option3.grid(row=1, column=2, padx=3, pady=3, ipadx=3, ipady=3)
        self.option5.grid(row=1, column=1, padx=3, pady=3, ipadx=3, ipady=3)
        self.option14.grid(row=1, column=0, padx=3, pady=3, ipadx=3, ipady=3)

        tk.Button(self, text="Generate", command=self.show, background="#9585A3", fg="#1C0532",activebackground="#34495E").grid(row=2, column=1,
                                                                                                     padx=3, pady=3,
                                                                                                     ipadx=3, ipady=3)
        self.result = tk.StringVar()
        tk.Entry(self, textvariable=self.result, justify="center", state="readonly").grid(row=3, column=1, padx=3,
                                                                                          pady=15, ipadx=3, ipady=3)
        tk.Button(self,text="copy",command=self.copy, background="#9585A3", fg="#1C0532",activebackground="#34495E").grid(row=4, column=1, padx=3,pady=3, ipadx=3, ipady=3)
    def generate(self):
        lists = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z'
            , 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                 'V', 'W', 'X', 'Y', 'Z'
            , '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.pass_list = []
        word = ''
        for i in range(0,62):
            word += lists[i]
            for i2 in range(0,62):
                word = word[0:1]
                word += lists[i2]
                for i3 in range(0,62):
                    word += lists[i3]
                    self.pass_list.append(word)
                    word = word[0:2]
            word = ''
        print(len(self.pass_list))

    def show(self):
        chosen = self.numbers.get()
        if chosen == 1:
            index = random.randint(0,len(self.pass_list))
            self.result.set(self.pass_list[index])

    def copy(self):
        value = self.result.get()
        self.clipboard_clear()
        self.clipboard_append(value)

if __name__ == "__main__":
    app = PasswordGenerator()
    app.mainloop()
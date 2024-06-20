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
        chars = string.ascii_lowercase+string.ascii_uppercase+string.digits
        self.pass_list3 = [ch+ch1+ch2 for ch in chars for ch1 in chars for ch2 in chars]

        # self.pass_list5 = [ch1+ch2+ch3+ch4+ch5 for ch1 in chars for ch2 in chars for ch3 in chars for ch4 in chars for ch5 in chars]
        #
        # self.pass_list14 = [ch1+ch2+ch3+ch4+ch5+ch6+ch7+ch8+ch9+ch10+ch11+ch12+ch13+ch14 for ch1 in chars
        #                     for ch2 in chars for ch3 in chars for ch4 in chars for ch5 in chars for ch6 in chars
        #                     for ch7 in chars for ch8 in chars for ch9 in chars for ch10 in chars
        #                     for ch11 in chars for ch12 in chars for ch13 in chars for ch14 in chars]

    def show(self):
        self.generate()
        chosen = self.numbers.get()
        if chosen == 1:
            index = random.randint(0,len(self.pass_list3))
            self.result.set(self.pass_list3[index])

    def copy(self):
        value = self.result.get()
        self.clipboard_clear()
        self.clipboard_append(value)

if __name__ == "__main__":
    app = PasswordGenerator()
    app.mainloop()
import tkinter as tk
import string
class Alexander(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Alexander's code")
        self.geometry("300x200")
        self.configure(background="#FA9835")
        self.resizable(width=False,height=False)
        self.controller()
        self.center(self)

    def center(self,win):
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
        self.code = tk.StringVar()
        tk.Entry(self,textvariable=self.code).grid(row=0,column=1,padx=3,pady=3,ipadx=3,ipady=3)

        self.radioButton = tk.IntVar()
        self.radioButton.get()
        tk.Radiobutton(self,variable=self.radioButton,value=1,text="encoder",background="#FA9835",activebackground="#FA9835").grid(row=1,column=0,padx=3,pady=3,ipadx=3,ipady=3)
        tk.Radiobutton(self,variable=self.radioButton,value=2,text="decoder",background="#FA9835",activebackground="#FA9835").grid(row=1,column=2,padx=3,pady=3,ipadx=3,ipady=3)

        btn = tk.Button(self,command=self.show,text="Show",background="#F6B675")
        btn.grid(row=2,column=1,padx=3,pady=3,ipadx=3,ipady=3)

        self.result = tk.StringVar()
        tk.Label(self, textvariable=self.result,background="#FA9835",foreground="#3B230B").grid(row=3, column=1,padx=3,pady=3,ipadx=3,ipady=3)

    def show(self):
        codes = self.code.get()
        codes = codes.lower()
        result = ''
        chars = string.ascii_lowercase
        if self.radioButton.get() == 1:
            for code in codes:
                for i in range(len(chars)):
                    if code == chars[i]:
                        if i == len(chars) - 1:
                            result += chars[0]
                        else:
                            result += chars[i+1]
                        break
        elif self.radioButton.get() == 2:
            for code1 in codes:
                for index in range(len(chars)):
                    if code1 == chars[index]:
                        result += chars[index-1]
                        break
        self.result.set(result)


if __name__ == "__main__":
    app = Alexander()
    app.mainloop()
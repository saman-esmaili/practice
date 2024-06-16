import string
import tkinter as tk

lowercase = [string.ascii_lowercase]
uppercase = [string.ascii_uppercase]

class PasswordGenerator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("380x250")
        self.resizable(width=False,height=False)
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
        # mainFrame = tk.Frame(self,background="#34495E")
        # mainFrame.pack(side="top",anchor="e")
        tk.Label(self,background="#34495E",fg="#EDE3F6",text="choose number of characters for your password").grid(row=0,column=1,padx=3,pady=3,ipadx=3,ipady=3)
        self.numbers = tk.IntVar()
        self.numbers.get()
        self.radio1 = tk.Radiobutton(self,text="3",background="#34495E",fg="#EDE3F6",variable=self.numbers,value="1",selectcolor="#34495E")
        self.radio2 = tk.Radiobutton(self,text="5",background="#34495E",fg="#EDE3F6",variable=self.numbers,value="2",selectcolor="#34495E")
        self.radio3 = tk.Radiobutton(self,text="14",background="#34495E",fg="#EDE3F6",variable=self.numbers,value="3",selectcolor="#34495E")
        self.radio1.grid(row=1,column=2,padx=3,pady=3,ipadx=3,ipady=3)
        self.radio2.grid(row=1,column=1,padx=3,pady=3,ipadx=3,ipady=3)
        self.radio3.grid(row=1,column=0,padx=3,pady=3,ipadx=3,ipady=3)
        tk.Button(self,text="Generate",command=self.show,background="#9585A3",fg="#1C0532").grid(row=2,column=1,padx=3,pady=3,ipadx=3,ipady=3)
        self.result = tk.StringVar()
        tk.Entry(self,textvariable=self.result,justify="center",state="readonly").grid(row=3,column=1,padx=3,pady=15,ipadx=3,ipady=3)
    def generate(self):
        pass

    def show(self):
        pass

if __name__ == "__main__":
    app = PasswordGenerator()
    app.mainloop()
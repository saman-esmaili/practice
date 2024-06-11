import tkinter as tk

class Order(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x500")
        self.title("order")
        self.configure(background="#8CFFEC")
        self.center(self)
        self.controller()
        self.labels = []
        self.rowFrame = None

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
        topFrame = tk.Frame(self,background="#8CFFEC")
        topFrame.pack(side='top')
        tk.Label(topFrame,text="Row Numbers:",background="#8CFFEC").grid(row=0,column=0,padx=3,pady=3,ipadx=3,ipady=3)
        self.row = tk.IntVar()
        tk.Entry(topFrame,textvariable=self.row).grid(row=0,column=1,padx=3,pady=3,ipadx=3,ipady=3)
        tk.Button(topFrame,text="Run",command=self.make_order,background="#BAECE4").grid(row=0,column=2,padx=3,pady=3,ipadx=3,ipady=3)
        tk.Button(topFrame,text="order",command=self.make_order2,background="#BAECE4").grid(row=0,column=3,padx=3,pady=3,ipadx=3,ipady=3)
        tk.Button(topFrame,text="order2",command=self.make_order3,background="#BAECE4").grid(row=0,column=4,padx=3,pady=3,ipadx=3,ipady=3)

    def clean(self):
        if self.rowFrame:
            self.rowFrame.destroy()
            self.rowFrame = None
            self.labels.clear()

    def make_order(self):
        self.clean()
        row = self.row.get()
        self.rowFrame = tk.Frame(self,background="#8CFFEC")
        self.rowFrame.pack(side='top',anchor='w')
        for i in range(1, row+1):
            for ind in range(1,i+1):
                label = tk.Label(self.rowFrame, text=ind,background="#8CFFEC")
                label.grid(row=i, column=ind)
                self.labels.append(label)
        for index in range(row):
            self.rowFrame.grid_rowconfigure(index,weight=1)
            self.rowFrame.grid_columnconfigure(index,weight=1)
    def make_order2(self):
        self.clean()
        row = self.row.get()
        amount = 1
        self.rowFrame = tk.Frame(self, background="#8CFFEC")
        self.rowFrame.pack(side='top', anchor='e')
        for i in range(1,row + 1):
            col = 0
            for ind in range(amount, amount +i):
                label = tk.Label(self.rowFrame, text=ind, background="#8CFFEC")
                label.grid(row=i,column=row-col+1)
                self.labels.append(label)
                col += 1
            if i > 1:
                amount = ind +1
            else:
                amount = 2
        for index in range(row):
            self.rowFrame.grid_rowconfigure(index, weight=1)
            self.rowFrame.grid_columnconfigure(index, weight=1)

    def make_order3(self):
        self.clean()
        row = self.row.get()
        self.rowFrame = tk.Frame(self, background="#8CFFEC")
        self.rowFrame.pack(side='top', anchor='w')
        amount = 1
        amount_for1 = 1
        for i in range(amount_for1,row):
            col = 0
            for index in range(amount, amount+i):
                # if i < 3:
                tk.Label(self.rowFrame,background="#8CFFEC",text=2**(index-1)).grid(row=i,column=col)
                col +=1
            amount = index+1
            amount_for1 += 1

if __name__ == "__main__":
    app = Order()
    app.mainloop()
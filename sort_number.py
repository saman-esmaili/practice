import tkinter as tk

class SortApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x340")
        self.title("sort numbers")
        self.configure(background="#66F2F7")
        self.resizable(width=False, height=False)
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
        topFrame = tk.Frame(self,background="#66F2F7")
        topFrame.pack(side=tk.TOP)
        tk.Label(topFrame,text="from:",background="#66F2F7").grid(row=0,column=0,padx=3,pady=3,ipadx=3,ipady=3)
        self.fromEntry = tk.IntVar()
        tk.Entry(topFrame,textvariable=self.fromEntry).grid(row=0,column=1,padx=3,pady=3,ipadx=3,ipady=3)
        tk.Label(topFrame,text="to:",background="#66F2F7").grid(row=0,column=2,padx=3,pady=3,ipadx=3,ipady=3)
        self.toEntry = tk.IntVar()
        tk.Entry(topFrame, textvariable=self.toEntry).grid(row=0,column=3,padx=3,pady=3,ipadx=3,ipady=3)

        tk.Label(topFrame, text="count:",background="#66F2F7").grid(row=1, column=0, padx=3, pady=3, ipadx=3, ipady=3)
        self.count = tk.IntVar()
        tk.Entry(topFrame, textvariable=self.count).grid(row=1, column=1, padx=3, pady=3, ipadx=3, ipady=3)

        tk.Button(topFrame,text="Generate",background="#B9FAFC",command=self.generate).grid(row=1, column=3, padx=3, pady=3, ipadx=3, ipady=3)
        for i in range(7):
            topFrame.grid_columnconfigure(i,weight=1)
        topFrame.grid_rowconfigure(0,weight=1)
        topFrame.grid_rowconfigure(1,weight=1)

        listBoxFrame = tk.Frame(self,background="#66F2F7")
        listBoxFrame.pack(side=tk.LEFT, fill=tk.BOTH)
        self.listbox = tk.Listbox(listBoxFrame,height=12)
        self.listbox.grid(row=0, column=1, padx=3, pady=3, ipadx=3, ipady=3)

        scrollbar = tk.Scrollbar(listBoxFrame,orient=tk.VERTICAL, command=self.listbox.yview)
        scrollbar.grid(row=0, column=0, padx=3, pady=3, ipadx=3, ipady=3)
        self.listbox.config(yscrollcommand=scrollbar.set)
        listBoxFrame.grid_columnconfigure(0,weight=1)
        listBoxFrame.grid_columnconfigure(1,weight=1)
        listBoxFrame.grid_rowconfigure(0,weight=1)

        buttonFame = tk.Frame(self,background="#66F2F7")
        buttonFame.pack(side=tk.LEFT, fill=tk.X)
        tk.Button(buttonFame,text="Bubble",background="#B9FAFC",command=self.bubble_sort).grid(row=0,column=0, padx=3, pady=3, ipadx=3, ipady=3,sticky='nesw')
        tk.Button(buttonFame,text="insertion",background="#B9FAFC",command=self.insertion_sort).grid(row=1,column=0, padx=3, pady=3, ipadx=3, ipady=3,sticky='nesw')
        buttonFame.grid_rowconfigure(0,weight=1)
        buttonFame.grid_rowconfigure(1,weight=1)
        buttonFame.grid_columnconfigure(0,weight=1)

        listBoxFrame2 = tk.Frame(self,background="#66F2F7")
        listBoxFrame2.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.converted_list = tk.Listbox(listBoxFrame2, height=12)
        self.converted_list.grid(row=0, column=0, padx=3, pady=3, ipadx=3, ipady=3)

        scrollbar2 = tk.Scrollbar(listBoxFrame2, orient=tk.VERTICAL, command=self.converted_list.yview)
        scrollbar2.grid(row=0, column=1, padx=3, pady=3, ipadx=3, ipady=3)
        self.converted_list.config(yscrollcommand=scrollbar2.set)
        listBoxFrame2.grid_rowconfigure(0,weight=1)
        listBoxFrame2.grid_columnconfigure(0,weight=1)
        listBoxFrame2.grid_columnconfigure(1,weight=1)

    def generate(self):
        pass
    def bubble_sort(self):
        pass
    def insertion_sort(self):
        pass

if __name__ == "__main__":
    app = SortApp()
    app.mainloop()
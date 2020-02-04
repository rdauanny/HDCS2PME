from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pandastable import Table, TableModel
from functions import csv_export


class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()

        self.title("Hybrid DCS to Power Monitoring Expert")
        self.minsize(200, 200)
        self.wm_iconbitmap('icon.ico')
        self.iconbitmap('icon.ico')
        

        self.formFrame = ttk.LabelFrame(self, text = "PME Server")
        self.formFrame.grid(column = 0, row = 2, padx = 40, pady = 40)

        self.tableFrame = ttk.LabelFrame(self, text = "Data Base")
        self.tableFrame.grid(column = 0, row =3, padx = 20, pady = 20)

        self.Menu()
        entries = self.Form()
        self.buttonStore(entries)


    def buttonStore(self, entries):
        self.buttonSto = ttk.Button(self.formFrame, text = "Store",command = (lambda e=entries: self.StoreDB(e)))
        self.buttonOpe = ttk.Button(self.formFrame, text = "Open File",command = (lambda e=entries: self.opencsv()))
        self.buttonSto.pack(side= LEFT, padx = 5, pady = 5)
        self.buttonOpe.pack(side= LEFT, padx = 5, pady = 5)

    def opencsv(self):
        self.filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
        (("CSV Files","*.csv"),("All Files","*.*")) )
        df = csv_export(self.filename)
        self.PandasTable(df)

    def Menu(self):
        self.menu = Menu(self)
        self.config(menu=self.menu)
        self.filemenu = Menu(self.menu)
        self.menu.add_cascade(label='File', menu=self.filemenu)
        self.filemenu.add_command(label='New')
        self.filemenu.add_command(label='Open...', command= self.opencsv)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Exit', command=self.quit)
        self.helpmenu = Menu(self.menu)
        self.menu.add_cascade(label='Help', menu=self.helpmenu)
        self.helpmenu.add_command(label='About')

    def PandasTable(self, df):

        self.table = pt = Table(self.tableFrame, dataframe=df, showtoolbar=False, showstatusbar=False)
        pt.show()

    def Form(self):
        fields = ('Operation Server', 'Alias PLC')
        self.entries = {}
        for field in fields:
            self.row = ttk.Frame(self.formFrame)
            self.lab = ttk.Label(self.row, width=22, text=field + ": ", anchor='w')
            self.ent = ttk.Entry(self.row)
            self.ent.insert(0, '0')
            self.row.pack(side=TOP,  padx=5, pady=5)
            self.lab.pack(side=LEFT)
            self.ent.pack(side=RIGHT, expand=YES, fill=X)
            self.entries[field] = self.ent
        return(self.entries)

    def StoreDB(self, entries):
        for ent in entries:
           print(ent ,entries[ent].get())


root = Root()
root.mainloop()
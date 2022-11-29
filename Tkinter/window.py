from tkinter import *
import pandas as pd
from tkinter import ttk

df = pd.DataFrame({"currency":["EUR","XCD","ARS","CAD"],
                   "volumne":[400,500,600,700]})

class app(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Python Guides")

        self.tree = ttk.Treeview(self)
        columns = list(df.columns)
        self.Combo = ttk.Combobox(self, values=list(df["currency"].unique()),state="readonly")
        self.Combo.pack()
        self.Combo.bind("<<ComboboxSelected>>", self.select_currency)
        self.tree["columns"] = columns
        self.tree.pack(expand=TRUE, fill=BOTH)

        for i in columns:
            self.tree.column(i, anchor="w")
            self.tree.heading(i, text=i, anchor="w")

        for index, row in df.iterrows():
            self.tree.insert("", "end", text=index, values=list(row))

    def select_currency(self,event=None):
        self.tree.delete(*self.tree.get_children())
        for index, row in df.loc[df["currency"].eq(self.Combo.get())].iterrows():
            self.tree.insert("", "end", text=index, values=list(row))

ws = app()
ws.mainloop()


# import tkinter as tk
# from tkinter import ttk
#
# import figures as f
#
# window = tk.Tk()
# window.title('Графический редактор')
# window.geometry('1280x720')
#
# f.canvas = f.Canvas('-')
#
# a = ttk.Treeview()
# a['a'] = list({0: 1, 1: 2, 2: 3})
# a.pack(expand='True', fill='both')
#
# # figure_label_text = tk.StringVar()
# # figure_label_text.set('Канвас')
# # figure_label = tk.Button(textvariable=figure_label_text, font=('Courier New', 50))
# # figure_label.pack(side='top')
#
# window.mainloop()

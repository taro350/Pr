import requests
import pandas as pd
import tkinter as tk
from tkinter import filedialog


def save_file_csv(csv_from_internet):
    data = requests.get(csv_from_internet).text
    df = pd.read_csv(io.StringIO(data))

    root = tk.Tk()

    canvas1 = tk.Canvas(root, width=300, height=300)
    canvas1.pack()

    def func():
        global df 
        ex_path = filedialog.asksaveasfilename(defaultextension='.csv')
        df.to_csv(ex_path, index=False)
    
    Butt = tk.Button(text='Push', command=func)
    canvas1.create_window(100, 100, window=Butt)

    root.mainloop()


if '__init__' == '__main__()':
    save_file_csv(csv_from_internet)

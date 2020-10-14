from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory

# Tk().withdraw()
filename = askopenfilename()
print(filename)

folder = askdirectory()
print(folder)

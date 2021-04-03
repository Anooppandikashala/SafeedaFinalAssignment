import tkinter as tk

class MainWindow():
  def __init__(self):
    self.window = tk.Tk()

  def setupUi(self):
    label = tk.Label(text="Estate Management System")
    label.pack()
    self.window.mainloop()
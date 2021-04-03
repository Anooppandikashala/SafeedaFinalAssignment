import tkinter as tk
import main_window
import user

class LoginWindow():
  def __init__(self):
    self.window = tk.Tk()

  def handleLogin(self):
    print("hello")
    username = self.entryUsername.get()
    password = self.entryPassword.get()
    print(username)
    print(password)
    
    secondWindow = main_window.MainWindow();
    secondWindow.setupUi()
    self.window.distroy()
    

  def showLogin(self):
    labelUsername = tk.Label(text="Username :")
    labelUsername.pack()
    self.entryUsername = tk.Entry()
    self.entryUsername.pack()
    labelPassword = tk.Label(text="Password :")
    labelPassword.pack()
    self.entryPassword = tk.Entry()
    self.entryPassword.pack()
    self.btnLogin = tk.Button(text="Login", command = self.handleLogin)
    self.btnLogin.pack()

  def setupUi(self):
    label = tk.Label(text="Estate Management System")
    label.pack()
    self.showLogin()
    self.window.mainloop()

  
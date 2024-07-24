from tkinter import *
from tkinter import messagebox
parent=Tk()
parent.geometry("100x100")
messagebox.showerror("Error","Your System ran into some problem. Detecting issues..")
messagebox.showinfo("Information","You are a Dork")
messagebox.showwarning("Warning","Injecting Malware...")
messagebox.askquestion("Question","Are you an Adult?")
messagebox.askretrycancel("Retry Box","Give up or Retry ?")
parent.mainloop()
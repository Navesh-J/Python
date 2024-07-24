import tkinter
class myGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()
        self.canvas=tkinter.Canvas(self.main_window,width=400,height=400)
        self.canvas.create_line(0,0,399,399)
        self.canvas.create_line(0,399,399,0)
        self.canvas.create_rectangle(50,100,150,200)
        self.canvas.create_oval(200,150,100,50)
        self.canvas.create_text(300,300,text='Hello World')
        self.canvas.pack()
        tkinter.mainloop()
my_GUI=myGUI()
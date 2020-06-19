import tkinter as tk
from tkinter import *
from ttk import Button, Style
from PIL import ImageTk, Image
import os
import astarf
import bfs
import dfs
import djikstra
import dynamic

TITLE_FONT = ("Helvetica", 18, "bold")


class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

            frame.configure(bg="#a1dbcd")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')


        self.instr1 = Label(self, bg='gray12', fg="white", width=125, justify=RIGHT, height=6, text="AGENT PERCEPT")
        self.instr1.configure(font=("Times New Roman", 14, "bold"))
        self.instr1.grid(row=0, column=1, columnspan=4, sticky=W + E)



        self.pack(fill=BOTH, expand=True)

        '''self.text1 = Text(self, width=50, height=2)
        self.text1.grid(row=4, column=3, sticky=W)
        self.text1.insert(0.0, "insert your statement here")'''

        self.rowconfigure(2, pad=15)

        self.rowconfigure(4, pad=15)
        self.rowconfigure(8, pad=15)
        self.rowconfigure(6, pad=15)
        self.rowconfigure(10, pad=25)
        self.rowconfigure(20, pad=25)

        self.obtn = Button(self, text="BREADTH SEARCH", command=self.contains2)
        self.obtn.grid(row=2, column=2, columnspan=3, sticky=W)

        self.obtn = Button(self, text="LEVEL SEARCH", command=self.contains2)
        self.obtn.grid(row=2, column=3, columnspan=3, sticky=W)

        self.obtn = Button(self, text="DEAPTH ", command=self.contains3)
        self.obtn.grid(row=4, column=2, columnspan=3, sticky=W)

        self.obtn = Button(self, text="FINITE GRAPH", command=self.contains3)
        self.obtn.grid(row=4, column=3, columnspan=3, sticky=W)

        self.obtn = Button(self, text="ONLY PATH LENGTH", command=self.contains4)
        self.obtn.grid(row=6, column=2, columnspan=3, sticky=W)

        self.obtn = Button(self, text="UNIIFORM COST", command=self.contains4)
        self.obtn.grid(row=6, column=3, columnspan=3, sticky=W)

        self.obtn = Button(self, text="PATH LENGTH AND HEURISTIC VALUE", command=self.contains1)
        self.obtn.grid(row=8, column=2, columnspan=3, sticky=W)

        self.obtn = Button(self, text="BEST PATH", command=self.contains1)
        self.obtn.grid(row=8, column=3, columnspan=3, sticky=W)

        self.obtn = Button(self, text="USER INPUT", command=self.contains5)
        self.obtn.grid(row=20, column=4, columnspan=4, sticky=W)

        self.pack()

    def contains2(self):

        # print(input)

                self.controller.show_frame("PageTwo")
                return

    def contains3(self):

        # print(input)

        self.controller.show_frame("PageThree")
        return

    def contains4(self):

            # print(input)

        self.controller.show_frame("PageFour")
        return

    def contains1(self):
                # print(input)

        self.controller.show_frame("PageOne")
        return

    def contains5(self):
        dynamic.start()
        return


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')

        self.columnconfigure(5, pad=5)
        '''''
        self.columnconfigure(1, pad=5)
        self.columnconfigure(2, pad=5)
        self.columnconfigure(3, pad=5)
        self.columnconfigure(4, pad=5)
          self.rowconfigure(0, pad=15)
        self.rowconfigure(1, pad=15)
        self.rowconfigure(2, pad=15)
        self.rowconfigure(3, pad=15)
        self.rowconfigure(4, pad=15)
        self.rowconfigure(18, pad=15)
        self.rowconfigure(46, pad=15)""""""
        '''
        imagehead = Image.open("astar.png")
        tkimage = ImageTk.PhotoImage(imagehead)
        self.tkimage = tkimage
        panel1 = Label(self, image=tkimage, width=600, height=500)
        panel1.grid(row=10, column=0, sticky=E)
        # for two big textboxes

        self.tb8 = Text(self, width=55, height=8, font=("Helvetica", 11), wrap=WORD)
        self.tb8.grid(row=10, column=20, columnspan=2, sticky=W)

        # forsmall two textboxes
        self.tb1 = Text(self, width=30, height=5)
        self.tb1.grid(row=0, column=0, sticky=W)
        self.tb1.insert(0.0, "insert start state")
        self.tb2 = Text(self, width=30, height=5)
        self.tb2.insert(0.0, "insert goal state")
        self.tb2.grid(row=0, column=1, sticky=W)

        # buttons
        self.hbtn = Button(self, text="BACK", command=lambda: controller.show_frame("StartPage"))
        self.hbtn.grid(row=1, column=0, columnspan=2, sticky=W)

        self.obtn = Button(self, text="SUBMIT", command=lambda: self.info())
        self.obtn.grid(row=1, column=1, columnspan=2, sticky=W)

    def info(self):
        # print(val)
        point1 = self.tb1.get("1.0", "end-1c")
        point2 = self.tb2.get("1.0", "end-1c")
        point1 = point1.split()
        point2 = point2.split()
        x1 = int(point1[0])
        y1 = int(point1[1])

        x2 = int(point2[0])
        y2 = int(point2[1])
        s = astarf.start(x1, y1, x2, y2)
        x = "start"
        for i in s:
            x = x + "-->" + str(i)
        self.tb8.configure(state=NORMAL)

        self.tb8.delete(1.0, END)

        self.tb8.insert(0.0, x)

        self.tb8.configure(state=DISABLED)


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')

        self.columnconfigure(5, pad=5)
        '''''
        self.columnconfigure(1, pad=5)
        self.columnconfigure(2, pad=5)
        self.columnconfigure(3, pad=5)
        self.columnconfigure(4, pad=5)
          self.rowconfigure(0, pad=15)
        self.rowconfigure(1, pad=15)
        self.rowconfigure(2, pad=15)
        self.rowconfigure(3, pad=15)
        self.rowconfigure(4, pad=15)
        self.rowconfigure(18, pad=15)
        self.rowconfigure(46, pad=15)""""""
        '''
        imagehead = Image.open("bfs_dfs.png")
        tkimage = ImageTk.PhotoImage(imagehead)
        self.tkimage = tkimage
        panel1 = Label(self, image=tkimage, width=650, height=500)
        panel1.grid(row=10, column=0, sticky=E)
        # for two big textboxes

        self.tb8 = Text(self, width=55, height=8, font=("Helvetica", 11), wrap=WORD)
        self.tb8.grid(row=10, column=20, columnspan=2, sticky=W)

        # forsmall two textboxes
        self.tb1 = Text(self, width=30, height=5)
        self.tb1.grid(row=0, column=0, sticky=W)
        self.tb1.insert(0.0, "insert goal state assuming start node is 0")
        # self.tb2 = Text(self, width=30, height=5)
        # self.tb2.insert(0.0, "insert goal state")
        # self.tb2.grid(row=0, column=1, sticky=W)

        # buttons
        self.hbtn = Button(self, text="BACK", command=lambda: controller.show_frame("StartPage"))
        self.hbtn.grid(row=1, column=0, columnspan=2, sticky=W)

        self.obtn = Button(self, text="SUBMIT", command=lambda: self.info())
        self.obtn.grid(row=1, column=1, columnspan=2, sticky=W)

    def info(self):
        # print(val)
        point1 = self.tb1.get("1.0", "end-1c")

        point1 = int(point1)
        x = bfs.start(point1)

        self.tb8.configure(state=NORMAL)

        self.tb8.delete(1.0, END)

        self.tb8.insert(0.0, x)

        self.tb8.configure(state=DISABLED)


class PageThree(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')

        self.columnconfigure(5, pad=5)
        '''''
        self.columnconfigure(1, pad=5)
        self.columnconfigure(2, pad=5)
        self.columnconfigure(3, pad=5)
        self.columnconfigure(4, pad=5)
          self.rowconfigure(0, pad=15)
        self.rowconfigure(1, pad=15)
        self.rowconfigure(2, pad=15)
        self.rowconfigure(3, pad=15)
        self.rowconfigure(4, pad=15)
        self.rowconfigure(18, pad=15)
        self.rowconfigure(46, pad=15)""""""
        '''
        imagehead = Image.open("bfs_dfs.png")
        tkimage = ImageTk.PhotoImage(imagehead)
        self.tkimage = tkimage
        panel1 = Label(self, image=tkimage, width=650, height=500)
        panel1.grid(row=10, column=0, sticky=E)
        # for two big textboxes

        self.tb8 = Text(self, width=55, height=8, font=("Helvetica", 11), wrap=WORD)
        self.tb8.grid(row=10, column=20, columnspan=2, sticky=W)

        # forsmall two textboxes
        self.tb1 = Text(self, width=30, height=5)
        self.tb1.grid(row=0, column=0, sticky=W)
        self.tb1.insert(0.0, "insert goal state assuming start node is 0")
        # self.tb2 = Text(self, width=30, height=5)
        # self.tb2.insert(0.0, "insert goal state")
        # self.tb2.grid(row=0, column=1, sticky=W)

        # buttons
        self.hbtn = Button(self, text="BACK", command=lambda: controller.show_frame("StartPage"))
        self.hbtn.grid(row=1, column=0, columnspan=2, sticky=W)

        self.obtn = Button(self, text="SUBMIT", command=lambda: self.info())
        self.obtn.grid(row=1, column=1, columnspan=2, sticky=W)

    def info(self):
        # print(val)
        point1 = self.tb1.get("1.0", "end-1c")

        point1 = int(point1)
        x = dfs.start(point1)

        self.tb8.configure(state=NORMAL)

        self.tb8.delete(1.0, END)

        self.tb8.insert(0.0, x)

        self.tb8.configure(state=DISABLED)


class PageFour(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')

        self.columnconfigure(5, pad=5)
        '''''
        self.columnconfigure(1, pad=5)
        self.columnconfigure(2, pad=5)
        self.columnconfigure(3, pad=5)
        self.columnconfigure(4, pad=5)
          self.rowconfigure(0, pad=15)
        self.rowconfigure(1, pad=15)
        self.rowconfigure(2, pad=15)
        self.rowconfigure(3, pad=15)
        self.rowconfigure(4, pad=15)
        self.rowconfigure(18, pad=15)
        self.rowconfigure(46, pad=15)""""""
        '''
        imagehead = Image.open("ucs.png")
        tkimage = ImageTk.PhotoImage(imagehead)
        self.tkimage = tkimage
        panel1 = Label(self, image=tkimage, width=600, height=500)
        panel1.grid(row=10, column=0, sticky=E)
        # for two big textboxes

        self.tb8 = Text(self, width=55, height=8, font=("Helvetica", 11), wrap=WORD)
        self.tb8.grid(row=10, column=20, columnspan=2, sticky=W)

        # forsmall two textboxes
        self.tb1 = Text(self, width=30, height=5)
        self.tb1.grid(row=0, column=0, sticky=W)
        self.tb1.insert(0.0, "insert start state")
        self.tb2 = Text(self, width=30, height=5)
        self.tb2.insert(0.0, "insert goal state")
        self.tb2.grid(row=0, column=1, sticky=W)

        # buttons
        self.hbtn = Button(self, text="BACK", command=lambda: controller.show_frame("StartPage"))
        self.hbtn.grid(row=1, column=0, columnspan=2, sticky=W)

        self.obtn = Button(self, text="SUBMIT", command=lambda: self.info())
        self.obtn.grid(row=1, column=1, columnspan=2, sticky=W)

    def info(self):
        # print(val)

        self.tb8.configure(state=NORMAL)
        self.tb8.delete(1.0, END)
        point1 = self.tb1.get("1.0", "end-1c")
        point2 = self.tb2.get("1.0", "end-1c")
        x = int(point1)
        y = int(point2)
        a = djikstra.start(x, y)
        self.tb8.insert(0.0, a)
        self.tb8.configure(state=DISABLED)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
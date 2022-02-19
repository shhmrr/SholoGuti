
import PageOne
from PageOne import *
try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2
from PageOne import Page1
from PIL import ImageTk, Image





class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, SixteenGutiPage, TwelveGutiPage,SixteenGuti_OneVOnePage,SixteenGuti_OneVAIPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.img = ImageTk.PhotoImage(Image.open("woodtexture1.gif"))  # PIL solution
        background_label = tk.Label(self, image=self.img)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        button1 = tk.Button(self, text="Play 16 Guti",
                            command=lambda: controller.show_frame("SixteenGutiPage"),height=3,width=20)
        button2 = tk.Button(self, text="Play 12 Guti",
                            command=lambda: controller.show_frame("TwelveGutiPage"),height=3,width=20)
        button1.place(relx = 0.5, rely = 0.25, anchor = "center")
        button2.place(relx = 0.5, rely = 0.5, anchor = "center")

class SixteenGutiPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        ##background
        self.img = ImageTk.PhotoImage(Image.open("woodtexture1.gif"))  # PIL solution
        background_label = tk.Label(self, image=self.img)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        buttonMenu = tk.Button(self, text="Back to Menu",
                           command=lambda: controller.show_frame("StartPage"),height=2,width=10)
        buttonOneVOne = tk.Button(self, text="Play 1Vs1",
                               command=lambda: controller.show_frame("SixteenGuti_OneVOnePage"),height=3,width=20)
        buttonOneVAI = tk.Button(self, text="Play Against Computer",
                                  command=lambda: controller.show_frame("SixteenGuti_OneVAIPage"),height=3,width=20)
        buttonOneVOne.place(relx=0.25, rely=0.5, anchor="center")
        buttonOneVAI.place(relx=0.75, rely=0.5, anchor="center")
        buttonMenu.place(relx=0.5, rely=0.65, anchor="center")

def Drawing16GutiBoard(canvas,canvasWidth,canvasHeight):
    w = canvasWidth
    h = canvasHeight
    ##horizontal lines
    canvas.create_line(0,   0,   w,   0,   fill='black', width=3)
    canvas.create_line(w/4,   h/8, 3*w/4,   h/8, fill='black', width=3)
    canvas.create_line(0, 2*h/8, w, 2*h/8, fill='black', width=3)
    canvas.create_line(0, 3*h/8, w, 3*h/8, fill='black', width=3)
    canvas.create_line(0, 4*h/8, w, 4*h/8, fill='black', width=3)
    canvas.create_line(0, 5*h/8, w, 5*h/8, fill='black', width=3)
    canvas.create_line(0, 6*h/8, w, 6*h/8, fill='black', width=3)
    canvas.create_line(w/4, 7*h/8, 3*w/4, 7*h/8, fill='black', width=3)
    canvas.create_line(0,   h,   w,   h,   fill='black', width=3)
    ##vertical lines
    canvas.create_line(0, 2 * h / 8, 0, 6 * h / 8, fill='black', width=3)
    canvas.create_line(w/4, 2 * h / 8, w/4, 6 * h / 8, fill='black', width=3)
    canvas.create_line(2*w/4, 0, 2*w/4, h , fill='black', width=3)
    canvas.create_line(3*w/4, 2 * h / 8, 3*w/4, 6 * h / 8, fill='black', width=3)
    canvas.create_line(w, 2 * h / 8, w, 6 * h / 8, fill='black', width=3)
    ##Diagonals top and bottom
    canvas.create_line(0, 0, 2*w/4, 2*h/8, fill='black', width=3)
    canvas.create_line(w, 0, 2 * w / 4, 2 * h / 8, fill='black', width=3)
    canvas.create_line(0, h, 2*w/4, 6*h/8, fill='black', width=3)
    canvas.create_line(w, h, 2*w/4,6*h/8, fill='black', width=3)
    ##Diagonals in the middle
    #up-left to bottom-right
    canvas.create_line(0, 2*h/8, w , 6 * h / 8, fill='black', width=3)
    canvas.create_line(2*w/4, 2 * h / 8, w, 4 * h / 8, fill='black', width=3)
    canvas.create_line(0, 4 * h / 8, 2*w/4, 6 * h / 8, fill='black', width=3)
    ##bottom-left to up-right
    canvas.create_line(0, 4 * h / 8, 2*w/4, 2 * h / 8, fill='black', width=3)
    canvas.create_line(0, 6 * h / 8, w, 2 * h / 8, fill='black', width=3)
    canvas.create_line(2*w/4, 6 * h / 8, w, 4 * h / 8, fill='black', width=3)

def FillingArray16GutiBoard():
    #the 16guti game is played in a 9 by 5 board. row = 9 col = 5
    #red = 2
    #green = 1
    #blank = 0
    #spaces in the board or not a move for the coin = -1 the board is not entirely a square

    arr = []
    arr.append([1,-1,1,-1,1])
    arr.append([-1,1,1,1,-1])
    arr.append([1,1,1,1,1])
    arr.append([1,1,1,1,1])
    arr.append([0,0,0,0,0])
    arr.append([2,2,2,2,2])
    arr.append([2,2,2,2,2])
    arr.append([-1,2,2,2,-1])
    arr.append([2,-1,2,-1,2])
    return arr
def Drawing16GutiBoardRedBluePlayers(canvas,canvasWidth,canvasHeight,arr,redGuti,blueGuti):
    redguti = []
    greenguti = []
    for i in range(9):
        temp = []
        for j in range(5):
            temp.append(0)
        redguti.append(temp)
        greenguti.append(temp)

    for i in range(9):
        for j in range(5):
            if arr[i][j] == 1:
                greenguti1 = canvas.create_image(j * canvasWidth / 4, i * canvasHeight / 8, image=blueGuti)
                greenguti[i][j] = greenguti1
            if arr[i][j] == 2:
                redguti1 = canvas.create_image(j * canvasWidth / 4, i * canvasHeight / 8, image=redGuti)
                redguti[i][j] = redguti1
    return redguti,greenguti


class SixteenGuti_OneVOnePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        ##background
        self.img = ImageTk.PhotoImage(Image.open("woodtexture1.gif"))  # PIL solution
        background_label = tk.Label(self, image=self.img)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        buttonMenu = tk.Button(self, text="Back",
                               command=lambda: controller.show_frame("SixteenGutiPage"),height=2,width=10)
        buttonMenu.place(relx=0.90, rely=0.90, anchor="center")
        self.canvasWidth = 300
        self.canvasHeight = 500
        canvas = tk.Canvas(self,width=self.canvasWidth,height=self.canvasHeight)
        self.canvas_bg = ImageTk.PhotoImage(file="woodtexture1.gif")
        canvas.create_image(10, 10, image=self.canvas_bg)
        canvas.place(relx=0.50, rely=0.50, anchor="center")

        Drawing16GutiBoard(canvas,self.canvasWidth,self.canvasHeight)

        self.boardArray = FillingArray16GutiBoard()

        self.redGuti = ImageTk.PhotoImage(file="redGuti.png")
        self.greenGuti = ImageTk.PhotoImage(file="greenGuti.png")
        self.redguti = [] #holds information about the red guti image. a 2d array.
        self.greenguti = [] #holds information about the green guti image. a 2d array.
        self.redguti,self.greenguti= Drawing16GutiBoardRedBluePlayers(canvas,self.canvasWidth,self.canvasHeight,self.boardArray,self.redGuti,self.greenGuti)

        print(self.redguti)
        print(self.greenguti)
        self.x = 0
        self.y = 0

        self.starting_i = 0
        self.starting_j = 0
        self.released_i = 0
        self.released_j = 0
        self.gate = 0
        def moveGuti(event):
            self.x = int(event.x)
            self.y = int(event.y)

            possible_j = (self.x * 4)/self.canvasWidth
            possible_i = (self.y * 8) / self.canvasHeight

            possible_i = round(possible_i)
            possible_j = round(possible_j)
            if self.gate == 0:
                self.gate = 1
                self.starting_i = possible_i
                self.starting_j = possible_j
            if self.gate == 1:
                self.released_i = possible_i
                self.released_j = possible_j

            print(self.starting_i,self.starting_j)
            print(possible_i,possible_j)

            #moving a red guti
            if self.boardArray[self.starting_i][self.starting_j] == 2:
                new_x = int(possible_j * (self.canvasWidth)/4)
                new_y = int(possible_i * (self.canvasHeight) / 8)
                canvas.delete(self.redguti[self.starting_i][self.starting_j])
                self.redguti[self.starting_i][self.starting_j] = canvas.create_image(event.x, event.y, image=self.redGuti)

        def moveReleased(event):
            new_x = int(self.released_j * (self.canvasWidth) / 4)
            new_y = int(self.released_i * (self.canvasHeight) / 8)
            # moving a red guti
            if self.boardArray[self.starting_i][self.starting_j] == 2:
                canvas.delete(self.redguti[self.starting_i][self.starting_j])
                self.redguti[self.released_i][self.released_j] = canvas.create_image(new_x, new_y,image=self.redGuti)
                self.boardArray[self.starting_i][self.starting_j] = 0
                self.boardArray[self.released_i][self.released_j] = 2


            self.gate = 0
        canvas.bind('<B1-Motion>', moveGuti)
        canvas.bind('<ButtonRelease-1>', moveReleased)





class SixteenGuti_OneVAIPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        ##background
        self.img = ImageTk.PhotoImage(Image.open("woodtexture1.gif"))  # PIL solution
        background_label = tk.Label(self, image=self.img)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        buttonMenu = tk.Button(self, text="Back",
                               command=lambda: controller.show_frame("SixteenGutiPage"),height=2,width=10)
        buttonMenu.place(relx=0.90, rely=0.90, anchor="center")

class TwelveGutiPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Back to Menu",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":

    app = SampleApp()
    app.maxsize(750, 750)
    app.minsize(750,750)
    app.mainloop()

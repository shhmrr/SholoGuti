
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
    w = canvasWidth - 50
    h = canvasHeight - 50
    x_shift = 25
    y_shift = 25
    ##horizontal lines
    canvas.create_line(0 + x_shift,   0 + y_shift,   w + x_shift,   0 + y_shift,   fill='black', width=3)
    canvas.create_line(w/4 + x_shift,   h/8 + y_shift, 3*w/4 + x_shift,   h/8 + y_shift, fill='black', width=3)
    canvas.create_line(0 + x_shift, 2*h/8 + y_shift, w + x_shift, 2*h/8 + y_shift, fill='black', width=3)
    canvas.create_line(0 + x_shift, 3*h/8 + y_shift, w + x_shift, 3*h/8 + y_shift, fill='black', width=3)
    canvas.create_line(0 + x_shift, 4*h/8 + y_shift, w + x_shift, 4*h/8 + y_shift, fill='black', width=3)
    canvas.create_line(0 + x_shift, 5*h/8 + y_shift, w + x_shift, 5*h/8 + y_shift, fill='black', width=3)
    canvas.create_line(0 + x_shift, 6*h/8 + y_shift, w + x_shift, 6*h/8 + y_shift, fill='black', width=3)
    canvas.create_line(w/4 + x_shift, 7*h/8 + y_shift, 3*w/4+ x_shift, 7*h/8 + y_shift, fill='black', width=3)
    canvas.create_line(0 + x_shift,   h + y_shift,   w+ x_shift,   h + y_shift,   fill='black', width=3)
    ##vertical lines
    canvas.create_line(0 + x_shift, 2 * h / 8 + y_shift, 0 + x_shift, 6 * h / 8+ y_shift, fill='black', width=3)
    canvas.create_line(w/4 + x_shift, 2 * h / 8 + y_shift, w/4 + x_shift, 6 * h / 8+ y_shift, fill='black', width=3)
    canvas.create_line(2*w/4 + x_shift, 0 + y_shift, 2*w/4 + x_shift, h + y_shift, fill='black', width=3)
    canvas.create_line(3*w/4 + x_shift, 2 * h / 8 + y_shift, 3*w/4 + x_shift, 6 * h / 8+ y_shift, fill='black', width=3)
    canvas.create_line(w + x_shift, 2 * h / 8 + y_shift, w + x_shift, 6 * h / 8+ y_shift, fill='black', width=3)
    ##Diagonals top and bottom
    canvas.create_line(0+ x_shift, 0+ y_shift, 2*w/4+ x_shift, 2*h/8+ y_shift, fill='black', width=3)
    canvas.create_line(w+ x_shift, 0+ y_shift, 2 * w / 4+ x_shift, 2 * h / 8+ y_shift, fill='black', width=3)
    canvas.create_line(0+ x_shift, h+ y_shift, 2*w/4+ x_shift, 6*h/8+ y_shift, fill='black', width=3)
    canvas.create_line(w+ x_shift, h+ y_shift, 2*w/4+ x_shift,6*h/8+ y_shift, fill='black', width=3)
    ##Diagonals in the middle
    #up-left to bottom-right
    canvas.create_line(0 + x_shift, 2*h/8+ y_shift, w + x_shift, 6 * h / 8+ y_shift, fill='black', width=3)
    canvas.create_line(2*w/4 + x_shift, 2 * h / 8+ y_shift, w+ x_shift, 4 * h / 8+ y_shift, fill='black', width=3)
    canvas.create_line(0 + x_shift, 4 * h / 8+ y_shift, 2*w/4+ x_shift, 6 * h / 8+ y_shift, fill='black', width=3)
    ##bottom-left to up-right
    canvas.create_line(0 + x_shift, 4 * h / 8+ y_shift, 2*w/4 + x_shift, 2 * h / 8+ y_shift, fill='black', width=3)
    canvas.create_line(0 + x_shift, 6 * h / 8+ y_shift, w + x_shift, 2 * h / 8+ y_shift, fill='black', width=3)
    canvas.create_line(2*w/4 + x_shift, 6 * h / 8+ y_shift, w + x_shift, 4 * h / 8+ y_shift, fill='black', width=3)

def FillingArray16GutiBoard():
    #the 16guti game is played in a 9 by 5 board. row = 9 col = 5
    #red = 2
    #green = 1
    #blank = 0
    #invalid = -1
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
    canvasWidth = canvasWidth - 50
    canvasHeight = canvasHeight - 50
    x_shift = 25
    y_shift = 25

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
                greenguti1 = canvas.create_image(j * canvasWidth / 4 + x_shift, i * canvasHeight / 8 + y_shift, image=blueGuti)
                greenguti[i][j] = greenguti1
            if arr[i][j] == 2:
                redguti1 = canvas.create_image(j * canvasWidth / 4 + x_shift, i * canvasHeight / 8 + y_shift, image=redGuti)
                redguti[i][j] = redguti1
    return redguti,greenguti


def distanceInSquare(starting_j, starting_i, released_j, released_i):
    #x0,y0,x1,y1
    distInSqr = (starting_j - released_j)*(starting_j - released_j) + (starting_i - released_i)*(starting_i - released_i)
    return distInSqr
def isValid16GutiMove(starting_j, starting_i, released_j, released_i,distInSqr,boardArr,currentPlayer):

    #invalid moves on upper triangle
    if released_j == 1 and released_i == 0:
        return 0
    if released_j == 3 and released_i == 0:
        return 0
    if released_j == 0 and released_i == 1:
        return 0
    if released_j == 4 and released_i == 1:
        return 0
    # invalid moves on lower triangle
    if released_j == 1 and released_i == 8:
        return 0
    if released_j == 3 and released_i == 8:
        return 0
    if released_j == 0 and released_i == 7:
        return 0
    if released_j == 4 and released_i == 7:
        return 0
    #invalid two step moves with space in the middle on upper side
    if starting_j == 0and starting_i == 0and released_j == 0 and released_i ==  2:
        return 0
    if starting_j == 0and starting_i == 2and released_j == 0 and released_i ==  0:
        return 0
    if starting_j == 4and starting_i == 0and released_j == 4 and released_i ==  2:
        return 0
    if starting_j == 4and starting_i == 2and released_j == 4 and released_i ==  0:
        return 0

    if starting_j == 1 and starting_i == 1 and released_j == 1 and released_i == 3:
        return 0
    if starting_j == 1 and starting_i == 3 and released_j == 1 and released_i == 1:
        return 0
    if starting_j == 3 and starting_i == 1 and released_j == 3 and released_i == 3:
        return 0
    if starting_j == 3 and starting_i == 3 and released_j == 3 and released_i == 1:
        return 0

    if starting_j == 1 and starting_i == 1 and released_j == 1 and released_i == 2:
        return 0
    if starting_j == 1 and starting_i == 2 and released_j == 1 and released_i == 1:
        return 0
    if starting_j == 3 and starting_i == 1 and released_j == 3 and released_i == 2:
        return 0
    if starting_j == 3 and starting_i == 2 and released_j == 3 and released_i == 1:
        return 0

    if starting_j == 1 and starting_i == 1 and released_j == 0 and released_i == 2:
        return 0
    if starting_j == 0 and starting_i == 2 and released_j == 1 and released_i == 1:
        return 0
    if starting_j == 3 and starting_i == 1 and released_j == 4 and released_i == 2:
        return 0
    if starting_j == 4 and starting_i == 2 and released_j == 3 and released_i == 1:
        return 0

    if starting_j == 2 and starting_i == 0 and released_j == 0 and released_i == 2:
        return 0
    if starting_j == 0 and starting_i == 2 and released_j == 2 and released_i == 0:
        return 0
    if starting_j == 2 and starting_i == 0 and released_j == 4 and released_i == 2:
        return 0
    if starting_j == 4 and starting_i == 2 and released_j == 2 and released_i == 0:
        return 0

    if starting_j == 2 and starting_i == 1 and released_j == 1 and released_i == 2:
        return 0
    if starting_j == 1 and starting_i == 2 and released_j == 2 and released_i == 1:
        return 0
    if starting_j == 2 and starting_i == 1 and released_j == 3 and released_i == 2:
        return 0
    if starting_j == 3 and starting_i == 2 and released_j == 2 and released_i == 1:
        return 0

    if starting_j == 2 and starting_i == 1 and released_j == 0 and released_i == 3:
        return 0
    if starting_j == 0 and starting_i == 3 and released_j == 2 and released_i == 1:
        return 0
    if starting_j == 2 and starting_i == 1 and released_j == 4 and released_i == 3:
        return 0
    if starting_j == 4 and starting_i == 3 and released_j == 2 and released_i == 1:
        return 0

    if starting_j == 2 and starting_i == 0 and released_j == 1 and released_i == 1:
        return 0
    if starting_j == 1 and starting_i == 1 and released_j == 2 and released_i == 0:
        return 0
    if starting_j == 2 and starting_i == 0 and released_j == 3 and released_i == 1:
        return 0
    if starting_j == 3 and starting_i == 1 and released_j == 2 and released_i == 0:
        return 0


    # invalid two step moves with space in the middle on lower side
    if starting_j == 0and starting_i == 6and released_j == 0 and released_i ==  8:
        return 0
    if starting_j == 0and starting_i == 8and released_j == 0 and released_i ==  6:
        return 0
    if starting_j == 4and starting_i == 6and released_j == 4 and released_i ==  8:
        return 0
    if starting_j == 4and starting_i == 8and released_j == 4 and released_i ==  6:
        return 0

    if starting_j == 1and starting_i == 6and released_j == 1 and released_i ==  7:
        return 0
    if starting_j == 1and starting_i == 7and released_j == 1 and released_i ==  6:
        return 0
    if starting_j == 3and starting_i == 6and released_j == 3 and released_i ==  7:
        return 0
    if starting_j == 3and starting_i == 7and released_j ==  3and released_i ==  6:
        return 0

    if starting_j == 1and starting_i == 5and released_j == 1 and released_i ==  7:
        return 0
    if starting_j == 1and starting_i == 7and released_j == 1 and released_i ==  5:
        return 0
    if starting_j == 3and starting_i == 5and released_j == 3 and released_i ==  7:
        return 0
    if starting_j == 3and starting_i == 7and released_j ==  3and released_i ==  5:
        return 0

    if starting_j == 2and starting_i == 8and released_j == 1 and released_i ==  7:
        return 0
    if starting_j == 1and starting_i == 7and released_j == 2 and released_i ==  8:
        return 0
    if starting_j == 2and starting_i == 8and released_j == 3 and released_i ==  7:
        return 0
    if starting_j == 3and starting_i == 7and released_j ==  2and released_i ==  8:
        return 0

    if starting_j == 2and starting_i == 8and released_j == 0 and released_i ==  6:
        return 0
    if starting_j == 0and starting_i == 6and released_j == 2 and released_i ==  8:
        return 0
    if starting_j == 2and starting_i == 8and released_j == 4 and released_i ==  6:
        return 0
    if starting_j == 4and starting_i == 6and released_j ==  2and released_i ==  8:
        return 0

    if starting_j == 0and starting_i == 6and released_j == 1 and released_i ==  7:
        return 0
    if starting_j == 1and starting_i == 7and released_j == 0 and released_i ==  6:
        return 0
    if starting_j == 4and starting_i == 6and released_j == 3 and released_i ==  7:
        return 0
    if starting_j == 3and starting_i == 7and released_j ==  4and released_i ==  6:
        return 0

    if starting_j == 1 and starting_i == 6 and released_j == 2 and released_i == 7:
        return 0
    if starting_j == 2 and starting_i == 7 and released_j == 1 and released_i == 6:
        return 0
    if starting_j == 3 and starting_i == 6 and released_j == 2 and released_i == 7:
        return 0
    if starting_j == 2 and starting_i == 7 and released_j == 3 and released_i == 6:
        return 0

    if starting_j == 0 and starting_i == 5 and released_j == 2 and released_i == 7:
        return 0
    if starting_j == 2 and starting_i == 7 and released_j == 0 and released_i == 5:
        return 0
    if starting_j == 4 and starting_i == 5 and released_j == 2 and released_i == 7:
        return 0
    if starting_j == 2 and starting_i == 7 and released_j == 4 and released_i == 5:
        return 0

    #current player is red
    if currentPlayer == 2:
        print("Red Player")

        if distInSqr == 1 and boardArr[released_i][released_j] == 0: #moving one step horizontally or vertically and no coin on the place
            return 1 #1 is valid

        if distInSqr == 4: #moving two steps horizontally or vertically
            middle_i = int((starting_i + released_i)/2)
            middle_j = int((starting_j + released_j) / 2)
            if boardArr[middle_i][middle_j] == 1 and boardArr[released_i][released_j] == 0: #the middle position has an opponent coin i.e green
                return 2 #2 is valid and an opponent coin got eaten

        valid_diagonal_arr = [[0, 2], [2, 2], [4, 2], [1, 3], [3, 3], [0, 4], [2, 4], [4, 4], [1, 5], [3, 5], [0, 6],
                              [2, 6], [4, 6], [0, 0], [1, 1], [4, 0], [3, 1], [0, 8], [1, 7], [4, 8], [3, 7]]
        if distInSqr == 2: #moving one step diagonally
            #there are 12 valid points for diagonal movements
            for i in range(len(valid_diagonal_arr)):
                if starting_j == valid_diagonal_arr[i][0] and starting_i == valid_diagonal_arr[i][1] and boardArr[released_i][released_j] == 0:
                    return 1#valid one step diagonal movement


        if distInSqr == 8: #moving two steps diagonally
            middle_i = int((starting_i + released_i) / 2)
            middle_j = int((starting_j + released_j) / 2)
            # there are 12 valid points for diagonal movements
            for i in range(len(valid_diagonal_arr)):
                if starting_j == valid_diagonal_arr[i][0] and starting_i == valid_diagonal_arr[i][1] and boardArr[released_i][released_j] == 0:
                    if boardArr[middle_i][middle_j] == 1:  # the middle position has an opponent coin i.e green
                        return 2  # 2 is valid and an opponent coin got eaten



    #current player is green
    if currentPlayer == 1:
        return 1#valid
        print("Green Player")

        #unfinished code


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
        self.currentPlayer = 2 ##current player is Red
        print(self.redguti)
        print(self.greenguti)
        self.x = 0
        self.y = 0

        self.starting_i = 0
        self.starting_j = 0
        self.released_i = 0
        self.released_j = 0
        self.gate = 0
        self.x_shift = 25 #same shift applied in the drawing function
        self.y_shift = 25
        def moveGuti(event):
            self.x = int(event.x)
            self.y = int(event.y)

            possible_j = ((self.x - self.x_shift) * 4)/(self.canvasWidth - 2*self.x_shift)
            possible_i = ((self.y - self.y_shift) * 8) /(self.canvasHeight - 2*self.y_shift)

            possible_i = round(possible_i)
            possible_j = round(possible_j)
            if self.gate == 0:
                self.gate = 1
                self.starting_i = possible_i
                self.starting_j = possible_j
            if self.gate == 1:
                self.released_i = possible_i
                self.released_j = possible_j

            # print(self.starting_i,self.starting_j)
            # print(possible_i,possible_j)

            #moving a red guti
            if self.boardArray[self.starting_i][self.starting_j] == 2 and self.currentPlayer == 2:
                new_x = int(possible_j * (self.canvasWidth)/4 + self.x_shift)
                new_y = int(possible_i * (self.canvasHeight) / 8 + self.y_shift)
                canvas.delete(self.redguti[self.starting_i][self.starting_j])
                self.redguti[self.starting_i][self.starting_j] = canvas.create_image(event.x, event.y, image=self.redGuti)

            # moving a green guti
            if self.boardArray[self.starting_i][self.starting_j] == 1 and self.currentPlayer == 1:
                new_x = int(possible_j * (self.canvasWidth)/4)
                new_y = int(possible_i * (self.canvasHeight) / 8)
                canvas.delete(self.greenguti[self.starting_i][self.starting_j])
                self.greenguti[self.starting_i][self.starting_j] = canvas.create_image(event.x, event.y, image=self.greenGuti)

        def moveReleased(event):


            old_x = int(self.starting_j * (self.canvasWidth - 2*self.x_shift) / 4 + self.x_shift)
            old_y = int(self.starting_i * (self.canvasHeight - 2*self.y_shift) / 8 + self.y_shift)
            new_x = int(self.released_j * (self.canvasWidth - 2*self.x_shift) / 4 + self.x_shift)
            new_y = int(self.released_i * (self.canvasHeight - 2*self.y_shift) / 8 + self.y_shift)

            #distance between initial and released posiiton
            self.distInSqr = distanceInSquare(self.starting_j,self.starting_i,self.released_j,self.released_i)

            ## currentPlayer 1 is Green and 2 is Red
            # moving a red guti
            if self.boardArray[self.starting_i][self.starting_j] == 2 and self.currentPlayer == 2:

                if isValid16GutiMove(self.starting_j,self.starting_i,self.released_j,self.released_i,self.distInSqr,self.boardArray,self.currentPlayer):
                    canvas.delete(self.redguti[self.starting_i][self.starting_j])
                    self.redguti[self.released_i][self.released_j] = canvas.create_image(new_x, new_y,image=self.redGuti)
                    self.boardArray[self.starting_i][self.starting_j] = 0
                    self.boardArray[self.released_i][self.released_j] = 2
                    self.currentPlayer = 1#player now green
                else:
                    canvas.delete(self.redguti[self.starting_i][self.starting_j])
                    self.redguti[self.starting_i][self.starting_j] = canvas.create_image(old_x , old_y , image=self.redGuti)

            # moving a green guti
            if self.boardArray[self.starting_i][self.starting_j] == 1 and self.currentPlayer == 1:

                if isValid16GutiMove(self.starting_j, self.starting_i, self.released_j, self.released_i,
                                     self.distInSqr, self.boardArray, self.currentPlayer):
                    canvas.delete(self.greenguti[self.starting_i][self.starting_j])
                    self.greenguti[self.released_i][self.released_j] = canvas.create_image(new_x , new_y,
                                                                                         image=self.greenGuti)
                    self.boardArray[self.starting_i][self.starting_j] = 0
                    self.boardArray[self.released_i][self.released_j] = 1
                    self.currentPlayer = 2  # player now red
                else:
                    canvas.delete(self.greenguti[self.starting_i][self.starting_j])
                    self.greenguti[self.starting_i][self.starting_j] = canvas.create_image(old_x, old_y,
                                                                                         image=self.greenGuti)


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

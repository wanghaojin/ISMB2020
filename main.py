import tkinter as tk
import tkinter.ttk as ttk
import random
import math
 
UP = 1
DOWN = -1

COLORS = {
    UP: "black",
    DOWN: "white"
}

n = 300
beta = 0.6
speed = 1
cell_size = 2

class IsingModel:
    def __init__(self):
        self.n = n
        width = n
        height = n
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.board = [[UP for _ in range(height)] for _ in range(width)]
        self.running = True
        self.onestepp = False

        self.root = tk.Tk()
        self.root.title("Ising model")
        self.canvas = tk.Canvas(self.root, width=width*cell_size, height=height*cell_size)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.handle_click)
        self.start_button = tk.Button(self.root, text="Start", fg='white',bg='#4CAF50',font=('黑体',self.cell_size//2),command=self.start)
        self.start_button.place(relheight=0.05,relwidth=0.1,relx=0.02,rely=0.9)
        self.pause_button = tk.Button(self.root, text="Pause", fg='white',bg='#FE5E08',font=('黑体',self.cell_size//2),command=self.pause)
        self.pause_button.place(relheight=0.05,relwidth=0.1,relx=0.12,rely=0.9)
        self.clear_button = tk.Button(self.root, text="Clear", fg='white',bg='#555555',font=('黑体',self.cell_size//2),command=self.clear)
        self.clear_button.place(relheight=0.05,relwidth=0.1,relx=0.22,rely=0.9)
        self.random_button = tk.Button(self.root, text="Random",fg='white',bg='#5677FC',font=('黑体',self.cell_size//2), command=self.random_set)
        self.random_button.place(relheight=0.05,relwidth=0.1,relx=0.32,rely=0.9)
        
        var3 = tk.IntVar()
        def adjust2(event):
            global speed
            speed = var3.get()
        self.scale2 = tk.Scale(self.root,from_=1,to=100,resolution=1,bg='#A9A9A9',orient=tk.HORIZONTAL,length=200,variable=var3)
        self.scale2.bind('<ButtonRelease-1>',adjust2)
        self.scale2.place(relx=0.66,rely=0.1)
        self.labe2 = tk.Label(self.root,text='Frequency',font=('黑体',10))
        self.labe2.place(relx=0.8,rely=0.1)

    def handle_click(self, event):
        x, y = event.x // self.cell_size, event.y // self.cell_size
        if self.board[x][y] == UP:
            self.board[x][y] = DOWN
        else:
            self.board[x][y] = UP
        self.draw_board()
 
    def draw_board(self):
        self.canvas.delete("all")
        for x in range(self.width):
            for y in range(self.height):
                color = COLORS[self.board[x][y]]
                self.canvas.create_rectangle(x*self.cell_size, y*self.cell_size,
                                             (x+1)*self.cell_size, (y+1)*self.cell_size,
                                             fill=color, outline="gray")
 
    def start(self):
        self.running = True
        self.evolve()
 
    def pause(self):
        self.running = False
 
    def clear(self):
        self.board = [[UP for _ in range(self.height)] for _ in range(self.width)]
        self.draw_board()
 
    def random_set(self):
        for i in range(self.height):
            for j in range(self.width):
                rnd = random.random()
                if rnd > 0.5:
                    self.board[i][j]=DOWN
        self.draw_board()
    
    def rand(self, p):
        rando = random.uniform(0,1)
        if rando <= p:
            return UP
        else:
            return DOWN
    
    def new_value(self, x, y):
        n = self.n
        upward = 0 if y==0 else self.board[x][y-1]
        rightward = 0 if x == n-1 else self.board[x+1][y]
        downward = 0 if y == n -1 else self.board[x][y+1]
        lefyward = 0 if x==0 else self.board[x-1][y]
        sum = lefyward + upward + rightward + downward
        probability = 1 / (1 + math.exp(-2 * beta * sum))
        return self.rand(probability)
 
    def evolve(self):
        if not self.running:
            return
        new_board = [[UP for _ in range(self.height)] for _ in range(self.width)]
        for x in range(self.width):
            for y in range(self.height):
                new_board[x][y] = self.new_value(x, y)
        self.board = new_board
        self.draw_board()
        if not self.onestepp:
            global speed
            self.root.after(1000//speed, self.evolve)
        else:
            self.onestepp = False
 
    def run(self):
        self.draw_board()
        self.root.mainloop()

game = IsingModel()
game.run()
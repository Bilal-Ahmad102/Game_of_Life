from pyglet.shapes import Line,Rectangle
import random
class Grid():
    def __init__(self,width,height) -> None:
        self.width = width
        self.height = height
        self.color = (255,255,255)
        self.cell_color = (60,60,50)
        self.size_of_box = 20
        
        self.columns = self.width//self.size_of_box
        self.rows = self.height//self.size_of_box

        self.lines   = []
        self.cells   = []
        self.squares = []

    def setup_grid(self,batch):
        for i in range(0,self.rows+1):   
            if i == self.rows:  y = (self.size_of_box*i)-1 
            else:               y = self.size_of_box*i
            self.lines.append(Line(x  =0,          y  =y,
                                   x2 =self.width, y2 =y,
                                   width=1,color=self.cell_color,batch=batch))        
        for i in range(0,self.columns+1):
            if i == 0:  x  = 1
            else:       x = self.size_of_box*i
            self.lines.append(Line(x  = x,          y  =0,
                                   x2 = x, y2 =self.height,
                                   width=1,color=self.cell_color,batch=batch))        
        for i in range(self.rows):
            self.cells.append([0 for _ in range(self.columns)])

        self.cells = [[random.choice([0, 1]) for _ in range(len(self.cells[0]))] for _ in range(len(self.cells))]

    def get_neighbours_status(self,x, y):
        total = 0
        # Loop through all possible neighbors
        for i in range(-1, 2):
            for j in range(-1, 2):
                # Skip the cell itself
                if i == 0 and j == 0:
                    continue
                # Calculate neighbor's coordinates
                nx, ny = x + i, y + j
                # Check if neighbor is within bounds
                if 0 <= nx < len(self.cells) and 0 <= ny < len(self.cells[0]):
                    if self.cells[nx][ny] == 1:
                        total += 1
        return total
    def update(self):
        new_cells = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.columns):
                alive_neighbours = self.get_neighbours_status(i, j)
                if self.cells[i][j] == 1:
                    if alive_neighbours == 2 or alive_neighbours == 3:
                        new_cells[i][j] = 1
                    else:
                        new_cells[i][j] = 0
                else:
                    if alive_neighbours == 3:
                        new_cells[i][j] = 1
                    else:
                        new_cells[i][j] = 0
        self.cells = new_cells
    def show(self, batch):
        self.squares.clear()
        for i in range(self.rows):
            for j in range(self.columns):
                if self.cells[i][j] == 1:
                    x = j * self.size_of_box  
                    y = i * self.size_of_box
                    self.squares.append(Rectangle(x, y,
                                                width=self.size_of_box-1, height=self.size_of_box-1,
                                                color=self.color, batch=batch))                    
                    
    def get_random_color(self):
        return (random.randint(0,255),random.randint(0,255),random.randint(0,255))                    
        # return (0,255,255)                    

                    
                    
                    
                    
                    
                    
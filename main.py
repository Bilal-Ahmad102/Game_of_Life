import pyglet as pg
from grid import Grid
import random

class Space():
    def __init__(self):
        self.window = pg.window.Window(1280,720)        
        # self.window = pg.window.Window(1200,700)
        self.lines_batch = pg.graphics.Batch()
        self.cells_batch = pg.graphics.Batch()
        self.window.push_handlers(on_draw=self.draw)
        self.grid = None
        self.grid_setup()
        print(self.window.width,self.window.height)
        pg.clock.schedule_interval(self.update,1/5)

    def grid_setup(self):
        self.grid = Grid(self.window.width,self.window.height)
        self.grid.setup_grid(self.lines_batch)

    def update(self,dt):
        self.grid.update()
        self.grid.show(self.cells_batch)
        # self.cells_batch = pg.graphics.Batch()

    def draw(self):
        self.window.clear()
        self.lines_batch.draw()    
        self.cells_batch.draw()
    
    def run(self):
        pg.app.run()
        
        
app = Space()
app.run()
from settings import *
from tetris import Tetris
import sys

class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption("Tetris Game")
        self.screen = pg.display.set_mode(FIELD_RES)
        self.clock = pg.time.Clock()
        self.set_timer()
        self.tetris = Tetris(self)

    def set_timer(self):
        self.user_event = pg.USEREVENT + 0
        self.anim_trigger = False
        pg.time.set_timer(self.user_event, ANIM_TIME_INTERVAL)

    def update(self):
        self.clock.tick(FPS)
        self.tetris.update()
    
    def draw_grid(self):
        for x in range(10):
            for y in range(20):
                pg.draw.rect(self.screen, (40,40,40),
                             (x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    def draw(self):
        self.screen.fill(color=FIELD_COLOR)
        self.draw_grid()
        self.tetris.draw()
        pg.display.flip()
        
    def check_for_events(self):
        self.anim_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == self.user_event:
                self.anim_trigger = True

    def run(self):
        while True:
            self.check_for_events()
            self.update()
            self.draw()

if __name__ == "__main__":
    game = App()
    game.run()
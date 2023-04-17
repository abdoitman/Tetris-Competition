from settings import *
from tetris import Tetris
import sys

class App:
    def __init__(self) -> None:
        pg.init()
        pg.display.set_caption("Tetris Game")
        self.screen = pg.display.set_mode(FIELD_RES)
        self.clock = pg.time.Clock()
        self.tetris = Tetris(self)

    def update(self):
        self.clock.tick(FPS)
        self.tetris.update()
    
    def draw(self):
        self.screen.fill(color=FIELD_COLOR)
        pg.display.flip()
        self.tetris.draw()

    def check_for_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_for_events()
            self.update()
            self.draw()

if __name__ == "__main__":
    game = App()
    game.run()
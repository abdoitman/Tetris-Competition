from settings import *
from tetris import Tetris, Text

class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption("Tetris Game")
        self.screen = pg.display.set_mode(WIN_RES)
        self.clock = pg.time.Clock()
        self.counter = GAME_DURATION * 100 * FPS
        self.tetris = Tetris(self)
        self.text = Text(self)
        self.set_timer()
        self.tetris.state = self.tetris.return_state_info()
        self.tetris.control_via_array(["MOV_L" , "ROT_CW" , "ROT_CW" , "MOV_D"])

    def set_timer(self):
        self.user_event = pg.USEREVENT + 0
        self.fast_user_event = pg.USEREVENT + 1
        self.anim_trigger = False
        self.fast_anim_trigger = False
        pg.time.set_timer(self.user_event, ANIM_TIME_INTERVAL)
        pg.time.set_timer(self.fast_user_event, FAST_ANIM_TIME_INTERVAL)

    def update(self):
        self.clock.tick(FPS)
        self.counter -= FPS 
        self.tetris.update()
    
    def draw_grid(self):
        for x in range(10):
            for y in range(20):
                pg.draw.rect(self.screen, (20,20,20),
                             (x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    def draw(self):
        self.screen.fill(color=INFO_BG_COLOR)
        self.screen.fill(color=FIELD_COLOR, rect=(0, 0, *FIELD_RES))
        self.tetris.draw()
        self.draw_grid()
        self.text.draw()
        pg.display.flip()
        
    def check_for_events(self):
        self.anim_trigger = False
        self.fast_anim_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif self.counter <= 0:
                pg.time.wait(1000)
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self.tetris.control(pressed_key= event.key)
            elif event.type == self.user_event:
                self.anim_trigger = True
            elif event.type == self.fast_user_event:
                self.fast_anim_trigger = True

    def run(self):
        while True:
            self.check_for_events()
            self.update()
            self.draw()

if __name__ == "__main__":
    game = App()
    game.run()
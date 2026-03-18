import pygame as pg

class App:
    def initialize(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def run(self):
        pg.init()
        self.screen = pg.display.set_mode((800, 600))
        pg.display.set_caption("PyBuilder")
        clock = pg.time.Clock()
        running = True
        self.initialize()
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            self.handle_input()
            self.update()
            self.draw()
            pg.display.flip()
            clock.tick(60)

import pygame as pg

from areas import viewport


class App:
    def initialize(self):
        self.area_options = [viewport.Viewport]

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
            self.update()
            self.draw()
            pg.display.flip()
            clock.tick(60)

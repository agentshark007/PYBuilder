import pygame as pg

from area import viewport


class App:
    def initialize_areas(self):
        for area in self.areas:
            area.initialize(self)

    def initialize(self):
        self.area_options = [viewport.Viewport]
        self.areas = [self.area_options[0](pg.Rect(0, 0, *self.screen.get_size()))]
        self.initialize_areas()

    def update_area_positions(self):
        # Temporary code until dynamic areas
        self.areas[0].rect = pg.Rect(0, 0, *self.screen.get_size())

    def update_areas(self):
        for area in self.areas:
            area.update(self)

    def update(self):
        self.update_area_positions()
        self.update_areas()

    def draw_areas(self):
        for area in self.areas:
            area.draw(self)
            self.screen.blit(area.surface, (area.rect.x, area.rect.y))

    def draw(self):
        self.draw_areas()

    def run(self):
        pg.init()
        pg.display.set_mode((800, 600), pg.RESIZABLE)
        pg.display.set_caption("PYBuilder")
        self.screen = pg.display.get_surface()

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

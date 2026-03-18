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
        self.gui_scale = 1.0
        self.gui_scale_speed = 2

    def update_gui_scale(self):
        cmd = self.keys[pg.K_LMETA] or self.keys[pg.K_RMETA]

        if cmd and self.keys[pg.K_MINUS]:
            self.gui_scale /= self.gui_scale_speed**self.deltatime

        if cmd and self.keys[pg.K_EQUALS]:
            self.gui_scale *= self.gui_scale_speed**self.deltatime

    def update_area_positions(self):
        # Temporary code until dynamic areas
        display_rect = self.screen.get_rect()
        for area in self.areas:
            area.rect = display_rect.copy()
            area.resize_surface()

    def update_areas(self):
        for area in self.areas:
            area.update(self)

    def update(self):
        self.keys = pg.key.get_pressed()
        self.update_gui_scale()
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
        self.target_fps = 60
        self.deltatime = 1 / 60
        running = True
        self.initialize()
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            self.update()
            self.draw()
            pg.display.flip()
            self.deltatime = clock.tick(self.target_fps) / 1000.0

import pygame as pg


class Area:
    def __init__(self, name: str, rect: pg.Rect):
        self.name = name
        self.frame_rect = rect.copy()
        self.bar_rect = rect.copy()
        self.rect = rect
        self.surface = pg.Surface(self.rect.size)

    def resize_surface(self):
        self.surface = pg.Surface(self.rect.size)

    def initialize(self, app):
        pass

    def update(self, app):
        pass

    def draw(self, app):
        self.surface.fill((0, 0, 0))

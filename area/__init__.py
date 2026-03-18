import pygame as pg


class Area:
    def __init__(self, name: str, rect: pg.Rect):
        self.name = name
        self.rect = rect
        self.surface = pg.Surface((rect.width, rect.height))

    def initialize(self, app):
        pass

    def update(self, app):
        pass

    def draw(self, app):
        pass

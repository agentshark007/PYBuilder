import pygame as pg

from area import Area


class Viewport(Area):
    def __init__(self, rect):
        super().__init__("Viewport", rect)

    def initialize(self, app):
        pass

    def update(self, app):
        pass

    def draw(self, app):
        self.surface.fill((0, 0, 0))

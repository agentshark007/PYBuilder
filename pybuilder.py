import pygame as pg

from area import Area
from area import viewport


class App:
    def initialize_areas(self):
        for area in self.areas:
            area.initialize(self)

    def initialize(self):
        self.area_options = [viewport.Viewport]
        self.areas: list[Area] = [self.area_options[0](pg.Rect(0, 0, *self.screen.get_size()))]
        self.initialize_areas()
        self.gui_scale = 1.0
        self.gui_scale_speed = 2
        self.min_gui_scale = 0.5
        self.max_gui_scale = 3.0
        self.area_bar_height_base = 28
        self.area_border_width_base = 2
        self.area_frame_bg = (24, 24, 24)
        self.area_bar_bg = (45, 45, 45)
        self.area_outline_color = (128, 128, 128)
        self.area_title_color = (230, 230, 230)
        self.area_title_padding_base = 8
        self.area_title_font_size_base = 20
        self._area_title_font_size = 0
        self.area_title_font = pg.font.SysFont(None, self.area_title_font_size_base)

    def get_scaled_area_metrics(self):
        border_width = max(1, int(round(self.area_border_width_base * self.gui_scale)))
        bar_height = max(4, int(round(self.area_bar_height_base * self.gui_scale)))
        title_padding = max(2, int(round(self.area_title_padding_base * self.gui_scale)))
        title_font_size = max(8, int(round(self.area_title_font_size_base * self.gui_scale)))
        divider_width = max(1, border_width // 2)

        if title_font_size != self._area_title_font_size:
            self.area_title_font = pg.font.SysFont(None, title_font_size)
            self._area_title_font_size = title_font_size

        return {
            "border_width": border_width,
            "bar_height": bar_height,
            "title_padding": title_padding,
            "divider_width": divider_width,
        }

    def update_gui_scale(self):
        cmd = self.keys[pg.K_LMETA] or self.keys[pg.K_RMETA]

        if cmd and self.keys[pg.K_MINUS]:
            self.gui_scale /= self.gui_scale_speed**self.deltatime

        if cmd and self.keys[pg.K_EQUALS]:
            self.gui_scale *= self.gui_scale_speed**self.deltatime

        self.gui_scale = max(self.min_gui_scale, min(self.gui_scale, self.max_gui_scale))

    def update_area_positions(self):
        # Temporary code until dynamic areas
        display_rect = self.screen.get_rect()
        metrics = self.get_scaled_area_metrics()
        for area in self.areas:
            area.frame_rect = display_rect.copy()

            border_width = metrics["border_width"]
            inner_width = max(1, area.frame_rect.width - border_width * 2)
            inner_height = max(1, area.frame_rect.height - border_width * 2)
            bar_height = min(metrics["bar_height"], max(1, inner_height - 1))
            content_height = max(1, inner_height - bar_height)

            area.bar_rect = pg.Rect(
                area.frame_rect.x + border_width,
                area.frame_rect.y + border_width,
                inner_width,
                bar_height,
            )
            area.rect = pg.Rect(
                area.frame_rect.x + border_width,
                area.frame_rect.y + border_width + bar_height,
                inner_width,
                content_height,
            )

            if area.surface.get_size() != area.rect.size:
                area.resize_surface()

    def draw_area_frame(self, area):
        metrics = self.get_scaled_area_metrics()
        border_width = metrics["border_width"]
        frame_surface = pg.Surface(area.frame_rect.size)
        frame_surface.fill(self.area_frame_bg)

        local_bar_rect = pg.Rect(
            border_width,
            border_width,
            area.bar_rect.width,
            area.bar_rect.height,
        )
        local_content_pos = (border_width, border_width + area.bar_rect.height)

        frame_surface.fill(self.area_bar_bg, local_bar_rect)
        frame_surface.blit(area.surface, local_content_pos)

        divider_y = border_width + area.bar_rect.height
        pg.draw.line(
            frame_surface,
            self.area_outline_color,
            (border_width, divider_y),
            (frame_surface.get_width() - border_width - 1, divider_y),
            metrics["divider_width"],
        )
        pg.draw.rect(frame_surface, self.area_outline_color, frame_surface.get_rect(), width=border_width)

        title_surface = self.area_title_font.render(area.name, True, self.area_title_color)
        title_pos = (
            border_width + metrics["title_padding"],
            local_bar_rect.centery - title_surface.get_height() // 2,
        )
        frame_surface.blit(title_surface, title_pos)

        self.screen.blit(frame_surface, area.frame_rect.topleft)

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
            self.draw_area_frame(area)

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

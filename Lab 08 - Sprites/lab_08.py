import arcade
import math

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class monedas(arcade.Sprite):

    def __init__(self, sprite1, sprite_scaling):
        """ Constructor. """

        super().__init__(sprite1, sprite_scaling)

        self.circle_angle = 0

        self.circle_radius = 0

        self.circle_speed = 0.008
        self.circle_center_x = 0
        self.circle_center_y = 0

    def update(self):
        self.center_x = self.circle_radius * math.sin(self.circle_angle) \
            + self.circle_center_x
        self.center_y = self.circle_radius * math.cos(self.circle_angle) \
            + self.circle_center_y

        #subimos el angulo para el siguiente mov
        self.circle_angle += self.circle_speed
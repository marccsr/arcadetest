import arcade

SCR_W=800
SCR_H=600

def dib_suelo():
    """dibujamos el suelo, en este caso es nieve"""
    arcade.draw_lrtb_rectangle_filled(0, SCR_W, SCR_H / 3, 0, arcade.color.ANTI_FLASH_WHITE)

def dib_muneco():
    """dibujamos el muñeco de nieve"""
    #cuerpo
    arcade.draw_circle_filled(500, 260, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(500, 340, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(500, 400, 40, arcade.color.WHITE)
    #ojos
    arcade.draw_circle_filled(485, 410, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(515, 410, 5, arcade.color.BLACK)
    #brazos
    arcade.draw_line(450,340,410,360, arcade.color.BLACK)
    arcade.draw_line(550,340,590,360, arcade.color.BLACK)

def dib_iglu():
    """dibujamos el iglú junto al muñeco de nieve"""
    arcade.draw_parabola_filled(100,-100,400,300,arcade.color.WHITE)

def dib_all(tDelta):
    """invocar a todas las funciones para dibujar la escena completa"""
    arcade.start_render()
    dib_suelo()
    dib_muneco()
    dib_iglu()

def main():
    arcade.open_window(SCR_W, SCR_H, "Dibujando con funciones")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

    #llamamos a la función dib_all cada 3s
    arcade.schedule(dib_all, 3)
    arcade.run()

#llamamos a main() para poder comenzar a dibujar
main()
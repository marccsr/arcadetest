import arcade

# abrimos una ventana nueva
arcade.open_window(800, 600, "Dibujo de ejemplo")

# especificamos el color de fondo
arcade.set_background_color([73, 9, 122])

# dibujamos el atardecer con varios colores
arcade.draw_lrtb_rectangle_filled(0, 800, 300, 200, [187, 11, 214])
arcade.draw_lrtb_rectangle_filled(0, 800, 400, 300, [124, 11, 158])
arcade.draw_lrtb_rectangle_filled(0, 800, 500, 400, [95, 6, 150])

# empezamos a dibujar
arcade.start_render()

# dibujamos la sombra
arcade.draw_lrtb_rectangle_filled(0, 800, 100, 0, arcade.color.BLACK)

# ***dibujamos los edificios***
# **primer edificio**
arcade.draw_lrtb_rectangle_filled(0, 250, 525, 50, arcade.color.BLACK)

# ventanas
arcade.draw_lrtb_rectangle_filled(50,100,475,425,[233, 237, 14])
arcade.draw_lrtb_rectangle_filled(50,100,200,150,[233, 237, 14])
arcade.draw_lrtb_rectangle_filled(150,200,475,425,[233, 237, 14])
arcade.draw_lrtb_rectangle_filled(150,200,200,150,[233, 237, 14])

# **segundo edificio**
arcade.draw_lrtb_rectangle_filled(600, 800, 400, 50, arcade.color.BLACK)

# ventanas
arcade.draw_lrtb_rectangle_filled(650,675,375,325,[233, 237, 14])
arcade.draw_lrtb_rectangle_filled(725,750,375,325,[233, 237, 14])
arcade.draw_lrtb_rectangle_filled(650,675,200,150,[233, 237, 14])
arcade.draw_lrtb_rectangle_filled(725,750,200,150,[233, 237, 14])

# **tercer edificio**
arcade.draw_lrtb_rectangle_filled(250,370,260,50, arcade.color.BLACK)

# ventanas
arcade.draw_lrtb_rectangle_filled(275,300,240,210,[233, 237, 14])
arcade.draw_lrtb_rectangle_filled(275,300,200,170,[233, 237, 14])
arcade.draw_lrtb_rectangle_filled(340,355,240,210,[233, 237, 14])
arcade.draw_lrtb_rectangle_filled(340,355,200,170,[233, 237, 14])

# ***terminamos de dibujar***
arcade.finish_render()

# dejamos la ventana abierta hasta que se cierre manualmente
arcade.run()
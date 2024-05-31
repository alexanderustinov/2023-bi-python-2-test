import cairo

WIDTH, HEIGHT = 600, 400

with cairo.SVGSurface("iceland_flag.svg", WIDTH, HEIGHT) as surface:
    cr = cairo.Context(surface)

    cr.set_source_rgb(0, 0, 0.56)
    cr.rectangle(0, 0, WIDTH, HEIGHT)
    cr.fill()

    cr.set_source_rgb(1, 1, 1)
    cr.rectangle(140, 0, 120, 400)
    cr.fill()

    cr.set_source_rgb(1, 1, 1)
    cr.rectangle(0, HEIGHT//3, WIDTH, 120)
    cr.fill()

    cr.set_source_rgb(1, 0, 0)
    cr.rectangle(0, HEIGHT // 2.5, WIDTH, 60)
    cr.fill()

    cr.set_source_rgb(1, 0, 0)
    cr.rectangle(WIDTH // 3.5, 0, 60, WIDTH)
    cr.fill()

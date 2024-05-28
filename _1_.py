import cairo
from math import pi

with cairo.SVGSurface('pic.svg', 500, 500) as surface:
    ctx = cairo.Context(surface)
    ctx.move_to(0, 0)

    ctx.set_source_rgba(1, 0, 0)
    ctx.rectangle(50, 50, 400, 50)
    ctx.fill()

    ctx.set_source_rgba(0, 0, 255)
    ctx.rectangle(50, 100, 400, 50)
    ctx.fill()

    ctx.set_source_rgba(1, 0.5 , 0)
    ctx.rectangle(50, 150, 400, 50)
    ctx.fill()

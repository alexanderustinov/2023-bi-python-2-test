import cairo
import os

WIDTH = 402
HEIGHT = 300
x = -133
y = 0
sfc = cairo.ImageSurface(cairo.Format.ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(sfc)

ctx.set_source_rgb(1, 1, 1)
ctx.rectangle(0, 0, WIDTH, HEIGHT)
ctx.paint()

ctx.set_source_rgb(0, 0, 0)
ctx.move_to(x,y)
ctx.line_to(x,y + 300)
ctx.line_to(x + 133,y + 300)
ctx.line_to(x + 133,y)
ctx.close_path()
ctx.fill_preserve()

ctx.set_source_rgb(1, 1, 0)
x = 133
ctx.move_to(x,y)
ctx.line_to(x,y + 300)
ctx.line_to(x + 140,y + 300)
ctx.line_to(x + 140,y)
ctx.line_to(x,y)
ctx.close_path()
ctx.fill_preserve()

x = 269
ctx.set_source_rgb(1, 0, 0)
ctx.move_to(x,y)
ctx.line_to(x,y + 300)
ctx.line_to(x + 133,y + 300)
ctx.line_to(x + 133,y)
ctx.line_to(x,y)
ctx.close_path()
ctx.fill_preserve()

ctx.stroke()

output_filename = 'Belg.png'
sfc.write_to_png(output_filename)
os.system(output_filename)

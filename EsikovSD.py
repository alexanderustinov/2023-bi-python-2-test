import cairo



with cairo.SVGSurface("result.svg", 900, 600) as surf:
    context = cairo.Context(surf)

    context.set_source_rgba(0, .53, .32, 1) 
    context.rectangle(0, 0, 360, 640)
    context.fill_preserve()
    context.set_source_rgba(0, 0, 0, 0)
    context.stroke()
    
    context.set_source_rgba(.988, .819, .086, 1) 
    context.rectangle(360, 0, 640, 300)
    context.fill_preserve()
    context.set_source_rgba(0, 0, 0, 0)
    context.stroke()

    context.set_source_rgba(.909, .067, .176, 1) 
    context.rectangle(360, 300, 640, 300)
    context.fill_preserve()
    context.set_source_rgba(0, 0, 0, 0)
    context.stroke()


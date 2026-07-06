init -1 python:
    SCREEN_W = config.screen_width
    SCREEN_H = config.screen_height

transform resizer:
    size (SCREEN_W, SCREEN_H)

transform fill_screen:
    subpixel True
    xalign 0.5 yalign 0.5
    size (SCREEN_W, None) 
    fit "cover"

init python:
    import os

    for file in renpy.list_files():
        if file.startswith("images/bg/") and file.lower().endswith((".png", ".jpg", ".webp")):
            
            name = os.path.splitext(os.path.basename(file))[0]
            
            renpy.image("bg " + name, At(file, resizer))

init python:
    def auto_aspect_ratio(d):
        return Frame(d, size=(SCREEN_W, SCREEN_H))
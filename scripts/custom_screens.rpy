screen warning_screen():
    text """{font=gui/fonts/cmunorm.ttf}{size=40}Warning! This game contains themes such as
Violence, strong language, and sexual themes
Player discretion is advised{/size}{/font}""":
        xalign 0.5
        yalign 0.45
        text_align 0.5
        line_leading 10
        color "#ffffff"

screen disclaimer_screen():
    text """{font=gui/fonts/cmunorm.ttf}{size=40}The places, events, and characters
in this game are all works of fiction.
Any similarities to real life are
purely coincidental and do not have
any correlation with the game.{/size}{/font}""":
        xalign 0.5
        yalign 0.45
        text_align 0.5
        line_leading 10
        color "#ffffff"


screen basic_controls():
    text """{font=gui/fonts/cmunorm.ttf}{size=40} Basic Controls
    Left Click / Space / Enter — Advance dialogue
    Right Click / Escape — Open menu
    Middle Click — Hide textbox
    Scroll Up — Rollback \n
    Best with earphones{/size}{/font}""":
        xalign 0.5
        yalign 0.45
        text_align 0.5
        line_leading 10
        color "#ffffff"


screen press_to_continue():
    text "{font=gui/fonts/cmunorm.ttf}{size=40}Press any button or click anywhere to continue{/font}":
        xalign 0.5
        yalign 0.90
        text_align 0.5
        color "#ffffff"


screen infinite_scream():
    zorder 50
    default a_str = ""

    # cps ≈ 10
    timer 0.10 repeat True action SetScreenVariable("a_str", a_str + "A")

    python:
        _full  = "A" + a_str + "AH"
        _cpl   = 16   # characters per line — increase if text wraps too early,
        _lines = [ _full[i : i + _cpl] for i in range(0, len(_full), _cpl) ]
        _wrapped = "\n".join(_lines)

    text "{font=gui/fonts/cmunorm.ttf}{size=160}[_wrapped]{/size}{/font}":
        xalign 0.5
        yalign 0.5


screen infinite_iloveu():
    zorder 50

    default a_str = ""

    timer 0.6 repeat True action SetScreenVariable("a_str", a_str + "I love U ")

    python:
        _full = a_str
        _cpl = 16
        _lines = [_full[i : i + _cpl] for i in range(0, len(_full), _cpl)]
        _wrapped = "\n".join(_lines)

    text "{font=gui/fonts/cmunorm.ttf}{size=120}[_wrapped]{/size}{/font}":
        xalign 0.5
        yalign 0.5
        xsize config.screen_width
        ysize config.screen_height
        text_align 0.5
        layout "subtitle"


transform frantic_shake:
    subpixel True
    pos (0.5, 0.5) anchor (0.5, 0.5)
    zoom 1.05 
    
    block:
        choice:
            linear 0.05 xoffset 18  yoffset -12 blur 2
        choice:
            linear 0.05 xoffset -20 yoffset 15 blur 10
        choice:
            linear 0.05 xoffset 14  yoffset 20 blur 4
        choice:
            linear 0.05 xoffset -16 yoffset -18 blur 8
        choice:
            linear 0.05 xoffset 22  yoffset 10 blur 0
        choice:
            linear 0.05 xoffset -12 yoffset -22 blur 12
        repeat


transform shake_settle(t=3.0):
    subpixel True
    xoffset 20 yoffset -20 blur 10
    easeout t xoffset 0 yoffset 0 blur 0


#Exposed pics
default obj_index = 1
image obj_pic1 = "images/objects/pic 1.webp"
image obj_pic2 = "images/objects/pic 2.webp"
image obj_pic3 = "images/objects/pic 3.webp"
image obj_pic4 = "images/objects/pic 4.webp"

screen object_viewer():
    zorder 10

    frame:
        xalign 0.5
        yalign 0.5
        background "#ffffff"
        padding (12, 12)

        add "obj_pic[obj_index]":
            zoom 2.5

    button:
        xysize (config.screen_width, config.screen_height)
        background None
        action If(obj_index < 4, [SetVariable("obj_index", obj_index + 1)], [Hide("object_viewer")])


# Bus hit
define whiteout_dissolve = ImageDissolve("images/wipes/radial_mask.png", 1.5, ramplen=256)

screen white_out(duration=1.5, hold=0.3, then_hide=True):
    zorder 200
    add Solid("#ffffff")

    if then_hide:
        timer duration + hold action Hide("white_out")


## Dream Scene Custom Screens
screen centered_line(line_text):
    zorder 100
    text line_text:
        xalign 0.5
        yalign 0.5
        xsize 900
        text_align 0.5
        color "#ffffff"
        size 34
        font "gui/fonts/cmunorm.ttf"
        outlines [(2, "#000000", 0, 0)]

transform water_in:
    alpha 0.0
    blur 12.0
    yoffset 8
    parallel:
        ease 0.9 alpha 1.0
    parallel:
        ease 0.9 blur 0.0
    parallel:
        ease 0.9 yoffset 0

transform water_out:
    alpha 1.0
    blur 0.0
    parallel:
        ease 0.7 alpha 0.0
    parallel:
        ease 0.7 blur 14.0
    parallel:
        ease 0.7 yoffset -8

init python:
    def get_line_pause(text_line, min_pause=1.0, max_pause=3.0, chars_per_sec=18.0):
        duration = len(text_line) / chars_per_sec
        return max(min_pause, min(max_pause, duration))

init python:
    def get_line_pause(text_line, min_pause=1.0, max_pause=3.0, chars_per_sec=18.0):
        duration = len(text_line) / chars_per_sec
        return max(min_pause, min(max_pause, duration))

    def show_positioned_line(line_text, xalign_value):
        txt = Text(line_text, xalign=xalign_value, yalign=0.5, xsize=700,
                text_align=xalign_value, color="#ffffff", size=64,
                outlines=[(2, "#000000", 0, 0)], line_spacing=6)
        renpy.show("water_line", what=txt, at_list=[water_in], zorder=100)
        renpy.pause(0.9, hard=False)
        renpy.pause(get_line_pause(line_text), hard=False)
        renpy.show("water_line", what=txt, at_list=[water_out], zorder=100)
        renpy.pause(0.7, hard=False)
        renpy.hide("water_line")
        renpy.pause(0.3, hard=False)
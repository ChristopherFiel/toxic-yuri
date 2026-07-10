screen warning_screen():
    text """{font=gui/fonts/cmunorm.ttf}{size=40}Warning! This game is intended for ages 18+
It contains adult themes such as
kidnapping, manipulation, violence,
foul language, and sexual themes
Viewer discretion is advised{/size}{/font}""":
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
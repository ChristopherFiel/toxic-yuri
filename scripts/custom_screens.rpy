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


screen infinite_scream():
    zorder 50
    default a_str = ""

    # cps ≈ 10
    timer 0.10 repeat True action SetScreenVariable("a_str", a_str + "A")

    python:
        _full  = "WA" + a_str + "A"
        _cpl   = 16   # characters per line — increase if text wraps too early,
        _lines = [ _full[i : i + _cpl] for i in range(0, len(_full), _cpl) ]
        _wrapped = "\n".join(_lines)

    text "{font=Midnightconstellations-YLgo.ttf}{size=160}[_wrapped]{/size}{/font}":
        xalign 0.5
        yalign 0.5
        text_align 0.5
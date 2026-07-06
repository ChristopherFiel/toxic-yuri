## Motion Sells Emotion: an ATL animation pack for Ren'Py, by EdgesSystem ######
## https://edgessystem.itch.io/motion-sells-emotion ############################
## This work is licensed under Creative Commons Attribution 4.0 International ##
## https://creativecommons.org/licenses/by/4.0/ ################################

define scale = 1.0

transform full:
    ypos 1.0
    zoom 1/scale

transform medlong:
    ypos 1.45
    zoom 1.5/scale

transform medium:
    ypos 1.9
    zoom 2.0/scale

transform medclose:
    ypos 2.7
    zoom 3/scale

transform close:
    ypos 4.4
    zoom 5.0/scale

transform closeshort:
    ypos 4.2
    zoom 5.0/scale

transform flicker(rate=1,min=0.45,max=0.5):
    alpha max
    choice:
        rate+0.2*rate
    choice:
        rate
    choice:
        rate-0.2*rate
    linear 0.1*rate alpha min
    linear 0.1*rate alpha max
    repeat

transform fast_moveoutright:
    yalign 0.5
    easeout 0.5 xalign 1.5

transform slide_in_left:
    xpos -0.5 xanchor 1.0
    yalign 1.0
    ease 1.5 xpos 0.55 xanchor 0.5
    ease 0.15 xpos 0.5


transform zoom_to(target_x, target_y, zoom_level=2.0):
    xanchor target_x
    yanchor target_y
    xpos    target_x
    ypos    target_y
    zoom    zoom_level

transform pan_to(target_x, target_y, zoom_level=1.8, dur=1.0):
    linear dur xanchor target_x yanchor target_y xpos target_x ypos target_y zoom zoom_level


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


## Motion Sells Emotion: an ATL animation pack for Ren'Py, by EdgesSystem ######
## https://edgessystem.itch.io/motion-sells-emotion ############################
## This work is licensed under Creative Commons Attribution 4.0 International ##
## https://creativecommons.org/licenses/by/4.0/ ################################

define scale = 1.0

transform toleft:
    xzoom 1

transform toright:
    xzoom -1

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


################################################################################
## Positions
################################################################################

transform offscreenleft: 
    anchor (1.0,1.0)
    xpos 0.0

transform farleft:
    anchor (0.5,1.0)
    xpos 0.0

transform left: # ^
    anchor (0.5,1.0)
    xpos 0.1

transform leftish:
    anchor (0.5,1.0)
    xpos 0.25

transform centerleft:
    anchor (0.5,1.0)
    xpos 0.4

transform center: # ^
    anchor (0.5,1.0)
    xpos 0.5

transform centerright:
    anchor (0.5,1.0)
    xpos 0.6

transform rightish:
    anchor (0.5,1.0)
    xpos 0.75

transform right: # ^
    anchor (0.5,1.0)
    xpos 0.9

transform farright:
    anchor (0.5,1.0)
    xpos 1.0

transform offscreenright: # ^
    anchor (0.0,1.0)
    xpos 1.0


################################################################################
## Movement between positions
################################################################################

transform walkto(location,steps=5,walktime=2.0,bounce=1,sway=1):
    parallel:
        ease walktime location
    parallel:
        linear walktime/(steps*2) yoffset -10*bounce
        linear walktime/(steps*2) yoffset 0
        repeat steps
    parallel:
        linear walktime/(steps*4) rotate -sway
        linear walktime/(steps*2) rotate sway
        linear walktime/(steps*4) rotate 0
        repeat steps

transform leapto(location,windup=1,power=1,airtime=1):
    ease windup yoffset 10*windup
    parallel:
        easein 0.4*airtime yoffset -100*power
        easeout 0.4*airtime yoffset 0
        easein_circ 0.1*airtime yoffset 10*power
        ease 0.1*airtime yoffset 0
    parallel:
        easein airtime location

transform fast_moveoutright:
    yalign 0.5
    easeout 0.5 xalign 1.5

transform slow_moveoutright:
    yalign 0.5
    easeout 1.0 xalign 2.0

transform slow_moveoutleft:
    yalign 0.5
    easeout 1.0 xalign -1.0

transform slide_in_left:
    xpos -0.5 xanchor 1.0
    yalign 1.0
    ease 1.5 xpos 0.55 xanchor 0.5
    ease 0.15 xpos 0.5

transform slide_in_right:
    xpos 1.5 xanchor 1.0
    yalign 1.0
    ease 1.0 xpos 0.55 xanchor 0.5
    ease 0.15 xpos 0.5

transform enter_from_left_to_center:
    xpos -0.5 
    xanchor 0.5
    yalign 1.0
    ease 1.5 xpos 0.5

transform slow_enter_from_left_to_center:
    xpos -0.5 
    xanchor 0.5
    yalign 1.0
    ease 2.5 xpos 0.5

transform enter_from_right_to_center:
    xpos 1.5 
    xanchor 0.5
    yalign 1.0
    ease 1.5 xpos 0.5

transform enter_from_right_slow(target_x=0.5, dur=2.5):
    xpos 1.5
    xanchor 0.5
    yalign 1.0
    ease dur xpos target_x

transform enter_from_left_to_leftish(target_x=0.25, dur=1.5):
    xpos -0.5
    xanchor 0.25
    yalign 1.0
    ease dur xpos target_x


## Other transforms
transform zoom_to(target_x, target_y, zoom_level=2.0):
    xanchor target_x
    yanchor target_y
    xpos    target_x
    ypos    target_y
    zoom    zoom_level

transform pan_to(target_x, target_y, zoom_level=1.8, dur=1.0):
    linear dur xanchor target_x yanchor target_y xpos target_x ypos target_y zoom zoom_level

define wipeleft_fast   = CropMove(0.25, "wipeleft")
define wipeleft_medium = CropMove(0.50, "wipeleft")
define wiperight_fast   = CropMove(0.25, "wiperight")
define wiperight_medium = CropMove(0.50, "wiperight")

transform fall_and_recover(height=400, fall_time=0.5, ground_time=1.0, recover_time=0.6, recover_offset=50):
    anchor (0.5, 1.0)
    yoffset 0
    rotate 0
    easein fall_time yoffset height rotate 90
    linear ground_time yoffset height rotate 90
    easeout recover_time yoffset recover_offset rotate 0

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


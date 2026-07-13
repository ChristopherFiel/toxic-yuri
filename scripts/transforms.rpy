## Motion Sells Emotion: an ATL animation pack for Ren'Py, by EdgesSystem ######
## https://edgessystem.itch.io/motion-sells-emotion ############################
## This work is licensed under Creative Commons Attribution 4.0 International ##
## https://creativecommons.org/licenses/by/4.0/ ################################

define scale = 1  # ~10% larger across all shots (1/1.1)


################################################################################
## Facing
################################################################################

transform toleft:
    xzoom 1

transform toright:
    xzoom -1


################################################################################
## Shot distance (zoom level)
################################################################################

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


################################################################################
## Static positions (snap, no animation)
################################################################################

transform offscreenleft:
    anchor (1.0, 1.0)
    xpos 0.0

transform farleft:
    anchor (0.55, 1.0)
    xpos 0.0

transform left:
    anchor (0.55, 1.0)
    xpos 0.1

transform leftish:
    anchor (0.55, 1.0)
    xpos 0.25

transform centerleft:
    anchor (0.55, 1.0)
    xpos 0.3

transform center:
    anchor (0.55, 1.0)
    xpos 0.45

transform center_lower:
    anchor (0.45, 1.0)
    xpos 0.45
    yanchor 1.0
    ypos 1.0
    yoffset -200

transform center_lowest:
    anchor (0.35, 1.0)
    xpos 0.25
    yanchor 1.0
    ypos 1.0
    yoffset -400

transform center_upper:
    anchor (0.45, 1.0)
    xpos 0.45
    yanchor 1.0
    ypos 1.0
    yoffset 200

transform center_uppest:
    anchor (0.45, 1.0)
    xpos 0.45
    yanchor 1.0
    ypos 1.0
    yoffset 600

transform centerright:
    anchor (0.55, 1.0)
    xpos 0.7

transform righty:
    anchor (0.55, 1.0)
    xpos 0.6

transform rightish:
    anchor (0.55, 1.0)
    xpos 0.75

transform right:
    anchor (0.55, 1.0)
    xpos 0.9

transform farright:
    anchor (0.55, 1.0)
    xpos 1.0

transform offscreenright:
    anchor (0.0, 1.0)
    xpos 1.0


################################################################################
## Animated movement — entrances / exits
################################################################################

transform fast_moveoutright:
    yalign 1.0
    easeout 0.5 xalign 1.5

transform slow_moveoutright:
    yalign 1.0
    easeout 1.0 xalign 2.0

transform bus_slow_moveoutright:
    yalign -4.0
    easeout 1.0 xalign 2.0

transform fast_moveoutleft:
    yalign 1.0
    easeout 0.5 xalign -1.0

transform slow_moveoutleft:
    yalign 1.0
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
    ease 1.5 xpos 0.45

transform slow_enter_from_left_to_center:
    xpos -0.5
    xanchor 0.5
    yalign 1.0
    ease 2.5 xpos 0.45

transform enter_from_right_to_center:
    xpos 1.5
    xanchor 0.5
    yalign 1.0
    ease 1.5 xpos 0.45

transform enter_from_right_to_rightish(target_x=0.75, dur=1.5):
    xpos 1.5
    xanchor 0.75
    yalign 1.0
    ease dur xpos target_x

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

transform enter_from_left_slow(target_x=0.1, dur=1.5):
    xpos -0.5
    xanchor 0.5
    yalign 1.0
    ease dur xpos target_x


################################################################################
## Animated movement — reposition an already-shown sprite
################################################################################
## Always pair these with an explicit shot-distance transform (full, medlong,
## medium, etc.) in the same show block — these only control position, not zoom.

transform slide_to(x, dur=1.0):
    anchor (0.55, 1.0)
    ease dur xpos x

transform slide_to_vert(y, dur=1.0):
    anchor (0.55, 1.0)
    ease dur ypos y

transform slide_off_right(dur=1.0):
    xanchor 0.5
    easeout dur xpos 1.5


################################################################################
## Falls / shakes / zooms
################################################################################

transform fall_and_recover(height=400, fall_time=0.5, ground_time=1.0, recover_time=0.6, recover_offset=50, settle_time=0.3):
    yoffset 0
    rotate 0
    easein fall_time yoffset height rotate 90
    linear ground_time yoffset height rotate 90
    easeout recover_time yoffset recover_offset rotate 0
    ease settle_time yoffset 0

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

transform zoom_to(target_x, target_y, zoom_level=2.0):
    xanchor target_x
    yanchor target_y
    xpos    target_x
    ypos    target_y
    zoom    zoom_level

transform pan_to(target_x, target_y, zoom_level=1.8, dur=1.0):
    linear dur xanchor target_x yanchor target_y xpos target_x ypos target_y zoom zoom_level


################################################################################
## Scene transitions
################################################################################

define wipeleft_fast    = CropMove(0.25, "wipeleft")
define wipeleft_medium  = CropMove(0.50, "wipeleft")
define wiperight_fast   = CropMove(0.25, "wiperight")
define wiperight_medium = CropMove(0.50, "wiperight")


################################################################################
## Effects
################################################################################

transform flicker(rate=1, min=0.45, max=0.5):
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

transform bump(dx=-30, dur=0.15):
    easeout dur xoffset dx
    easein dur xoffset 0

################################################################################
## Reactions
################################################################################

transform school_pop:
    ease 0.15 zoom 1.15

transform school_idle:
    ease 0.15 zoom 1.0
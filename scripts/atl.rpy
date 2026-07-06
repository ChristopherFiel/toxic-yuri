init python:
    # first-person blink
    def eyewarp(x):
        return x ** 1.33

    # ATL transition
    eyeclose = ImageDissolve("wipes/eye.png", 0.25, ramplen=128, reverse=True, time_warp=eyewarp)
    eyeopen = ImageDissolve("wipes/eye.png", 0.5, ramplen=128, reverse=False, time_warp=eyewarp)


init python:
    # first-person blink (slow)
    def eyewarp(x):
        return x ** 1.33

    # ATL transition
    eyeclose_slow = ImageDissolve("wipes/eye.png", 1.0, ramplen=256, reverse=True, time_warp=eyewarp)
    eyeopen_slow = ImageDissolve("wipes/eye.png", 0.5, ramplen=256, reverse=False, time_warp=eyewarp)

init python:
    # first-person blink
    def eyewarp(x):
        return x ** 1.33

    # ATL transition
    eyeclose_fast = ImageDissolve("wipes/eye.png", 0.1, ramplen=128, reverse=True, time_warp=eyewarp)
    eyeopen_fast = ImageDissolve("wipes/eye.png", 0.25, ramplen=128, reverse=False, time_warp=eyewarp)


init:
    transform additive_blend:
        additive 1.0

    transform floating:
        yoffset 0
        ease 1. yoffset -5
        ease 1. yoffset 0
        repeat